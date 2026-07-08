# Storyboard DTC Product Creative Skill

SKU 级 DTC 商品创意导演 skill。输入一个 Amazon / Shopify / TikTok Shop 链接、ASIN、商品图、截图或 SKU brief，先锁商品真相，再由 DTC Creative Director 形成 Reference Pack，再由 Brand Film Look Director 形成品牌片视觉规则，最后由 Storyboard Design Expert 输出横屏 5 格故事版图片和英文视频脚本。

## Output

默认最终回复只输出三段：

```markdown
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` 嵌入或链接 5-panel contact sheet，每个 panel 是 16:9 横屏，并且每格都是 video-ready keyframe。

## Workflow

```text
Product Truth
-> Live Ad Reference Collection
-> Ad Reference Decomposition
-> DTC Creative Director
-> DTC Creative Reference Pack
-> Brand Film Look Director
-> Brand Film Look Pack
-> Storyboard Design Expert
-> Horizontal 5-panel image
-> English video script with Camera / Motion
-> Local validation
```

## Execution Contract

这个 skill 运行时直接产出工作记录和交付物，不只给建议：

- 建立 `Product Truth Card`。
- 记录 `source_records.json`。
- 拆解可用参考为 `ad_reference`。
- 形成 `DTC Creative Reference Pack`。
- 形成 `Brand Film Look Pack`。
- 生成或组装 `contact_sheet.png` 与 `panels/*.png`。
- 保存 `run.json`。
- 运行 `scripts/validate_storyboard.py`。
- 如果当前环境缺少抓取、生图、文件写入或图片嵌入能力，在 `run.json` 记录 blocked artifact 和原因。

## Internal Roles

### DTC Creative Director

不负责出图。它负责在出图前做创意选择：

```text
creative_type
scene_ref
motion_chain
model_ref
camera_plan
brand_film_mode
script_pattern
picture_fragment_logic
```

输出物是 `DTC Creative Reference Pack`。

每个 selected `creative_type`、`scene_ref`、`motion_ref`、`model_ref`、`camera_ref` 都必须带中文 `description`，说明这个选择在故事版里干什么。

### Brand Film Look Director

不重新选择创意方向。它把 `brand_film_mode` 翻译成：

- 同一拍摄世界锁；
- 镜头、焦距感、机位和运动规则；
- 光线、阴影、材质和接触感规则；
- shot function map；
- signature shot；
- end-frame rule；
- failure rules。

输出物是 `Brand Film Look Pack`。它不能在最终输出里暴露导演名字、电影名或 "like this director" 语言。

### Storyboard Design Expert

不重新选择创意方向。它只把 `DTC Creative Reference Pack` 和 `Brand Film Look Pack` 转成：

- 一张横屏 5 格 16:9 storyboard/contact sheet 图片；
- 15 秒或 30 秒英文视频脚本；
- 本地验证记录。

## Reference Pack 简版

完整 schema 在 `references/dtc-director-reference-pack-schema.md`。

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

没有这个 pack，不进入故事版图片生成。

## Brand Film Look Pack 简版

完整 schema 在 `references/brand-film-look-director.md`。

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

没有这个 pack，不进入 Storyboard Design Expert。

## Key References

- `SKILL.md`：入口流程和硬门控。
- `references/dtc-director-reference-pack-schema.md`：DTC Creative Reference Pack schema。
- `references/storyboard-video-keyframe-rules.md`：横屏 5 格 video-ready keyframe 规则。
- `references/dtc-creative-pattern-library.md`：creative_type 库。
- `references/dtc-scene-library.md`：scene_ref 库。
- `references/dtc-motion-library.md`：motion_chain 库。
- `references/dtc-model-library.md`：model_ref 库。
- `references/camera-language-library.md`：camera_plan 库。
- `references/brand-film-mode-library.md`：brand_film_mode 内部品牌片语言库。
- `references/brand-film-look-director.md`：把 brand_film_mode 翻译成具体镜头、光线、材质和节奏规则。
- `references/cinematic-grammar-rules.md`：禁止空泛电影感词，要求可执行的镜头和光线语法。
- `references/brand-film-storyboard-qa.md`：品牌片故事版质量检查和拒绝条件。
- `references/category-adapters.md`：类目适配和 custom apparel / personalized product 锁定规则。
- `references/source-compliance-policy.md`：公开、授权、用户提供来源的采集边界。
- `references/live-crawl-strategy.md`：实时参考采集和 fallback 记录。
- `references/ad-reference-analysis-schema.md`：广告参考拆解结构。
- `scripts/validate_storyboard.py`：本地交付验证。

## Script Rule

第三段脚本固定包含：

```markdown
| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
```

`Camera / Motion` 必须来自 `camera_selection` 和 `motion_selection`。`Reference Logic` 必须说明借鉴了什么结构、场景、动作、镜头或剧本逻辑，但不写具体品牌名。

## Local Artifacts

最终回复仍然只给三段内容；本地运行时保存：

```text
run.json
source_records.json
contact_sheet.png
panels/*.png
```

`run.json` 至少需要：

```json
{
  "source_url": "...",
  "locked_terms": ["..."],
  "creative_type": "...",
  "scene_ref": "...",
  "motion_chain": ["..."],
  "model_ref": "...",
  "camera_plan": {
    "opening_camera": "...",
    "context_camera": "...",
    "proof_camera": "...",
    "use_camera": "...",
    "end_frame_camera": "..."
  },
  "ref_descriptions": {
    "creative_type": "...",
    "scene_ref": "...",
    "motion_refs": ["..."],
    "model_ref": "...",
    "camera_refs": {
      "opening_camera": "...",
      "context_camera": "...",
      "proof_camera": "...",
      "use_camera": "...",
      "end_frame_camera": "..."
    }
  },
  "brand_film_mode": {
    "mode_id": "...",
    "visual_signature": "...",
    "key_technique": "...",
    "product_translation": "...",
    "camera_translation": "...",
    "lighting_translation": "...",
    "risk": "..."
  },
  "brand_film_look_pack": {
    "brand_world_lock": "...",
    "cinematic_grammar": "...",
    "shot_function_map": "...",
    "material_and_light_rules": "...",
    "signature_shot": "...",
    "end_frame_rule": "..."
  },
  "end_frame": {
    "product_position": "...",
    "logo_or_label_visibility": "...",
    "proof_memory": "...",
    "CTA_intent": "...",
    "camera_state": "...",
    "lighting_state": "..."
  },
  "contact_sheet": "...",
  "panel_count": 5,
  "panel_aspect_ratio": "16:9"
}
```

## Validation

```bash
python3 scripts/validate_storyboard.py /path/to/output_dir
```

验证内容：

- `run.json`、`source_records.json` 都存在且是有效 JSON。
- `run.json` 包含 `source_url` 和 `locked_terms`。
- `brand_film_mode` 存在，且不使用导演名字作为对外语言。
- `brand_film_look_pack` 存在，且包含品牌世界锁、电影语法、shot function map、材质光线规则、signature shot 和 end-frame rule。
- `end_frame` 包含 product position、logo/label visibility、proof memory、CTA intent、camera state、lighting state。
- contact sheet 存在且可读取。
- `panels/` 中 5 张 panel 均为 16:9。

## Boundaries

- 商品真相高于创意参考。
- DTC Creative Director 可以借鉴广告结构，不能替代 SKU 事实。
- Brand Film Look Director 只能翻译视觉语言，不能重选创意方向。
- Storyboard Design Expert 不能重新发明创意方向。
- 不固定 1-5 格剧情角色；每格任务来自 `picture_fragment_logic`。
- 公共来源默认只保存 URL、摘要、允许截图/关键帧和结构化拆解；原视频、完整广告文件、品牌资产只允许用于用户提供或授权来源。
- 定制类商品必须锁定同一个 Design Asset；没有用户真实设计时只能用中性占位，不编造假 logo。
