# Storyboard Video Keyframe Rules

## Total Image Rule

The storyboard must be one actual image.

The image must be:

- landscape,
- horizontal,
- five-panel,
- 16:9 contact sheet,
- single-row by default,
- video-keyframe ready.

Do not deliver a text storyboard, shot list, table, or prompt as the storyboard.

## Panel Schema

```yaml
storyboard_panel:
  panel_number:
  content_task:
  creative_type:
  scene_ref:
  model_ref:
  motion_ref:
  camera_ref:
  product_truth_lock:
  visual_fragment_logic:
  continuity_from_previous:
  video_generation_note:
```

## Fixed Five-Panel Plan

```yaml
panel_plan:
  panel_1:
    role: Hook + Product Entrance
    must_show:
      - product appears clearly
      - hook visual from creative_type
      - scene anchor begins
    camera:
      - opening_camera
    motion:
      - first motion in motion_chain
    failure:
      - product not visible
      - hook unrelated to product
      - looks like generic lifestyle

  panel_2:
    role: Buyer Tension / Context
    must_show:
      - buyer problem, choice, routine, or use context
      - selected scene_ref
      - selected model_ref if needed
    camera:
      - context_camera
    motion:
      - setup motion
    failure:
      - scene is decorative only
      - buyer tension unclear
      - person steals attention

  panel_3:
    role: Strongest Product Proof
    must_show:
      - key product detail
      - proof_asset
      - mechanism, material, fit, texture, size, option, or use proof
    camera:
      - proof_camera
    motion:
      - proof motion
    failure:
      - no proof
      - only pretty shot
      - claim not visually supported

  panel_4:
    role: Use Moment / Benefit / Objection Resolution
    must_show:
      - action completing
      - product benefit becoming visible
      - objection being answered
    camera:
      - use_camera
    motion:
      - action completion
    failure:
      - new claim appears
      - action does not follow panel 3
      - product becomes secondary

  panel_5:
    role: CTA Intent / Purchase Confidence / Hero Frame
    must_show:
      - product-dominant final frame
      - reason to trust or choose
      - clean CTA intent
    camera:
      - end_frame_camera
    motion:
      - camera settles or product resolves
    failure:
      - only aesthetic ending
      - product unclear
      - CTA not connected to proof
```

## Video-Ready Keyframe Criteria

Every panel must:

- show the product clearly,
- preserve Product Truth Card locks,
- inherit `creative_type`, `scene_ref`, `model_ref`, `motion_ref`, and `camera_ref`,
- contain a visible action state that can continue into image-to-video,
- include real physical contact or plausible contact shadows,
- carry continuity from the previous panel,
- avoid fake UI, fake reviews, fake claims, fake badges, and unsupported result shots.

Panel 3 is non-negotiable: it must be the strongest product proof frame. If panel 3 does not show product proof, regenerate before scripting.

## Script Binding

The English script row for each panel must bind to the same camera and motion:

```text
panel camera_ref + motion_ref -> script Camera / Motion
panel borrowed logic -> script Reference Logic
panel visual proof -> subtitle and voiceover
```

Do not use voiceover to compensate for missing proof in the image.
