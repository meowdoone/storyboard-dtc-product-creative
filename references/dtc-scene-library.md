# DTC Scene Library

## Purpose

`scene_ref` decides where the product can be proven. The scene is not decoration.

## Schema

```yaml
scene_ref:
  id:
  best_for:
  product_fit:
  location:
  surface:
  lighting:
  props_allowed:
  props_forbidden:
  human_presence:
  camera_space:
  proof_supported:
  production_risk:
  horizontal_16_9_notes:
```

## Scene Entries

| id | best_for | product_fit | location | surface | lighting | props_allowed | props_forbidden | human_presence | camera_space | proof_supported | production_risk | horizontal_16_9_notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| studio-tabletop | generic SKU, packaging, accessories, custom products, detail proof | product can sit on a table for inspection | neutral indoor tabletop | matte / neutral tabletop | soft daylight or soft studio daylight | packaging, info card, hands, minimal neutral props | decorative clutter, fake UI, fake review cards | hand-only or no-human | top-down, 45-degree, macro | material, size, packaging, structure, options | can feel too studio | keep horizontal negative space; do not crop product |
| bathroom-counter | care, beauty, personal care, fragrance, wash products | product naturally appears near counter/mirror | bathroom counter | stone / ceramic counter | soft morning light | towel, mirror edge, water drops, basic routine objects | too many skincare props, fake skin result | hand-only / partial body | counter-level, mirror-adjacent, macro | texture, use, routine, packaging | can get cluttered | clean horizontal counter, product centered |
| kitchen-prep | food, drink, kitchen tools, containers, cleaning | product participates in prep/pour/open/clean action | kitchen counter | wood / stone / stainless counter | daylight kitchen | ingredients, cup, bowl, cloth, hands | decorative food styling, unsupported effect | hand-only / home user | top-down, side close-up, tracking | capacity, pour, texture, cleaning, process | props can steal focus | props serve product action only |
| desk-setup | office, digital, accessories, stationery, tools | product enters work desk or device context | desk setup | desk mat / wood desk | window light / practical desk lamp | laptop edge, notebook, cable, pen | complex device wall, RGB, fake app UI | hand-only / office worker | over-desk, tabletop tracking, rack focus | fit, size, organization, connection | generic office mood | product on main desk axis |
| travel-packing | storage, apparel, accessories, travel goods | product enters bag/suitcase/packing action | bed / suitcase / packing table | fabric / suitcase interior | home or hotel daylight | suitcase, clothing edge, passport edge, pouch | travel scenery, irrelevant props | hand-only / traveler | top-down packing, close insert | size, portability, storage, kit | product can be buried | open suitcase horizontally, product centered |
| bedside-routine | sleep, fragrance, lamps, home items, care, reading | product participates in morning/night routine | bedside table | wood / fabric / nightstand | soft warm practical light | book, cup, bedding edge, lamp | over-emotional people, messy bedding | hand-only / home user | locked-off, slow push-in, rack focus | routine fit, touch, switch, placement | can become mood only | preserve layers, keep product away from edge |
| gym-locker | sports goods, drink, towel, bags, support gear, wearables | product is used before/after activity | gym locker / bench | bench / locker shelf | clean overhead gym light | water bottle, towel, shoe edge | exaggerated performance action | athlete / hand-only | handheld follow, low angle, product close-up | portability, wearing, durability, identity | person can steal product | product stays in hand/action center |
| car-interior | car accessories, portable devices, storage, fragrance | product appears in console, seat, cup holder, trunk | car interior | dashboard / seat / console | window daylight | real car structure | fake navigation UI, dangerous driving action | hand-only / driver partial | over-shoulder, close insert, locked-off | fit, size, fixed placement, portability | narrow/dark space | keep car context lines in 16:9 |
| gifting-table | gifts, custom products, nice packaging | product is opened, placed, passed, personalized | tabletop / wrapping surface | paper / table / fabric | soft daylight | wrapping paper, ribbon, card, hands | fake brand card, fake greeting text | hand-only / couple / shopper | top-down, macro, hero reveal | packaging, custom, gift choice | decoration can dominate | product and packaging unfold horizontally |
| unboxing-table | kits, packaging, accessories, multi-part products | product is removed from package and parts shown | clean table | matte table | soft daylight | box, insert, manual, hands | nonexistent accessories | hand-only | top-down, 45-degree, tabletop tracking | packaging, parts, completeness | invented parts | arrange parts horizontally without covering main product |
| outdoor-use | outdoor, sport, pet, portable, worn products | product naturally participates in outdoor action | park / trail / street / outdoor table | ground / bench / hand-held | natural daylight | minimal scene cues | travel spectacle, unsupported performance | user / athlete / hand-only | handheld follow, medium close-up, product insert | use relation, portability, scene identity | background can steal focus | blur background, product close to camera |
| no-human-product-macro | product detail strong enough alone | product can prove through material/structure/package | neutral macro setup | matte / controlled surface | soft studio daylight | none or very minimal | human, complex props, fake UI | no-human | macro, slow push-in, orbit | material, structure, craft, packaging | lacks use context | vary 5 camera distances to keep rhythm |

## Scene Lock

After selecting a scene, five panels must preserve:

- same space,
- same surface family,
- same light direction,
- same prop system,
- same product scale logic.
