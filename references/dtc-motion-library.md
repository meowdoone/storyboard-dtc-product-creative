# DTC Motion Library

## Purpose

`motion_chain` makes the storyboard video-ready. Every selected motion must have:

```text
start_state -> action -> end_state
```

## Schema

```yaml
motion_ref:
  id:
  best_for:
  start_state:
  action:
  end_state:
  human_action:
  product_action:
  camera_support:
  video_keyframe_use:
  continuity_note:
  risk:
```

## Motion Entries

| id | best_for | start_state | action | end_state | human_action | product_action | camera_support | video_keyframe_use | continuity_note | risk |
|---|---|---|---|---|---|---|---|---|---|---|
| pick-up | hand-held products | product rests on surface | hand picks product up | product enters use position or frame center | hand enters, grips, lifts | product moves from surface to hand | locked-off-demo / handheld-follow | panel 1 or 2 product entrance | hand shape and product angle continue | hand blocks product |
| unbox | packaging, kits, multi-part SKUs | package closed | open package and remove product | product and package relationship clear | hands open box, remove product | product revealed from package | top-down-tabletop / tabletop-tracking | panels 1-3 establish realness | do not invent accessories | packaging/product mismatch |
| align | install, fit, custom, sizing | product and target object separate | align product to target/object/print zone | position or size relation confirmed | hands align edges or placement | product moves into fit position | top-down-tabletop / locked-off-demo | panel 3 proof | target must be evidenced | invented compatibility |
| apply | care, patch, cream, body/surface contact | product near body/surface | apply, attach, or press | use state visible | hand applies product | product contacts surface/body | macro-push-in / handheld-follow | panel 3 or 4 proof/use | no exaggerated result | fake before/after |
| pour | liquid, drink, condiment, cleaner, container | container before tilt | pour liquid | liquid enters target container/surface | hand tilts product | liquid flows | macro-push-in / locked-off-demo | texture/capacity proof | fluid state realistic | impossible liquid |
| tap | electronic, switch, button, tool | finger near button/touch zone | tap or press | supported state/action completes | finger taps | product responds only if evidenced | macro-push-in / rack-focus | panel 3 mechanism proof | do not create fake UI | fictional feedback |
| plug-in | electronics, charging, connector fit | cable/port separate | insert or connect | connection visible | hand guides connector | connector enters port | macro-push-in / over-shoulder-product-check | compatibility proof | interface must match evidence | fake compatible device |
| wear | apparel, accessories, protective gear | product not worn | put on/wear/adjust | body placement clear | body/hand wears product | product fits body | handheld-follow / locked-off-demo | panels 2-4 use proof | body and product ratio stable | deformation/scale error |
| unfold | foldable, storage, apparel, portable | product folded/stored | unfold | full shape visible | hands unfold | product expands | top-down-tabletop / tabletop-tracking | panel 2 or 3 structure | before/after same product | shape jumps |
| fold | storage, apparel, portable | product open | fold | compact state visible | hands fold | product becomes compact | top-down-tabletop / handheld-follow | portability proof | folding logic real | unsupported structure |
| compare | size, color, version, neutral old method | two objects/versions visible | point, slide, or swap | difference visible | hand points or slides | product contrasted with neutral object | split-screen-comparison / locked-off-demo | panel 3 proof | compare only evidenced differences | fake competitor flaw |
| rotate | appearance, structure, packaging | product front/static | rotate | side/back/detail visible | hand or turntable rotates | product reveals another side | orbit-product-reveal / macro-push-in | product detail proof | logo/structure stable | different product appears |
| reveal | gift, unbox, custom, packaging, choice | product partly covered | remove cover/card/box | product visible | hand pulls cover/card | product becomes visible | hero-reveal / top-down-tabletop | panel 1 hook or panel 5 hero | cover cannot become fake brand asset | overdramatic reveal |
| hand-pass | gift, social, household sharing | product in one hand | pass to another hand | recipient holds product | two hands pass product | product remains visible | handheld-follow / locked-off-demo | social proof / CTA frame | same people/hands | people steal product |
| texture-touch | fabric, material, leather, paper, food, care | fingers near texture | touch, press, glide | subtle material response visible | fingers press/glide | texture responds subtly | macro-push-in | panel 3 sensory proof | response must be restrained | AI plastic feel |
| close-open | box, lid, bag, bottle, clasp, storage | product closed | open | inside/function state visible | hand opens lid/zip/flap | product changes state | top-down-tabletop / macro-push-in | mechanism or package proof | opening structure real | invented internals |

## Motion Checks

Reject a motion choice when:

- the action cannot be shown in a still keyframe,
- the product does not support the action,
- the action requires unsupported claims,
- the selected camera cannot show the action,
- panel 3 loses product proof.
