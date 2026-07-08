# DTC Creative Type Library

## Purpose

`creative_type` is the main DTC creative logic selected by `DTC Creative Director`.

Choose exactly one main `creative_type`. Do not blend multiple main types unless one is clearly secondary in the Reference Pack.

## Schema

```yaml
creative_type:
  id:
  label:
  best_for:
  buyer_tension:
  required_product_evidence:
  visual_structure:
  hook_logic:
  proof_logic:
  CTA_logic:
  risk:
  when_not_to_use:
```

## Creative Types

| id | label | best_for | buyer_tension | required_product_evidence | visual_structure | hook_logic | proof_logic | CTA_logic | risk | when_not_to_use |
|---|---|---|---|---|---|---|---|---|---|---|
| problem-solution | Problem Solution | Product solves a concrete buyer problem | Buyer recognizes a problem but not the right solution | visible use process or result | problem visible -> product enters -> use/proof -> resolved state | make the problem recognizable | product action proves solution | check details or choose version | overstated effect | no visible solution result |
| objection-proof | Objection Proof | Quality, size, fit, setup, authenticity concerns | Buyer wants to buy but is not confident | material, structure, size, handling, comparison | objection shown -> product detail -> proof action -> confidence frame | name the doubt | detail or action removes doubt | confirm spec/material/fit | invented competitor flaw | no proof asset |
| feature-to-benefit | Feature To Benefit | Clear function needs benefit translation | Buyer sees feature but not why it matters | feature entrance, structure, use action | feature close-up -> use moment -> benefit visible -> hero frame | open on concrete feature | connect feature to user benefit | see function details | feature-only without benefit | feature is not visible |
| mechanism-reveal | Mechanism Reveal | Value comes from mechanism, material, craft, setup | Buyer asks why it works | mechanism, material, part, operation detail | curiosity detail -> mechanism reveal -> macro proof -> use result | real detail creates curiosity | close-up, handling, or part relationship | view details/specs | fictional teardown | no visible mechanism |
| comparison | Comparison | Size, color, version, old method, option choice | Buyer is deciding between alternatives | real or neutral comparison basis | option/old way -> product difference -> side-by-side proof -> decision frame | show choice conflict | visual difference proves choice | choose option/version | fake competitor claims | no fair comparison basis |
| routine-integration | Routine Integration | Product enters daily process | Buyer asks if it fits real life | natural use setting and action | routine start -> product enters -> action completes -> routine state | familiar moment | process action proves fit | add to routine | generic lifestyle | product does not depend on routine |
| customization-choice | Customization Choice | Custom, color, size, kit, modular, configurable products | Buyer asks if it can match their need | option/configuration/customization entrance | choice problem -> options shown -> configuration action -> final selected state | reveal the choice | option change proves configurability | choose/upload/configure | fake artwork/options | no real option/config |
| trust-proof | Trust Proof | Quality, authenticity, material, durability, packaging | Buyer fears a bad purchase | material, structure, packaging, spec, review, or detail evidence | doubt cue -> detail proof -> handling proof -> confident end frame | enter trusted detail | macro/touch/shadow/detail proof | check details/reviews | fake certification/review | no credible evidence |
| sensory-proof | Sensory Proof | Texture, touch, shine, sound, fabric, food, liquid | Buyer needs to feel quality | visible material or texture | macro sensory hook -> touch/action -> detail proof -> memory frame | close detail hook | hand/light/macro makes texture visible | check material/detail | AI plastic feel | no sensory attribute |
| product-macro | Product Macro | Product appearance, structure, packaging, craft is strong | Buyer needs inspection | readable product detail | hero macro -> detail rotation -> proof detail -> clean product end frame | product detail first | macro/rotation proves detail | view product details | lacks use context | product needs human use to understand |
| ugc-demo | UGC Demo | Human explanation or use demo is needed | Buyer wants to see real use | product can be naturally demonstrated | creator/hand hook -> demo -> proof -> personal CTA | human or hand enters fast | action proves use method | try/check link | person steals product | product details matter more |
| founder-demo | Founder Demo | Brand reason, maker logic, design rationale | Buyer asks why product exists | product and explanation can be same frame | founder reason -> design detail -> use proof -> trust CTA | one design reason | product detail supports explanation | learn brand/details | empty brand story | no brand/founder context |

## Selection Rules

- Select by buyer tension and available proof, not by desired style.
- `customization-choice` requires real options, configuration, or customization evidence.
- `founder-demo` requires brand/founder context; do not invent it.
- `comparison` requires a fair neutral comparison or user-provided basis.
- `sensory-proof` and `product-macro` need strong visual detail.
- If the product is already highly constrained by Product Truth Card, choose the lowest-risk creative type that still gives a reason to watch.

## Supporting Menus

Hook tactics:

- visual interruption
- problem recognition
- direct question
- specific claim
- curiosity gap
- before-after contrast
- micro demo
- detail macro
- choice reveal
- mistake callout
- comparison open
- routine disruption

Proof mechanics:

- material macro
- hand pressure / touch
- use sequence
- scale / fit check
- compatibility check
- configuration reveal
- package contents
- visible result
- side-by-side comparison
- expert handling
- routine completion
- social proof frame

CTA patterns:

- check the details
- choose your option
- upload your design
- shop the set
- confirm your fit
- see how it works
- get the routine
- try it today
- build your kit
- compare the options
