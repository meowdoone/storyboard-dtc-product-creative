---
name: storyboard-dtc-product-creative
description: Use when a user wants a SKU-level DTC product creative storyboard from an Amazon, Shopify, TikTok Shop, ecommerce URL, product image, screenshot, ASIN, SKU brief, or short product description. Lock product truth, collect and decompose DTC references, run DTC Creative Director, produce a DTC Creative Reference Pack, then create product image, horizontal 5-panel storyboard image, and 15s or 30s English script.
---

# DTC 商品创意故事版 Skill

## Purpose

Turn one real SKU into a DTC product-led creative storyboard package for StoreClaw, FYPro, image-to-video, Amazon listing demo, Shopify PDP video, paid social, or brand creative testing.

This skill has two internal roles:

```text
DTC Creative Director
Storyboard Design Expert
```

`DTC Creative Director` chooses the creative logic before image generation. It does not generate final images.

`Storyboard Design Expert` uses only the `DTC Creative Reference Pack` to generate the horizontal 5-panel storyboard and English video script. It does not choose a new creative direction.

Default final response contains only:

```text
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` must contain one actual horizontal single-row storyboard/contact-sheet image with five 16:9 landscape panels. Do not replace it with a text shot list, prompt, table, or strategy.

The script text must be English. Chinese labels are allowed in table headers, but `屏幕字幕`, `旁白 / 口播`, `Camera / Motion`, and `Reference Logic` values must be natural English.

## Product Truth Lock

Before reference collection, creative planning, image generation, or scripting, create an internal Product Truth Card.

```yaml
product_truth_card:
  product_type:
  product_name:
  brand_or_seller:
  source_evidence:
    - source_url:
      evidence_type: product_page | product_image | screenshot | asin | sku_brief | user_asset
      captured_fact:
  visual_facts:
    shape:
    color:
    material:
    texture:
    package:
    logo_or_label:
    visible_components:
    size_ratio:
  product_behavior:
    how_it_is_used:
    who_uses_it:
    where_it_is_used:
    what_action_it_requires:
  proof_assets:
    visible_detail:
    visible_result:
    visible_mechanism:
    visible_comparison:
  allowed_claims:
  unsupported_claims:
  locked_terms:
  forbid_mutations:
  evidence_conflicts:
```

Completion criteria:

- `source_evidence` contains at least one reliable product page, product image, screenshot, ASIN record, SKU brief, or user asset.
- `locked_terms` preserves SKU-critical words: product type, color, material, silhouette, size/fit, label/logo, customization state, and visible design asset.
- `forbid_mutations` names concrete drift risks.
- Unsupported claims are absent from `allowed_claims`.
- Evidence conflicts are recorded instead of silently resolved.

If product truth is insufficient, stop before storyboard generation. Ask for product evidence or mark the result as rough concept. Do not create a final product-containing storyboard from a brief alone.

## Main Flow

Run these steps in order:

```text
1. Product Truth Lock
2. Live DTC Ad Reference Collection
3. Ad Reference Decomposition
4. DTC Creative Director
5. DTC Creative Reference Pack
6. Storyboard Design Expert
7. Horizontal 5-Panel Storyboard Image Generation
8. English Video Demo Script
9. Final QA
```

### 1. Product Truth Lock

Build the Product Truth Card and select one primary category adapter from [references/category-adapters.md](references/category-adapters.md).

Completion: product facts, locked terms, forbidden mutations, category adapter, evidence conflicts, and allowed claims are explicit.

### 2. Live DTC Ad Reference Collection

Build a crawl plan and collect public, authorized, user-provided, local, or fallback references using [references/live-crawl-strategy.md](references/live-crawl-strategy.md) and [references/source-compliance-policy.md](references/source-compliance-policy.md).

Public sources default to URL, summary, permitted screenshot/keyframe, and structured decomposition. Original videos, full ad files, brand assets, and private assets require `authorized` or `user_provided` source type.

Completion: every source attempt has a `source_record`, including blocked-source fallback records.

### 3. Ad Reference Decomposition

Convert selected references into `ad_reference` records using [references/ad-reference-analysis-schema.md](references/ad-reference-analysis-schema.md).

Completion: every selected reference states what can be borrowed and what must not be copied for this SKU.

### 4. DTC Creative Director

Run DTC Creative Director before storyboard generation. It must select these in order:

```text
Step 1: Select creative_type
Step 2: Select scene_ref
Step 3: Select motion_chain
Step 4: Select model_ref
Step 5: Select camera_plan
Step 6: Select script_pattern
Step 7: Select picture_fragment_logic
Step 8: Output DTC Creative Reference Pack
```

Use:

- creative types from [references/dtc-creative-pattern-library.md](references/dtc-creative-pattern-library.md)
- scene refs from [references/dtc-scene-library.md](references/dtc-scene-library.md)
- motion refs from [references/dtc-motion-library.md](references/dtc-motion-library.md)
- model refs from [references/dtc-model-library.md](references/dtc-model-library.md)
- camera refs from [references/camera-language-library.md](references/camera-language-library.md)
- pack schema from [references/dtc-director-reference-pack-schema.md](references/dtc-director-reference-pack-schema.md)

Completion: exactly one main `creative_type` is selected, every scene/motion/model/camera choice serves product truth, and the Reference Pack is complete.

### 5. DTC Creative Reference Pack

Create the internal `DTC Creative Reference Pack`. It is the only creative input for Storyboard Design Expert.

Required top-level fields:

```yaml
dtc_creative_reference_pack:
  product_truth_lock:
  creative_type:
  selected_ad_references:
  scene_selection:
  motion_selection:
  model_selection:
  camera_selection:
  script_pattern:
  picture_fragment_logic:
  rejected_references:
  adaptation_reason:
```

Completion: pack includes `creative_type`, `scene_selection`, `motion_selection`, `model_selection`, and `camera_selection`. Without this pack, do not generate storyboard image.

### 6. Storyboard Design Expert

Storyboard Design Expert must not invent a new creative direction. It uses only:

- `product_truth_lock`
- `creative_type`
- `selected_ad_references`
- `scene_selection`
- `motion_selection`
- `model_selection`
- `camera_selection`
- `script_pattern`
- `picture_fragment_logic`

Completion: the five-panel plan follows [references/storyboard-video-keyframe-rules.md](references/storyboard-video-keyframe-rules.md), and panel 3 is the strongest product proof.

### 7. Horizontal 5-Panel Storyboard Image Generation

Generate or assemble one actual horizontal single-row contact sheet with five 16:9 landscape panels.

Image generation prompt must include:

```text
1. product_truth_lock
2. creative_type
3. selected_ad_reference logic
4. scene_ref
5. model_ref
6. motion_chain
7. camera_plan
8. picture_fragment_logic
9. five-panel video keyframe plan
10. horizontal 16:9 contact sheet constraint
11. same shoot / same product / same lighting continuity
12. real physical contact shadows
13. no fake UI / no fake claims / no fake reviews
```

Completion: the result is an actual image, not text-only storyboard; every panel is a video-ready keyframe.

### 8. English Video Demo Script

Default to 15 seconds. Use 30 seconds only when requested.

```markdown
| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

Completion: `Camera / Motion` matches `camera_selection` and `motion_selection`; `Reference Logic` explains borrowed structure without naming specific brands; all script-facing text is English.

### 9. Final QA

Run [scripts/validate_storyboard.py](scripts/validate_storyboard.py) when local files exist.

Completion:

- final response remains the three user-facing sections,
- `run.json`, `source_records.json`, and `qa.json` exist for local runs,
- `qa.json` contains `source_url` and `locked_terms`,
- contact sheet is horizontal single-row,
- five panel images are 16:9,
- panel 3 is strongest product proof,
- every panel is video-keyframe ready,
- product truth, Reference Pack, storyboard, and script agree.

## Hard Rules

1. Do not generate storyboard before `DTC Creative Reference Pack` exists.
2. Do not let Storyboard Design Expert choose `creative_type` again.
3. Do not choose multiple main creative types.
4. Do not choose a scene that cannot naturally contain the product.
5. Do not choose a motion that cannot be shown as `start_state -> action -> end_state`.
6. Do not choose a model strategy that steals attention from the product.
7. Do not choose camera language only for style; it must support hook, proof, use, or CTA.
8. Panel 3 must contain the strongest product proof.
9. Every panel must be video-ready keyframe.
10. Script `Camera / Motion` must match `camera_selection` and `motion_selection`.

## Required Local Artifacts

The final user-facing response stays three sections, but every executed local run should save:

```text
run.json
source_records.json
qa.json
```

`run.json` should include `product_truth_card`, selected category adapters, `dtc_director_input`, `dtc_creative_reference_pack`, and output paths.

`source_records.json` should include all source records and fallback records.

`qa.json` should include `source_url`, `locked_terms`, `forbid_mutations`, `creative_type`, `scene_ref`, `motion_chain`, `model_ref`, `camera_plan`, `panel_count`, `panel_aspect_ratio`, `contact_sheet`, `contact_sheet_layout`, and pass/fail flags.

## Output Contract

Use this shape in the final answer:

```markdown
## 1. 产品图

![产品图](...)

## 2. 故事版

创意大片方向：...

同一拍摄世界锁：...

![5 格 16:9 横屏故事版](...)

## 3. 15 秒或者 30 秒视频脚本文字

| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

Do not expose Product Truth Card, full Reference Pack, source records, JSON, or QA notes in the final response unless the user asks for them.
