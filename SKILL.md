---
name: storyboard-dtc-product-creative
description: Use when a user wants a SKU-level DTC product creative storyboard from a product link, Amazon/Shopify/TikTok Shop URL, product image, product screenshot, ecommerce page, ASIN, SKU brief, or short product description. The required output format is exactly product image first, then storyboard, then 15-second or 30-second video script text. Product truth is the hard gate; DTC creative lens is allowed only after product identity, function, material, scale, claims, and use logic are locked.
---

# DTC 商品创意故事版 Skill

## 目标

把一个真实商品转成 DTC 风格的商品主导创意故事版。

默认只输出三段：

```text
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

这个 skill 面向 SKU 级电商创意，不是泛广告文案工具。

优先级顺序：

```text
商品真相
> 买家决策逻辑
> DTC 创意镜头
> 视觉风格
> 脚本文字
```

如果创意和商品真相冲突，删掉创意，不改商品。

## 适用场景

用户提出以下需求时使用：

- DTC 商品创意故事版
- 电商商品创意
- DTC 广告分镜
- 商品主导创意视频
- SKU 级创意方向
- Shopify / Amazon / TikTok Shop 商品创意
- 商品图转故事版
- 商品证明 + 创意角度
- "DTC 创意"
- "商品创意故事版"
- "产品为主，但要有创意"

不用于：

- 没有商品证据的泛品牌 campaign
- 只做 logo
- 纯文案
- 长篇 campaign 策略
- 市场研究报告
- Meta 广告批量生成
- UGC 达人脚本，除非用户明确要求

## 核心规则

默认响应只能包含：

```text
## 1. 产品图
## 2. 故事版
## 3. 15 秒或者 30 秒视频脚本文字
```

不要默认输出 JSON、长分析、negative prompt、平台报告、DTC 理论、竞品分析或额外章节。

第三段脚本必须是英文。表格里的 `屏幕字幕` 和 `旁白 / 口播` 必须是自然英文。

## 商品真相门槛

做任何创意判断前，先在内部锁定商品真相。

必须提取并保持：

- 商品类型
- 形状 / 轮廓
- 颜色
- 材质 / 纹理
- 包装 / 标签 / logo
- 可见部件 / 组件
- 尺寸和比例线索
- 商品如何被使用
- 什么结果是可见的
- 哪些声明是允许的
- 哪些东西绝对不能变

如果没有可靠商品图、商品页或清晰截图，不要生成最终商品故事版。要求用户补商品证据，或者明确标记为 rough concept。

禁止编造：

- 新包装
- 新 logo
- 新功效声明
- 新功能
- 新配件
- 新 before/after 结果
- 证据不支持的新使用场景
- 假认证
- 假评论
- 假 Amazon / Shopify / TikTok UI

## 商品行为适配器

内部先判断商品行为，而不是只按类目套模板。

行为适配器包括：

- 穿戴 / 携带 / 身体接触
- 个性化 / 可配置
- 手动操作 / 组装 / 安装
- 涂抹 / 挤出 / 质地展示
- 连接 / 配对 / 兼容
- 摆放 / 展示 / 收纳
- 食用 / 饮用 / 盛放
- 与人、宠物或主体互动
- 套装 / 组合 / 多部件设置

适配器决定：

- 哪些商品真相必须锁定
- 哪个 buyer event 有证据支持
- 是否需要真实使用关系
- 哪些镜头负责证明商品
- 哪些场景高风险

不要把行为适配分析作为额外输出段落暴露出来。

## DTC 创意判断

锁定商品真相后，再内部选择 DTC 创意方向。

依次判断：

1. `shopper_tension`
   买家现在有什么疑虑、欲望、痛点或决策问题？

2. `reason_to_watch`
   为什么这个内容值得做成短视频 / 故事版，而不是只用静态商品图？

3. `creative_lens`
   哪种 DTC 创意角度能让商品证明更有记忆点？

4. `product_entrance`
   商品如何在第 1 或第 2 格成为明确主角？

5. `visual_device`
   用什么视觉装置组织 5 格画面？

6. `proof_sequence`
   每一格依次证明哪些商品事实？

7. `creative_safety`
   这个创意有没有添加证据不支持的道具、功效、场景、情绪或人物？

这些判断只影响故事版，不作为默认输出章节。

## DTC 创意镜头菜单

选择一个主创意镜头，不要混太多。

允许的 creative lens：

- `proof-first demo`
  商品价值主要来自实物、功能、细节时使用。

- `before-trigger-after`
  有清晰问题、商品介入、可信最终状态时使用。

- `mechanism reveal`
  商品部件、质地、材质、设置方式或操作机制重要时使用。

- `configuration reveal`
  商品支持个性化、调节、定制、选项、套装或模块组合时使用。

- `scale / fit / compatibility proof`
  买家需要确认尺寸、适配、摆放、兼容性或比例时使用。

- `visual metaphor`
  商品利益点可以用简单、安全的视觉隐喻表达时使用。

- `restrained color-world`
  商品颜色、包装色或品牌色能形成有记忆点但仍真实的视觉世界时使用。

- `social proof scene`
  真实使用、共享场景、身份认同或群体语境重要，并且商品证据支持时使用。

- `curiosity gap`
  商品有一个真实可见的功能、设置、结构或结果，能自然制造问题感时使用。

不要使用：

- 会隐藏商品的幻想视觉世界
- 改变商品功能的抽象隐喻
- listing 证据不支持的情绪剧情
- 夸张 transformation
- 假 UI
- 假声明
- 和购买决策无关的装饰道具

## 创意安全门槛

DTC 创意只能在商品真相锁定之后进入。

如果创意会改变以下任何内容，必须拒绝：

- 商品几何形状
- 商品颜色
- 材质
- 包装
- logo / 标签
- 尺寸 / 比例
- 使用方式
- 兼容关系
- 功效声明
- 可见结果
- 买家决策逻辑

商品不是创意里的道具。商品是创意存在的原因。

## 故事版规则

故事版必须：

- 商品主导
- 有 DTC 创意，但必须基于证据
- 有记忆点
- 有商业可用性
- 足够真实，可以成为电商生产素材
- 5 格保持一致
- 只围绕一个清晰 creative lens

默认故事版格式：

```text
创意大片方向: 一句简洁的 DTC Creative Film Treatment
同一拍摄世界锁: 一段紧凑的 Shooting World Lock
5 格 16:9 连续关键帧: 一张 storyboard/contact-sheet 图，包含五个编号 16:9 商品证明创意画面
```

5 格逻辑：

1. 商品进入 / SKU 锚点
2. 买家疑虑 / 场景设置
3. 商品证明 / 机制 / 细节
4. 使用瞬间 / 转变 / payoff
5. 购买信心 / 最终商品主导状态

至少两格必须证明商品细节。

至少两格必须承载 DTC creative lens。

所有 5 格必须保持同一个商品真相。

## DTC 视觉真实感门槛

故事版应该像真实可生产的电商 / DTC 品牌素材，不像泛 AI lifestyle 广告。

如果出现以下问题，拒绝或重画：

- 商品不可读
- 场景好看但没用
- 光线或阴影假
- 商品比例变化
- 手部或身体交互不符合物理逻辑
- 道具干扰商品决策
- 创意镜头变成无关美术风格
- 商品消失在视觉世界里
- 最后一格不能增强购买信心

## 脚本规则

默认 15 秒。用户要求 30 秒时才用 30 秒。

脚本必须严格匹配故事版。

不要引入：

- 新人物
- 新房间
- 新声明
- 新商品动作
- 新利益点
- 新视觉世界
- 故事版里没有的平台 CTA

15 秒脚本格式：

```markdown
| 时间 | 画面 | 屏幕字幕 | 旁白 / 口播 |
|---|---|---|---|
| 0-2s | ... | Clear product hook | "..." |
| 2-5s | ... | Show the problem | "..." |
| 5-8s | ... | See the detail | "..." |
| 8-11s | ... | Watch it work | "..." |
| 11-15s | ... | Ready to buy | "..." |
```

所有屏幕字幕和旁白必须是英文。

## 交付前检查

回复前检查：

- 是否先展示产品图
- 商品真相是否保持
- 是否内部选择了 DTC creative lens
- buyer event 是否有商品证据支持
- 商品是否在第 1 或第 2 格明确成为主角
- 商品是否持续可见、可检查
- 至少两格是否证明商品细节
- 至少两格是否承载创意镜头
- 是否没有添加不支持的声明或场景
- 故事版是否像一个连续的 DTC 商品创意，而不是五张随机图
- 脚本是否匹配故事版
- 脚本文字是否为英文
- 默认输出是否只有三段
