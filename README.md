# Storyboard DTC Product Creative Skill

SKU 级 DTC 商品创意导演 skill。输入一个 Amazon / Shopify / TikTok Shop 链接、ASIN、商品图、截图或 SKU brief，先锁商品真相，再由 DTC Creative Director 形成 Reference Pack，最后由 Storyboard Design Expert 输出横屏 5 格故事版图片和英文视频脚本。

## Output

默认最终回复只输出三段：

```markdown
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` 必须包含真实图片：一张横向单行 5-panel contact sheet，每个 panel 是 16:9 横屏，并且每格都是 video-ready keyframe。

## Workflow

```text
Product Truth
-> Live Ad Reference Collection
-> Ad Reference Decomposition
-> DTC Creative Director
-> DTC Creative Reference Pack
-> Storyboard Design Expert
-> Horizontal 5-panel image
-> English video script with Camera / Motion
-> Local validation
```

## Internal Roles

### DTC Creative Director

不负责出图。它负责在出图前做创意选择：

```text
creative_type
scene_ref
motion_chain
model_ref
camera_plan
script_pattern
picture_fragment_logic
```

输出物是 `DTC Creative Reference Pack`。

### Storyboard Design Expert

不重新选择创意方向。它只把 `DTC Creative Reference Pack` 转成：

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
  script_pattern:
  picture_fragment_logic:
  rejected_references:
  adaptation_reason:
```

没有这个 pack，不进入故事版图片生成。

## Key References

- `SKILL.md`：入口流程和硬门控。
- `references/dtc-director-reference-pack-schema.md`：DTC Creative Reference Pack schema。
- `references/storyboard-video-keyframe-rules.md`：横屏 5 格 video-ready keyframe 规则。
- `references/dtc-creative-pattern-library.md`：creative_type 库。
- `references/dtc-scene-library.md`：scene_ref 库。
- `references/dtc-motion-library.md`：motion_chain 库。
- `references/dtc-model-library.md`：model_ref 库。
- `references/camera-language-library.md`：camera_plan 库。
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

最终回复仍然只给三段内容；本地运行时应保存：

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
  "contact_sheet": "...",
  "contact_sheet_layout": "horizontal_single_row",
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
- contact sheet 是横向单行 5 格图。
- `panels/` 中 5 张 panel 均为 16:9。
- 竖向堆叠 contact sheet 会失败。

## Boundaries

- 商品真相高于创意参考。
- DTC Creative Director 可以借鉴广告结构，不能替代 SKU 事实。
- Storyboard Design Expert 不能重新发明创意方向。
- Panel 3 必须是最强商品证明。
- 公共来源默认只保存 URL、摘要、允许截图/关键帧和结构化拆解；原视频、完整广告文件、品牌资产只允许用于用户提供或授权来源。
- 定制类商品必须锁定同一个 Design Asset；没有用户真实设计时只能用中性占位，不编造假 logo。
