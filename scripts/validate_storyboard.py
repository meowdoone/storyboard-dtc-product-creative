#!/usr/bin/env python3
"""Validate a local storyboard-dtc-product-creative output directory."""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Iterable


IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
CONTACT_SHEET_MIN_RATIO = 4.0
PANEL_RATIO = 16 / 9
PANEL_RATIO_TOLERANCE = 0.04


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as file:
        header = file.read(24)
    if len(header) < 24 or not header.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def read_jpeg_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as file:
        data = file.read()
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG file")

    idx = 2
    while idx < len(data):
        if data[idx] != 0xFF:
            idx += 1
            continue
        while idx < len(data) and data[idx] == 0xFF:
            idx += 1
        if idx >= len(data):
            break
        marker = data[idx]
        idx += 1
        if marker in {0xD8, 0xD9}:
            continue
        if idx + 2 > len(data):
            break
        segment_len = struct.unpack(">H", data[idx : idx + 2])[0]
        if segment_len < 2 or idx + segment_len > len(data):
            break
        if marker in {
            0xC0,
            0xC1,
            0xC2,
            0xC3,
            0xC5,
            0xC6,
            0xC7,
            0xC9,
            0xCA,
            0xCB,
            0xCD,
            0xCE,
            0xCF,
        }:
            if idx + 7 > len(data):
                break
            height = struct.unpack(">H", data[idx + 3 : idx + 5])[0]
            width = struct.unpack(">H", data[idx + 5 : idx + 7])[0]
            return width, height
        idx += segment_len
    raise ValueError("could not find JPEG dimensions")


def read_image_size(path: Path) -> tuple[int, int]:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return read_png_size(path)
    if suffix in {".jpg", ".jpeg"}:
        return read_jpeg_size(path)
    raise ValueError(f"unsupported image type: {suffix}")


def is_nonempty(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise ValueError(f"missing required file: {path.name}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.name}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return data


def resolve_path(output_dir: Path, value: object, fallback: Path) -> Path:
    if isinstance(value, str) and value.strip():
        path = Path(value)
        return path if path.is_absolute() else output_dir / path
    return fallback


def list_panel_paths(output_dir: Path, qa: dict) -> list[Path]:
    raw_panel_paths = qa.get("panel_paths")
    if isinstance(raw_panel_paths, list) and raw_panel_paths:
        return [
            path if path.is_absolute() else output_dir / path
            for item in raw_panel_paths
            if isinstance(item, str)
            for path in [Path(item)]
        ]

    panels_dir = output_dir / "panels"
    if not panels_dir.exists():
        return []
    return sorted(
        path
        for path in panels_dir.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS
    )


def validate_qa(qa: dict) -> list[str]:
    errors: list[str] = []
    for field in [
        "source_url",
        "locked_terms",
        "creative_type",
        "scene_ref",
        "motion_chain",
        "model_ref",
        "camera_plan",
    ]:
        if not is_nonempty(qa.get(field)):
            errors.append(f"qa.json missing non-empty `{field}`")
    camera_plan = qa.get("camera_plan")
    if isinstance(camera_plan, dict):
        for field in [
            "opening_camera",
            "context_camera",
            "proof_camera",
            "use_camera",
            "end_frame_camera",
        ]:
            if not is_nonempty(camera_plan.get(field)):
                errors.append(f"qa.json `camera_plan` missing non-empty `{field}`")
    elif "camera_plan" in qa:
        errors.append("qa.json `camera_plan` must be an object")
    if qa.get("panel_count") not in (None, 5):
        errors.append("qa.json `panel_count` must be 5 when present")
    if qa.get("panel_aspect_ratio") not in (None, "16:9"):
        errors.append("qa.json `panel_aspect_ratio` must be `16:9` when present")
    return errors


def validate_contact_sheet(output_dir: Path, qa: dict) -> list[str]:
    errors: list[str] = []
    contact_sheet = resolve_path(output_dir, qa.get("contact_sheet"), output_dir / "contact_sheet.png")
    if not contact_sheet.exists():
        return [f"contact sheet not found: {contact_sheet}"]

    try:
        width, height = read_image_size(contact_sheet)
    except ValueError as exc:
        return [f"contact sheet size read failed: {exc}"]

    if width <= height:
        errors.append(
            f"contact sheet must be horizontal single-row; got {width}x{height}"
        )
    if height > 0 and width / height < CONTACT_SHEET_MIN_RATIO:
        errors.append(
            f"contact sheet ratio too narrow for five landscape panels; got {width / height:.3f}"
        )
    if qa.get("contact_sheet_layout") not in (None, "horizontal_single_row"):
        errors.append("qa.json `contact_sheet_layout` must be `horizontal_single_row` when present")
    return errors


def validate_panels(output_dir: Path, qa: dict) -> list[str]:
    errors: list[str] = []
    panels = list_panel_paths(output_dir, qa)
    if len(panels) != 5:
        errors.append(f"expected 5 panel images, found {len(panels)}")
        return errors

    for panel in panels:
        if not panel.exists():
            errors.append(f"panel not found: {panel}")
            continue
        try:
            width, height = read_image_size(panel)
        except ValueError as exc:
            errors.append(f"{panel.name} size read failed: {exc}")
            continue
        if height <= 0:
            errors.append(f"{panel.name} has invalid height 0")
            continue
        ratio = width / height
        if abs(ratio - PANEL_RATIO) > PANEL_RATIO_TOLERANCE:
            errors.append(f"{panel.name} must be 16:9; got {width}x{height} ratio={ratio:.3f}")
    return errors


def validate_output(output_dir: Path) -> list[str]:
    qa_path = output_dir / "qa.json"
    try:
        qa = load_json(qa_path)
    except ValueError as exc:
        return [str(exc)]

    errors: list[str] = []
    for required_json in ["run.json", "source_records.json"]:
        try:
            load_json(output_dir / required_json)
        except ValueError as exc:
            errors.append(str(exc))
    errors.extend(validate_qa(qa))
    errors.extend(validate_contact_sheet(output_dir, qa))
    errors.extend(validate_panels(output_dir, qa))
    return errors


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a storyboard output directory for horizontal 5-panel DTC storyboard delivery."
    )
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)

    output_dir = args.output_dir.expanduser().resolve()
    if not output_dir.exists():
        print(f"ERROR: output directory not found: {output_dir}", file=sys.stderr)
        return 2
    if not output_dir.is_dir():
        print(f"ERROR: output path is not a directory: {output_dir}", file=sys.stderr)
        return 2

    errors = validate_output(output_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: storyboard output valid: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
