# DTC Creative Reference Pack Schema

## Purpose

`DTC Creative Reference Pack` is the handoff from `DTC Creative Director` to `Storyboard Design Expert`.

It is the only creative input for storyboard generation. If the pack is missing or incomplete, do not generate the storyboard image.

## DTC Director Input

```yaml
dtc_director_input:
  product_truth_card:
    product_type:
    product_category:
    product_visual_facts:
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
    unsupported_claims:
    buyer_decision:
      target_buyer:
      buyer_stage:
      buyer_objection:
      reason_to_believe:
      cta_intent:

  ad_references:
    - source_url:
      source_type:
      platform:
      brand:
      category:
      product_type:
      format:
      aspect_ratio:
      duration:
      hook:
      scene:
      model:
      motion:
      camera:
      proof:
      script:
      reusable_pattern:
```

## Pack Schema

```yaml
dtc_creative_reference_pack:
  product_truth_lock:
    product_type:
    visual_facts:
    use_behavior:
    proof_assets:
    unsupported_claims:

  creative_type:
    id:
    reason:
    buyer_tension:
    proof_asset:
    risk:

  selected_ad_references:
    - source_url:
      source_type:
      platform:
      brand:
      format:
      aspect_ratio:
      borrowed_structure:
      borrowed_scene_logic:
      borrowed_motion_logic:
      borrowed_camera_logic:
      borrowed_script_logic:
      picture_fragment_logic:
      what_not_to_copy:

  scene_selection:
    scene_ref:
    source_reference:
    location:
    surface:
    lighting:
    props_allowed:
    props_forbidden:
    horizontal_16_9_notes:
    reason:

  motion_selection:
    motion_chain:
      - motion_ref:
        start_state:
        action:
        end_state:
        human_action:
        product_action:
        camera_support:
        panel_usage:
    continuity_note:

  model_selection:
    model_ref:
    presence_type:
    role:
    visibility:
    wardrobe:
    hand_or_body_visibility:
    continuity_lock:
    reason:

  camera_selection:
    camera_plan:
      opening_camera:
      context_camera:
      proof_camera:
      use_camera:
      end_frame_camera:
    transition_logic:
    reason:

  script_pattern:
    hook_line_logic:
    proof_line_logic:
    CTA_line_logic:
    pacing_structure:

  picture_fragment_logic:
    panel_1:
    panel_2:
    panel_3:
    panel_4:
    panel_5:

  rejected_references:
    - source_url:
      reason:

  adaptation_reason:
```

## Completion Criteria

- `creative_type` is exactly one main type.
- `scene_selection`, `motion_selection`, `model_selection`, and `camera_selection` are present.
- `motion_selection.motion_chain` uses `start_state -> action -> end_state`.
- `camera_selection.camera_plan.proof_camera` supports panel 3 product proof.
- `picture_fragment_logic.panel_3` is the strongest product proof.
- `selected_ad_references` all have `source_url` or local source path.
- `what_not_to_copy` explicitly protects Product Truth Card locks.

## Handoff Rule

Storyboard Design Expert must not re-select creative direction. It may only translate the pack into:

- one actual horizontal five-panel 16:9 storyboard image,
- one English 15s or 30s video script,
- local QA records.
