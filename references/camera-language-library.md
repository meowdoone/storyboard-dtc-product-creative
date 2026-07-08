# DTC Camera Language Library

## Purpose

`camera_plan` makes each storyboard panel video-keyframe ready. Camera is not style decoration; it must support hook, proof, use, or CTA.

## Schema

```yaml
camera_ref:
  id:
  best_for:
  shot_size:
  camera_position:
  camera_motion:
  product_role:
  video_keyframe_use:
  transition_logic:
  risk:
```

## Camera Entries

| id | best_for | shot_size | camera_position | camera_motion | product_role | video_keyframe_use | transition_logic | risk |
|---|---|---|---|---|---|---|---|---|
| locked-off-demo | clear operation, size, use relation | medium close-up | fixed 45-degree or eye-level | no movement; action happens inside frame | product readable throughout | demo and proof panels | cut on completed action | stable but plain |
| top-down-tabletop | unbox, choice, placement, customization, alignment | top-down medium | overhead | slight tracking or fixed | product and hands clearly visible | panel 1-3 setup/proof | hand movement leads next frame | flat diagram feel |
| macro-push-in | material, texture, structure, button, port, package detail | macro close-up | close product detail | slow push-in | product detail hero | panel 3 strongest proof | push into detail then cut to use | AI over-sharp/fake material |
| handheld-follow | UGC, real use, travel, sport, home routine | close or medium close-up | follows hand/product | subtle handheld follow | product stays near center | panel 2 or 4 use action | motion continues across cut | blur/shake hides product |
| slow-dolly | hero shot, premium product display, brand feel | medium to close-up | frontal or 45-degree | slow dolly in/out | product gains importance | panel 5 hero confidence | camera settles into end frame | empty premium mood |
| rack-focus | product/context relation, human-to-product transition | medium close-up | foreground/background relation | focus shift | focus lands on product | panel 1 hook or panel 2 context | focus shift reveals product | product may be unclear |
| tabletop-tracking | desk/table process, unbox, align, choice, compare | top-down or 45-degree | parallel to table movement | horizontal track | product moves along frame | panel 2-4 motion chain | track direction carries continuity | too many props |
| orbit-product-reveal | appearance, structure, multi-angle detail | close-up / hero close-up | around product | slight orbit | product center hero | panel 3 or 5 | orbit reveals side/detail | 3D fake feel |
| hero-reveal | final frame, gift, packaging, selected configuration | clean product hero | front or 45-degree | settle or reveal | product dominates final frame | panel 5 | action resolves into hero | pretty but not confidence |
| match-cut | connect actions or scenes | varies | matched composition | matched action direction | product connects moments | panel transitions | match shape/motion/direction | complex for image generation |
| split-screen-comparison | comparison, choice, before/after, size/color/version | two-panel comparison inside frame | symmetrical | minimal | difference visible | panel 3 proof | split resolves to chosen product | fake competitor/result |
| over-the-shoulder-product-check | choice, detail check, shopping judgement, car/desk context | over-shoulder close-up | behind user, product in hands/surface | subtle push or fixed | product is what user checks | panel 2 buyer context | gaze/hand directs proof frame | person back steals frame |

## Camera Plan Slots

```yaml
camera_plan:
  opening_camera:
  context_camera:
  proof_camera:
  use_camera:
  end_frame_camera:
```

Panel 3 should usually use `macro-push-in`, `locked-off-demo`, `split-screen-comparison`, or another proof-first camera that makes the product detail inspectable.
