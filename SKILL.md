---
name: storyboard-dtc-product-creative
description: Use when a user wants a SKU-level DTC product creative storyboard or premium brand-film style product storyboard from ecommerce product evidence such as Amazon, Shopify, TikTok Shop, product images, screenshots, ASINs, SKU briefs, or short product descriptions. Produces a Product Truth Card, DTC Creative Reference Pack, Brand Film Look Pack, horizontal 5-panel storyboard image, and English 15s/30s script.
---

# DTC 商品创意故事版 Skill

## Purpose

Turn one real SKU into a DTC product-led creative storyboard package for StoreClaw, Amazon listing demo, Shopify PDP video, paid social, or brand creative testing.

This skill has two internal roles:

```text
DTC Creative Director
Brand Film Look Director
Storyboard Design Expert
```

`DTC Creative Director` chooses the creative logic before image generation. It does not generate final images.

`Brand Film Look Director` turns the selected DTC creative logic into concrete camera, light, material, rhythm, and end-frame rules. It does not change SKU facts or choose a new creative direction.

`Storyboard Design Expert` uses only the `DTC Creative Reference Pack` and `Brand Film Look Pack` to generate the horizontal 5-panel storyboard and English video script. It does not choose a new creative direction.

Default final response contains only:

```text
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` embeds or links the generated storyboard/contact-sheet image with five 16:9 landscape panels.

The script text must be English. Chinese labels are allowed in table headers, but `屏幕字幕`, `旁白 / 口播`, `Camera / Motion`, and `Reference Logic` values must be natural English.

## Execution Contract

Run the workflow as production work, not as advice. For every run:

1. Create the internal records required by each step.
2. Save `run.json` and `source_records.json` when filesystem access exists.
3. Create or attach the contact sheet and panel assets when image generation or image assembly is available.
4. If a required capability is unavailable, record the blocked artifact and reason in `run.json` instead of silently downgrading the workflow.
5. Keep the final user-facing response to the three sections in the Output Contract.

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
6. Brand Film Look Director
7. Brand Film Look Pack
8. Storyboard Design Expert
9. Horizontal 5-Panel Storyboard Image Generation
10. English Video Demo Script
11. Delivery Validation
```

### 1. Product Truth Lock

Build the Product Truth Card. Read [references/category-adapters.md](references/category-adapters.md), select one primary adapter, and copy its required locks, buyer events, proof beats, and forbid mutations into the run.

Completion: product facts, locked terms, forbidden mutations, category adapter, evidence conflicts, and allowed claims are explicit.

### 2. Live DTC Ad Reference Collection

Read [references/live-crawl-strategy.md](references/live-crawl-strategy.md) and [references/source-compliance-policy.md](references/source-compliance-policy.md). Then build the crawl plan, attempt the source classes available in the current environment, and write every attempt into `source_records.json`.

Public sources default to URL, summary, permitted screenshot/keyframe, and structured decomposition. Original videos, full ad files, brand assets, and private assets require `authorized` or `user_provided` source type.

Completion: every source attempt has a `source_record`, including blocked-source fallback records.

### 3. Ad Reference Decomposition

Read [references/ad-reference-analysis-schema.md](references/ad-reference-analysis-schema.md). Convert every selected source into an `ad_reference` record with reusable structure, scene logic, motion logic, camera logic, script logic, and `what_not_to_copy`.

Completion: every selected reference states what can be borrowed and what must not be copied for this SKU.

### 4. DTC Creative Director

Run DTC Creative Director before storyboard generation. It must select these in order:

```text
Step 1: Select creative_type
Step 2: Select scene_ref
Step 3: Select motion_chain
Step 4: Select model_ref
Step 5: Select camera_plan
Step 6: Select brand_film_mode
Step 7: Select script_pattern
Step 8: Select picture_fragment_logic
Step 9: Select end_frame
Step 10: Output DTC Creative Reference Pack
```

Read these reference files and make the selections from them:

- creative types from [references/dtc-creative-pattern-library.md](references/dtc-creative-pattern-library.md)
- scene refs from [references/dtc-scene-library.md](references/dtc-scene-library.md)
- motion refs from [references/dtc-motion-library.md](references/dtc-motion-library.md)
- model refs from [references/dtc-model-library.md](references/dtc-model-library.md)
- camera refs from [references/camera-language-library.md](references/camera-language-library.md)
- brand film modes from [references/brand-film-mode-library.md](references/brand-film-mode-library.md)
- pack schema from [references/dtc-director-reference-pack-schema.md](references/dtc-director-reference-pack-schema.md)

Completion: exactly one main `creative_type` is selected through the buyer situation router, every scene/motion/model/camera/brand-film choice serves product truth, and the Reference Pack is complete.

Every selected `creative_type`, `scene_ref`, `motion_ref`, `model_ref`, and `camera_ref` must preserve the Chinese `description` field from its library so the pack states what each choice does, not only its ID.

`brand_film_mode` is internal brand-film language. Do not expose director names, film names, or "like this director" language in the final output.

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
  brand_film_mode:
  script_pattern:
  picture_fragment_logic:
  end_frame:
  rejected_references:
  adaptation_reason:
```

Completion: pack includes `creative_type`, `scene_selection`, `motion_selection`, `model_selection`, `camera_selection`, `brand_film_mode`, `picture_fragment_logic`, and `end_frame`. Without this pack, do not generate storyboard image.

Completion also requires Chinese descriptions for every selected library reference.

### 6. Brand Film Look Director

Run Brand Film Look Director after the Reference Pack exists and before storyboard planning. Read:

- [references/brand-film-look-director.md](references/brand-film-look-director.md)
- [references/brand-film-mode-library.md](references/brand-film-mode-library.md)
- [references/cinematic-grammar-rules.md](references/cinematic-grammar-rules.md)
- [references/brand-film-storyboard-qa.md](references/brand-film-storyboard-qa.md)

It must convert `brand_film_mode` into concrete visual rules:

```text
camera behavior
lens / shot distance
light direction
shadow and material treatment
color grade
motion pacing
shot function map
signature shot
end-frame rule
failure rules
```

Completion: Brand Film Look Director outputs `brand_film_look_pack` and does not expose director names, film names, or "like this director" language.

### 7. Brand Film Look Pack

Create the internal `Brand Film Look Pack`. It is the only brand-film visual input for Storyboard Design Expert.

Required top-level fields:

```yaml
brand_film_look_pack:
  brand_film_mode:
  brand_world_lock:
  cinematic_grammar:
  shot_function_map:
  material_and_light_rules:
  pacing_rules:
  signature_shot:
  end_frame_rule:
  failure_rules:
```

Completion: `shot_function_map` follows `picture_fragment_logic`, not fixed panel roles. `signature_shot` and `end_frame_rule` strengthen product proof and buyer confidence without inventing claims.

### 8. Storyboard Design Expert

Storyboard Design Expert must not invent a new creative direction. It uses only:

- `product_truth_lock`
- `creative_type`
- `selected_ad_references`
- `scene_selection`
- `motion_selection`
- `model_selection`
- `camera_selection`
- `brand_film_mode`
- `script_pattern`
- `picture_fragment_logic`
- `end_frame`
- `brand_film_look_pack`

Completion: the five-panel plan follows [references/storyboard-video-keyframe-rules.md](references/storyboard-video-keyframe-rules.md) and [references/brand-film-storyboard-qa.md](references/brand-film-storyboard-qa.md), every panel task comes from `picture_fragment_logic`, and the rhythm suggestion is used only when it fits the SKU evidence.

### 9. Horizontal 5-Panel Storyboard Image Generation

Generate or assemble one contact sheet with five 16:9 landscape panels. When filesystem access exists, save `contact_sheet.png` and five panel files under `panels/`.

Image generation prompt must include:

```text
1. product_truth_lock
2. creative_type
3. selected_ad_reference logic
4. scene_ref
5. model_ref
6. motion_chain
7. camera_plan
8. brand_film_mode
9. brand_film_look_pack
10. brand_world_lock
11. cinematic_grammar
12. shot_function_map
13. material_and_light_rules
14. picture_fragment_logic
15. end_frame
16. five-panel picture_fragment_logic
17. horizontal 16:9 contact sheet constraint
18. same shoot / same product / same lighting continuity
19. real physical contact shadows
20. no fake UI / no fake claims / no fake reviews
```

Completion: `contact_sheet.png` or an embedded image is present, five panel assets are available when local files can be saved, and every panel is a video-ready keyframe.

### 10. English Video Demo Script

Default to 15 seconds. Use 30 seconds only when requested.

```markdown
| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

Completion: `Camera / Motion` matches `camera_selection` and `motion_selection`; `Reference Logic` explains borrowed structure without naming specific brands; all script-facing text is English.

### 11. Delivery Validation

Run [scripts/validate_storyboard.py](scripts/validate_storyboard.py) when local files exist.

Completion:

- final response remains the three user-facing sections,
- `run.json` and `source_records.json` exist for local runs,
- `run.json` contains `source_url` and `locked_terms`,
- five panel images are 16:9,
- every panel is video-keyframe ready,
- product truth, Reference Pack, storyboard, and script agree.

## Hard Rules

1. Do not generate storyboard before `DTC Creative Reference Pack` exists.
2. Do not generate storyboard before `Brand Film Look Pack` exists.
3. Do not let Storyboard Design Expert choose `creative_type` again.
4. Do not choose multiple main creative types.
5. Do not choose a scene that cannot naturally contain the product.
6. Do not choose a motion that cannot be shown as `start_state -> action -> end_state`.
7. Do not choose a model strategy that hides the product or weakens product proof.
8. Do not choose camera language only for style; it must support hook, proof, use, or CTA.
9. Do not force fixed panel roles; panel tasks come from `picture_fragment_logic`.
10. Every panel must be video-ready keyframe.
11. Script `Camera / Motion` must match `camera_selection` and `motion_selection`.

## Required Local Artifacts

The final user-facing response stays three sections, but every executed local run saves:

```text
run.json
source_records.json
```

`run.json` includes `product_truth_card`, selected category adapters, `dtc_director_input`, `dtc_creative_reference_pack`, `brand_film_look_pack`, output paths, blocked artifacts if any, and validation fields: `source_url`, `locked_terms`, `forbid_mutations`, `creative_type`, `scene_ref`, `motion_chain`, `model_ref`, `camera_plan`, `brand_film_mode`, `brand_film_look_pack`, `end_frame`, `panel_count`, `panel_aspect_ratio`, and `contact_sheet`.

`source_records.json` includes all source records and fallback records.

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

Do not expose Product Truth Card, full Reference Pack, source records, JSON, or validation notes in the final response unless the user asks for them.
