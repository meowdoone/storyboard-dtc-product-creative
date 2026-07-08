# DTC Model / Human Presence Library

## Purpose

`model_ref` decides whether a human, hand, body crop, founder, expert, or no-human strategy enters the storyboard.

Human presence is optional. It must serve product proof.

## Schema

```yaml
model_ref:
  id:
  best_for:
  presence_type:
  role:
  visibility:
  wardrobe:
  hands:
  face:
  body_language:
  continuity_lock:
  when_to_use:
  when_not_to_use:
  risk:
```

## Model Entries

| id | best_for | presence_type | role | visibility | wardrobe | hands | face | body_language | continuity_lock | when_to_use | when_not_to_use | risk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| no-human-product-macro | detail, structure, material, packaging strong enough | no-human | none | product only | none | none | none | none | product, light, background continuous | product explains value alone | human use is required | lacks use context |
| hand-only | most SKU demos, unbox, use, touch, size | partial-human | user hands | hands only | neutral sleeves if visible | clean natural hands, consistent tone/nails | not visible | precise, product-first | same hand type, skin tone, action direction | action proof needed without identity | identity/emotion/voice trust needed | hands hide product |
| ugc-creator | real use, explanation, trust | human | creator / everyday user | face optional, upper body or hands | simple casual, non-branded | natural demo gestures | friendly but not over-modeled | direct, practical | same person, outfit, scene | viewer needs to see real user | product details more important | face steals product |
| founder | brand reason, maker logic, design rationale | human | founder / maker | upper body + product | simple credible wardrobe | holding/pointing to product | calm credible | explains product, not performing | product always in frame | real brand/founder context exists | no founder material | empty brand film |
| shopper | choice, comparison, trial, buying judgement | human / partial-human | buyer deciding | hands, torso, over-shoulder | everyday neutral | compares, picks, checks | usually not needed | evaluating | action or gaze around product choice | options/fit/color/size concern exists | no buying decision scene | generic shopping |
| expert | technical, care, tool, functional products | human | expert user | hands / upper body | category-appropriate, no fake credential | careful demonstration | optional | precise and calm | no fake certification, product visible | professional action is evidenced | no expert context | fake expert feel |
| couple | gift, home, shared context | human group | two users | hands / partial bodies | coordinated neutral | passing, unboxing, using together | optional | restrained, product-focused | same two people across panels | gift/shared use matters | single user proves enough | emotion steals product |
| parent | family, child-related, caregiver products | human | parent / caregiver | hands / partial body | home casual | careful handling | optional | protective, practical | no unsupported safety/effect claims | evidence supports family use | product unrelated to family | invented safety claim |
| athlete | sport, outdoor, wearable, gym goods | human | active user | partial body / hands / gear use | sport neutral | grip, wear, pack, adjust | not needed | active but controlled | product visible, not buried by movement | real sport/outdoor use | product cannot support sport context | performance exaggeration |
| office-worker | office, desk, digital, productivity tool | human / partial-human | office user | hands, torso, over-desk | neutral workwear | type, plug, organize, place | not needed | focused | desk, hands, device relationship stable | product enters work flow | product unrelated to office | generic office mood |
| home-user | home, daily use, storage, cleaning, household | human / partial-human | everyday home user | hands / partial body | casual neutral | use, place, clean, open | optional | natural | same home scene and light | household routine matters | professional/outdoor scene fits better | lifestyle without proof |

## Selection Rules

- Prefer `no-human-product-macro` or `hand-only` when product proof does not require identity.
- Use faces only when identity or trust is needed and evidence supports it.
- For custom apparel, prefer faceless torso or cropped wearer unless the user provides model direction.
- Model strategy must not steal attention from product or hide panel 3 proof.
