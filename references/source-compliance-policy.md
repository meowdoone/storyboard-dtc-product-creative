# 来源采集与素材使用策略

## 目标

明确实时采集、授权采集和用户提供素材在 skill 中如何使用。

## 可使用来源

```yaml
source_types:
  public:
    - public ad libraries
    - search results
    - public brand sites
    - public social pages
    - public landing pages
  authorized:
    - user logged-in accounts
    - user-owned ad accounts
    - user-paid creative libraries
    - private links provided by user
    - user-owned asset libraries
  user_provided:
    - uploaded videos
    - screenshots
    - downloaded ad files
    - scripts
    - brand references
    - competitor lists
```

## 可复制、采集并保存的内容

- 广告原片
- 原视频文件
- 视频片段
- 截图
- 缩略图
- 关键帧
- 脚本
- 字幕
- 口播
- 品牌资产
- landing page 画面
- 画面片段
- 镜头运动
- 人物动作
- 商品动作
- hook 文字
- CTA 文案
- 产品展示片段
- source_url

## 使用方式

采集内容进入 `DTC Creative Reference Pack`，用于：

- 参考追溯
- 广告拆解
- 创意结构提取
- 场景库匹配
- 运动库匹配
- 模特库匹配
- 镜头库匹配
- 剧本结构参考
- 横屏故事版图片生成
- 视频 demo 脚本生成

## 私域和登录来源

用户授权或用户账号可访问的私域内容可以作为 `authorized` 来源采集。

包括：

- 用户登录状态下的广告库
- 用户自己的广告账号后台
- 用户购买的创意库
- 用户自己的素材库
- 用户提供的私域参考页面
- 用户提供的私密链接

这类来源必须记录 `source_type: authorized`，并保留 `source_url` 或本地素材路径。

## 记录要求

每条参考必须记录：

```yaml
source_record:
  source_url:
  source_type:
  captured_assets:
  local_paths:
  capture_time:
  notes:
```

## 平台阻挡降级

平台阻挡、登录失效、页面不可访问或素材无法下载时，按顺序降级：

```text
平台页面
-> 搜索结果摘要
-> 手动链接
-> 用户提供参考广告
-> 用户上传素材
-> 内置参考库
```

降级后仍然要记录来源：

```yaml
fallback_record:
  attempted_source_url:
  fallback_type:
  fallback_source_url:
  user_provided_asset_path:
  reason:
```
