# Storyboard DTC Product Creative Skill

把真实商品转成可做视频 demo 的 DTC 商品创意输出：

```text
商品证据
-> 实时 DTC 广告参考采集
-> 广告结构拆解
-> DTC Creative Reference Pack
-> 横屏 5 格故事版图片
-> 15 秒或 30 秒英文视频脚本
```

这个 skill 不是泛广告文案工具，也不是只做漂亮图。它面向 SKU 级内容工作流：给一个 Amazon / Shopify / TikTok Shop 商品链接、商品图、截图、ASIN、SKU brief 或短描述，先锁定商品真相，再实时收集和拆解 DTC 广告参考，最后输出可继续做横屏视频 demo 的故事版图片和英文脚本。

## 输出格式

默认只输出三段：

```markdown
## 1. 产品图

## 2. 故事版

## 3. 15 秒或者 30 秒视频脚本文字
```

`## 2. 故事版` 必须是真实图片：一张横屏 5 格 16:9 storyboard / contact-sheet 图。不能用文字分镜、表格、shot list 或 prompt 替代图片。

## 内部角色

```text
Live DTC Creative Intelligence Director
Storyboard Design Expert
```

`Live DTC Creative Intelligence Director` 负责：

- 分析商品和买家决策问题
- 建立实时采集计划
- 采集公开、授权或用户提供的 DTC 广告参考
- 保存 `source_url` 或本地素材路径
- 拆解结构、场景、人物、动作、镜头、节奏、画面片段和剧本
- 形成 `DTC Creative Reference Pack`

`Storyboard Design Expert` 负责：

- 选择场景库、模特库、运动库、镜头库
- 生成横屏 5 格连续故事版图片
- 保持同一商品、同一拍摄世界、同一光线和真实接触阴影
- 输出可做视频 demo 的英文脚本

## 实时采集来源

支持三类来源：

```text
public
authorized
user_provided
```

`public` 包括公开可访问的广告库、搜索结果、品牌官网、公开 landing page、公开社媒广告页、YouTube、广告案例库等。

`authorized` 包括用户登录状态下可访问的广告库、用户自己的广告账号后台、用户购买的创意库、用户自己的素材库、用户提供的私域参考页面。

`user_provided` 包括用户上传或直接提供的广告视频、截图、链接、品牌案例、竞品清单、脚本、参考图或已下载素材。

可复制、采集并保存到 reference pack 的内容：

- 广告原片 / 视频文件
- 视频片段
- 截图 / 缩略图
- 关键画面帧
- 脚本文字 / 口播 / 字幕
- 品牌资产
- landing page 画面
- hook 文字
- CTA 文案
- 评论或社媒上下文
- 产品展示片段
- 模特 / 人物画面
- 动作和镜头片段
- `source_url`

平台阻挡时降级：

```text
平台页面
-> 搜索结果摘要
-> 手动链接
-> 用户给参考广告
-> 用户上传素材
-> 内置参考库
```

## 9 步流程

```text
1. 证据锁定
2. 实时广告参考采集
3. 广告拆解
4. 内容属性卡
5. Reference Pack 选择
6. 内容策略选择
7. 横屏故事版图片生成
8. 视频 demo 英文脚本
9. 交付前 QA
```

核心优先级：

```text
商品真相
> 内容属性
> 实时广告参考
> 创意参考包
> 买家决策逻辑
> DTC 创意角度
> 场景 / 模特 / 运动 / 镜头库
> 视觉风格
> 脚本文字
```

如果创意和商品真相冲突，删掉创意，不改商品。

## Reference Pack

故事版生成前必须形成内部 `DTC Creative Reference Pack`：

```yaml
dtc_creative_reference_pack:
  product_truth_lock:
  selected_ad_references:
  selected_creative_patterns:
  selected_scene_refs:
  selected_model_refs:
  selected_motion_refs:
  selected_camera_refs:
  selected_script_patterns:
  picture_fragment_refs:
  source_urls:
  rejected_references:
  adaptation_reason:
```

Reference Pack 决定故事版如何拍。它回答：

- 借鉴哪些广告结构？
- 当前 SKU 使用哪个场景系统？
- 是否需要真人、手部、专家、创始人、UGC creator 或无人物？
- 商品和人物分别怎么动？
- 镜头如何移动？
- 哪些画面片段适合横屏 5 格故事版？
- 哪个剧本结构适合 15 秒或 30 秒 demo？

## 内置库

实时参考优先，内置库兜底：

- `references/live-crawl-strategy.md`
- `references/ad-reference-analysis-schema.md`
- `references/dtc-creative-pattern-library.md`
- `references/dtc-scene-library.md`
- `references/dtc-motion-library.md`
- `references/dtc-model-library.md`
- `references/camera-language-library.md`
- `references/source-compliance-policy.md`

## 故事版图片要求

故事版图片必须满足：

- 最终图片是横屏，不是竖屏或方图
- 5 个 panel 都是横屏 16:9
- 默认横向单行排列
- 每一格有内容任务
- 每一格保持商品真相
- 每一格像同一次真实拍摄里的连续镜头
- 每一格体现已选场景、人物、动作、镜头或画面片段参考
- 至少两格证明商品细节
- 至少两格承载内容角度或 creative lens
- 第 5 格增强购买信心

默认故事版方向：

```text
内容属性锁: target_buyer、content_angle、hook_type、core_message、proof_asset
创意参考锁: selected_ad_references、scene_ref、model_ref、motion_ref、camera_ref、script_pattern
创意大片方向: 一句 DTC Creative Film Treatment
同一拍摄世界锁: Shooting World Lock
5 格 16:9 横屏连续关键帧图片: 实际生成图片
```

## 脚本要求

默认 15 秒；用户要求 30 秒时才用 30 秒。

脚本必须是英文，并包含：

- `Camera / Motion`
- `Reference Logic`
- 屏幕字幕
- 旁白 / 口播
- 与故事版一致的画面任务

15 秒脚本格式：

```markdown
| 时间 | 画面 | Camera / Motion | 屏幕字幕 | 旁白 / 口播 | Reference Logic |
|---|---|---|---|---|---|
| 0-2s | ... | ... | ... | "..." | ... |
| 2-5s | ... | ... | ... | "..." | ... |
| 5-8s | ... | ... | ... | "..." | ... |
| 8-11s | ... | ... | ... | "..." | ... |
| 11-15s | ... | ... | ... | "..." | ... |
```

## 中文说明

完整中文介绍见：

```text
介绍.md
```
