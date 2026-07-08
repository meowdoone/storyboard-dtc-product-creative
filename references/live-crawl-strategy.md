# 实时 DTC 广告参考采集策略

## 目标

给到一个商品后，先分析商品，再实时查找和采集相关 DTC 创意广告参考。

采集结果用于：

- 建立创意方向
- 拆解场景、人物、动作、镜头、节奏、画面片段和剧本
- 形成 `DTC Creative Reference Pack`
- 支撑横屏 5 格故事版图片
- 支撑视频 demo 脚本

## 输入

```yaml
product_input:
  product_url:
  product_images:
  sku_brief:
  category:
  claims:
  buyer_problem:
  product_behavior:
```

## Live Crawl Plan

```yaml
live_crawl_plan:
  product_category:
  product_behavior:
  buyer_problem:
  main_benefit:
  proof_type:
  competitor_keywords:
  adjacent_category_keywords:
  platform_keywords:
  region_keywords:
  source_priority:
```

## 来源类型

### public

公开可访问来源：

- Meta Ad Library
- TikTok Creative Center
- Google Ads Transparency Center
- YouTube
- 品牌官网
- 公开 landing page
- 公开社媒广告页
- 公开广告案例库
- 搜索结果页

### authorized

用户授权或用户账号可访问来源：

- 用户登录状态下的广告库
- 用户购买的创意库
- 用户自己的素材库
- 用户提供的广告账号后台
- 用户提供的私域参考页面
- 用户有权限访问的竞品监控工具

### user_provided

用户直接提供来源：

- 广告视频
- 截图
- 广告链接
- 品牌案例
- 竞品清单
- 已下载素材
- 脚本
- 参考图

## 默认采集字段

```yaml
source_capture:
  source_url:
  source_type:
  platform:
  brand:
  category:
  country_or_region:
  language:
  ad_format:
  aspect_ratio:
  duration:
  video_file:
  screenshots:
  keyframes:
  transcript:
  subtitles:
  brand_assets:
  landing_page_url:
  landing_page_frames:
  hook_text:
  CTA_text:
  product_showing_fragments:
  model_frames:
  human_action_fragments:
  product_action_fragments:
  camera_motion_fragments:
  visual_fragment_notes:
  social_context:
  notes:
```

## 降级策略

平台阻挡或采集失败时，按顺序降级：

```text
平台页面
-> 搜索结果摘要
-> 手动链接
-> 用户提供参考广告
-> 用户上传素材
-> 内置参考库
```

## 完成标准

- 至少尝试 2 类来源。
- 每条有效参考保留 `source_url` 或本地素材路径。
- 每条参考进入 `ad_reference` 拆解。
- 没有有效参考时标记 `reference_sparse`，并使用内置库兜底。
