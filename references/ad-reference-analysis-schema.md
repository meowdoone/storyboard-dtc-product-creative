# 广告参考拆解 Schema

## 目标

把实时采集、授权访问或用户提供的广告参考，拆成可被故事版专家调用的结构。

## Schema

```yaml
ad_reference:
  source_url:
  source_type: public | authorized | user_provided | local_file
  local_asset_path:
  platform:
  brand:
  category:
  product_type:
  region:
  language:
  format:
  aspect_ratio:
  duration:

  original_assets:
    video:
    screenshots:
    keyframes:
    transcript:
    subtitles:
    brand_assets:
    landing_page:

  hook:
    first_3_seconds:
    hook_type:
    visual_interruption:
    opening_frame:
    opening_line:

  scene:
    location:
    surface:
    lighting:
    props:
    realism_level:
    scene_transition:

  model:
    presence_type:
    role:
    wardrobe:
    hand_or_body_visibility:
    expression:
    continuity_notes:

  motion:
    human_action:
    product_action:
    camera_motion:
    transition:
    pacing:
    reusable_clip_logic:

  proof:
    proof_mechanic:
    product_detail_shown:
    objection_answered:
    visual_evidence:

  script:
    spoken_line_pattern:
    subtitle_pattern:
    CTA:
    pacing_structure:

  reusable_pattern:
    what_to_borrow:
    picture_fragment_logic:
    scene_logic:
    action_logic:
    camera_logic:
    script_logic:
    what_not_to_copy:
```

## 拆解重点

- 结构：广告从 hook 到 CTA 的组织方式。
- 场景：空间、表面、光线、道具和生活方式语境。
- 模特：人物角色、手部、身体、服装、姿态。
- 动作：人物动作、商品动作、手部动作。
- 镜头：景别、运动、焦点、转场。
- 节奏：每个片段的时长和信息密度。
- 画面片段：可转译到当前 SKU 的画面逻辑。
- 剧本：口播、字幕、CTA 的结构。

## 输出用途

每条 `ad_reference` 只能作为内部导演素材，用于生成：

- `DTC Creative Reference Pack`
- 横屏故事版图片提示
- 视频 demo 脚本

