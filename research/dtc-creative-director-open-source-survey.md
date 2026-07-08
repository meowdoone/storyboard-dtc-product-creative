# DTC Creative Director Open Source Survey

Date: 2026-07-08

## Conclusion

No single open-source project already provides the full target system:

```text
live global DTC ad reference collection
-> creative director taxonomy
-> scene library
-> motion library
-> model / human presence library
-> storyboard image expert
-> video-demo-ready motion script
```

The practical direction is to keep this repo as the SKU-truth-first DTC storyboard skill, then add a live reference director layer in front of the storyboard expert.

## Sources Reviewed

### Ethanxwang/tvc-director

Source: https://github.com/Ethanxwang/tvc-director

Useful pattern:

- Treats the agent as a TVC advertising creative director.
- Uses phases such as creative brief, proposal, visual direction, pre-production, storyboard and shooting.
- Includes casting, product look, location scouting, character references, scene references, multi-grid storyboard and video prompts.

Adoption:

- Borrow the director workflow and pre-production asset planning.
- Adapt it to DTC SKU truth, real product evidence, live reference collection and horizontal 5-panel storyboard image output.

### lujiaheng-artpivot/openclaw-ecommerce-ad-skills

Source: https://github.com/lujiaheng-artpivot/openclaw-ecommerce-ad-skills

Useful pattern:

- Separates ecommerce growth ads, TVC craft, story video, Seedance video and QC.
- Has agent roles such as creative director, TVC creative director, manga director and video QC.
- Recommends workflow composition across ad analytics, storyboards, sound design and video generation.

Adoption:

- Use the role split: DTC creative intelligence director upstream, storyboard design expert downstream.
- Keep QC as the final image and video-demo readiness gate.

### AdsTurbo/adsturbo-creative-mcp

Source: https://github.com/AdsTurbo/adsturbo-creative-mcp

Useful pattern:

- Local MCP / CLI planning layer for video ad briefs, hooks, UGC scripts, storyboards, variation plans, reviews and prompts.
- Storyboard schema includes platform, duration, aspectRatio, scenes, timing, visual, caption, voiceover, purpose, shotType and productionNotes.

Adoption:

- Borrow the structured storyboard object.
- Add fields this repo needs: source_pattern, source_url, scene_ref, motion_ref, model_ref, camera_ref, product_truth_lock, image_panel_task, picture_fragment_logic and video_demo_motion.

### ComposioHQ/awesome-claude-skills competitive-ads-extractor

Source: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/competitive-ads-extractor/SKILL.md

Useful pattern:

- Extracts competitor ads from ad libraries.
- Captures screenshots.
- Analyzes problems, use cases, value props, themes, formats and successful creative patterns.

Adoption:

- Use as a pattern for the DTC Ad Reference Collector.
- Extend analysis beyond copy into scene, human presence, action, camera, proof mechanic, visual fragment, CTA and product role.

### facebookresearch/Ad-Library-API-Script-Repository

Source: https://github.com/facebookresearch/Ad-Library-API-Script-Repository

Useful pattern:

- Official example scripts for Meta Ad Library API.
- Useful where API access fits the source being collected.

Adoption:

- Keep as one possible `public` source connector pattern.
- Still support web search, manual links, user-authorized sources and user-provided assets as parallel collection paths.

### FlowExtractAPI/tiktok-ad-library-scraper and Facebook Ads Library scraper repos

Sources:

- https://github.com/FlowExtractAPI/tiktok-ad-library-scraper
- https://github.com/domini-67/facebook-ads-library-scraper

Useful pattern:

- Show the shape of scraper outputs: advertiser, creative type, dates, audience, media assets, targeting metadata and CTA metadata.

Adoption:

- Use the output shape as inspiration for `ad_reference`.
- Capture the parts that matter to storyboard generation: source_url, original assets, hook, scene, model, motion, proof mechanic, script pattern and CTA.

### Motion Creative Strategy Library

Source: https://motionapp.com/library/

Useful pattern:

- Organizes paid-social creative by brand pages, visual ad formats, audience personas, frameworks and hook tactics.

Adoption:

- Build local libraries with similar buckets:
  - DTC visual formats
  - buyer states
  - hook tactics
  - proof mechanics
  - scene systems
  - motion systems
  - model systems
  - camera systems

## Adopted Architecture

```text
product truth lock
-> live crawl plan
-> public / authorized / user_provided reference collection
-> ad_reference decomposition
-> DTC Creative Reference Pack
-> content strategy
-> horizontal 5-panel storyboard image
-> English video-demo script
```

## Added Reference Files

```text
references/live-crawl-strategy.md
references/ad-reference-analysis-schema.md
references/dtc-creative-pattern-library.md
references/dtc-scene-library.md
references/dtc-motion-library.md
references/dtc-model-library.md
references/camera-language-library.md
references/source-compliance-policy.md
```
