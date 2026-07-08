---
name: storyboard-dtc-product-creative
description: Use when a user wants a SKU-level DTC product creative storyboard from a product link, Amazon/Shopify/TikTok Shop URL, product image, product screenshot, ecommerce page, ASIN, SKU brief, or short product description. The required output format is exactly product image first, then a generated horizontal storyboard image/contact sheet, then 15-second or 30-second video script text. Product truth is the hard gate; DTC creative lens is allowed only after product identity, function, material, scale, claims, and use logic are locked.
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

这个 skill 面向 SKU 级电商内容创意，不是泛广告文案工具。

优先级顺序：

```text
商品真相
> 内容属性
> 买家决策逻辑
> DTC 创意角度
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

`## 2. 故事版` 必须输出真实图片：一张横屏 5 格 16:9 storyboard / contact-sheet 图。不能只输出文字分镜、表格、prompt 或镜头描述。

图片必须是横屏拍摄逻辑：不能是竖屏拼贴，不能是方图思维，不能把 5 格做成竖向排列。

如果当前环境不能生成或嵌入图片，停止并说明缺少图片生成能力；不要用文字故事版代替。

第三段脚本必须是英文。表格里的 `屏幕字幕` 和 `旁白 / 口播` 必须是自然英文。

## 执行流程

每次运行都按 6 步走，不要跳步。

### 1. 证据锁定

读取产品图、商品页、截图或 SKU brief，建立商品真相。

完成标准：

- 能指出商品是什么。
- 能指出哪些视觉事实不能变。
- 能指出哪些功能、结果或声明没有证据，不能写。
- 如果证据不足，停止，不进入故事版。

### 2. 内容属性卡

建立内部 `Content Attribute Card`。

完成标准：

- `target_buyer` 具体，不是泛泛的 customers。
- `buyer_stage` 已选择。
- `content_angle` 只选一个。
- `hook_type` 只选一个。
- `core_message` 是一句话，不是卖点列表。
- `reason_to_believe` 能被画面证明。
- `objection` 和 `proof_asset` 对应。
- `cta_intent` 是买家下一步动作，不是空泛 slogan。

### 3. 内容策略选择

把内容属性转成一个可拍的内容策略。

完成标准：

- `shopper_tension` 能解释为什么用户会继续看。
- `buyer_event` 是一个真实可见动作或时刻。
- `creative_lens` 服务内容角度，不只是视觉风格。
- `product_entrance` 发生在第 1 或第 2 格。
- `visual_device` 能组织 5 格画面。

### 4. 横屏故事版图片生成

把内容策略映射并生成成一张横屏 5 格 16:9 storyboard / contact-sheet 图片。

完成标准：

- `## 2. 故事版` 下方已经嵌入实际图片。
- 最终图片是横屏；如果工具支持画幅参数，使用 16:9 landscape。
- 5 个画面必须是横屏 16:9 frame。
- 5 个画面默认横向单行排列；不要竖向排列。
- 每一格有一个内容任务。
- 每一格都保持商品真相。
- 每一格像同一次真实拍摄里的连续镜头。
- 至少两格证明商品细节。
- 至少两格承载内容角度或 creative lens。
- 第 5 格增强购买信心，而不是只做漂亮收尾。

### 5. 英文脚本

写 15 秒或 30 秒英文脚本。

完成标准：

- 每行字幕和旁白都服务对应内容任务。
- 不用旁白补救画面没有证明的内容。
- 不添加故事版没有的新利益点、新场景或新 CTA。

### 6. 交付前 QA

按 `交付前检查` 逐项检查。

完成标准：

- 默认输出仍然只有三段。
- 第二段已经输出真实故事版图片。
- 内容属性、创意镜头、脚本和故事版互相一致。
- 商品真相优先级高于所有创意表达。

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

## 内容属性层

DTC 内容不能只有镜头，必须先有内容属性。

在内部建立 `Content Attribute Card`，用于决定故事版和脚本。

必须判断：

1. `target_buyer`
   这条内容说给谁看？不要只写泛泛的 "customers"。

2. `buyer_stage`
   买家处在哪个阶段？
   - unaware
   - problem aware
   - solution aware
   - product aware
   - most aware

3. `content_angle`
   这条内容的主角度是什么？只能选一个主角度。

4. `hook_type`
   前 2 秒用什么方式让人继续看？

5. `core_message`
   这条内容只想让用户记住的一句话是什么？

6. `product_promise`
   商品能承诺什么？必须有商品证据支持。

7. `reason_to_believe`
   用户凭什么相信？来自材质、结构、细节、操作、评论、规格、对比或可见结果。

8. `objection`
   买家可能担心什么？尺寸、质量、使用难度、适配、效果、价格、耐用性、真实性等。

9. `proof_asset`
   这条内容用什么可见证据消除疑虑？

10. `cta_intent`
   最后希望用户做什么？了解细节、确认适配、选择款式、加入购物车、查看定制效果等。

这些属性必须影响故事版和脚本。不要只生成漂亮镜头。

默认不要把完整 `Content Attribute Card` 作为独立章节输出；但 `## 2. 故事版` 里的创意大片方向必须体现这些属性。

## 内容策略映射

`content_angle` 决定说什么，`hook_type` 决定怎么开场，`creative_lens` 决定怎么拍。

三者必须匹配：

```text
content_angle -> hook_type -> creative_lens -> proof_asset -> CTA intent
```

不要出现：

- 内容角度是 objection handling，但画面没有消除疑虑。
- hook 是 curiosity gap，但后面没有解释这个 gap。
- creative lens 是 visual metaphor，但隐喻改了商品功能。
- proof_asset 是材质/结构，但故事版只展示生活方式。
- CTA intent 是确认适配，但最后一格没有给适配信心。

## Buyer Event

`buyer_event` 是承载内容角度的真实动作或时刻。

它不是大剧情，也不是情绪包装。

好的 `buyer_event`：

- 展示买家正在确认尺寸、材质、配置、颜色、用法或结果。
- 展示商品进入真实流程中的一个关键瞬间。
- 展示一个可见细节如何解决一个疑虑。
- 展示从问题到商品证明的最短路径。

差的 `buyer_event`：

- 为了氛围添加家庭、送礼、户外、派对、夸张人物。
- 让商品变成背景道具。
- 只制造情绪，不解决买家问题。
- 依赖无法证明的功效或结果。

## DTC 内容角度菜单

`content_angle` 决定这条内容讲什么，不等于镜头风格。

选择一个主角度：

- `problem-solution`
  从买家真实问题进入，商品作为解决方案。

- `objection handling`
  专门消除一个购买疑虑，比如尺寸、材质、适配、安装、效果、真实性。

- `feature-to-benefit`
  从一个可见功能或结构，转译成用户利益。

- `use-case demo`
  展示一个具体使用场景，不能泛生活方式化。

- `comparison`
  和旧状态、普通方案、错误用法或不合适选择做对比；不能编造竞品事实。

- `social identity`
  让用户感觉“这是为我这种人做的”；必须有真实人群或使用语境支持。

- `customization / choice`
  适合定制、选项、颜色、组合、尺寸、套装、模块化商品。

- `trust proof`
  用细节、材质、工艺、结构、规格、真实评论或可见结果建立信任。

- `sensory proof`
  用质地、声音、触感、重量、光泽、液体、食物状态等感官线索证明商品。

- `routine integration`
  展示商品如何进入日常流程，而不是孤立摆拍。

不要选择证据不支持的内容角度。

内容角度必须落到 5 格：

| content_angle | 第 2 格任务 | 第 4 格任务 | 第 5 格任务 |
|---|---|---|---|
| problem-solution | 让问题可见 | 商品解决过程 | 解决后的可信状态 |
| objection handling | 明确一个疑虑 | 用证据消除疑虑 | 给购买信心 |
| feature-to-benefit | 展示功能入口 | 功能转成利益 | 利益和商品绑定 |
| use-case demo | 建立具体场景 | 展示真实使用 | 收束到使用后状态 |
| comparison | 建立对比对象 | 商品差异可见 | 明确为什么选它 |
| social identity | 建立人群语境 | 商品服务身份/场景 | 用户自我代入 |
| customization / choice | 展示选择问题 | 展示配置/定制过程 | 最终选择状态 |
| trust proof | 建立不信任点 | 展示可信证据 | 强化放心购买 |
| sensory proof | 建立感官期待 | 展示质地/声音/触感 | 保留可感知记忆点 |
| routine integration | 建立日常流程 | 商品进入流程 | 流程完成状态 |

## DTC Hook 菜单

`hook_type` 决定前 2 秒怎么进入。

选择一个：

- `visual interruption`
  用不寻常但真实的画面让人停下。

- `problem recognition`
  让用户立刻认出自己的问题。

- `specific claim`
  给出一个可证明、不过度的具体卖点。

- `curiosity gap`
  展示一个真实细节，让用户想知道原因。

- `before-after contrast`
  展示可信的前后状态，不编造效果。

- `micro demo`
  直接展示一个小动作或小结果。

- `detail macro`
  用商品细节作为开场。

- `choice reveal`
  展示颜色、款式、定制、配置或套装选择。

Hook 必须和商品证据相关。不要用泛情绪钩子。

Hook 必须在第 1 格和 0-2s 脚本同时成立。

如果画面看不出 hook，重写第 1 格。

如果字幕/旁白里的 hook 不能被画面证明，删掉或改弱。

## DTC 创意判断

锁定商品真相后，再内部选择 DTC 创意方向。

依次判断：

1. `shopper_tension`
   买家现在有什么疑虑、欲望、痛点或决策问题？

2. `content_angle`
   这条内容用哪个角度说服用户？

3. `hook_type`
   前 2 秒如何进入？

4. `reason_to_watch`
   为什么这个内容值得做成短视频 / 故事版，而不是只用静态商品图？

5. `creative_lens`
   哪种 DTC 创意角度能让商品证明更有记忆点？

6. `product_entrance`
   商品如何在第 1 或第 2 格成为明确主角？

7. `visual_device`
   用什么视觉装置组织 5 格画面？

8. `proof_sequence`
   每一格依次证明哪些商品事实？

9. `script_payload`
   脚本里每一行字幕和旁白分别承担什么内容任务？

10. `creative_safety`
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

creative lens 必须服务 content_angle。

示例：

- `objection handling` + `mechanism reveal`: 用结构/材质近景消除质量疑虑。
- `customization / choice` + `configuration reveal`: 用选项变化证明可配置。
- `trust proof` + `proof-first demo`: 用细节和使用过程建立信任。
- `feature-to-benefit` + `visual metaphor`: 用简单隐喻帮助理解利益，但不改变商品功能。
- `routine integration` + `social proof scene`: 展示商品进入日常流程，但人物不能压过商品。

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

故事版必须是一张图片。

必须调用可用的图片生成或图片编辑能力，生成一张横屏 5 格 16:9 storyboard / contact-sheet 图，并把图片嵌入 `## 2. 故事版`。

## 横屏画幅门槛

故事版图片用于横屏视频预演。

必须满足：

- 最终画布是 landscape 横屏，不是 portrait 竖屏。
- 每一个 panel 都是横屏 16:9 构图。
- 默认用 5 个横屏 panel 横向单行排列。
- 如果图片模型容易做成方图，也必须在图内保留明确横屏 contact sheet，不做竖向堆叠。
- panel 编号可以很小，但不能挤占商品画面。

如果生成结果出现以下情况，必须重生成：

- 竖屏画布
- 方形九宫格感
- 5 格上下排列
- panel 内部是竖屏短视频画面
- 商品被竖向裁切，看不清横屏构图

## 连续拍摄门槛

故事版不是 5 张随机图。

必须像同一次真实拍摄里的连续关键帧：

- 同一个商品实例。
- 同一颜色、材质、比例、包装、logo / 标签。
- 同一个拍摄世界。
- 同一光源方向和光线强度。
- 同一桌面 / 房间 / 背景材质。
- 同一镜头语言，允许远景、中景、近景变化，但不能像不同广告片。
- 同一手部 / 人物设定；如果没有必要，不引入人物。
- 动作从上一格自然进入下一格。

如果生成结果出现以下情况，必须重生成：

- 每格像不同场景
- 商品比例、颜色或材质跳变
- 光线方向跳变
- 手部、人物或道具不连续
- 第 1 格和第 5 格像两个不同项目

## 真实拍摄门槛

图片必须像真实可拍的 DTC 商品素材，而不是 AI 风格概念图。

生成图片时优先使用：

- natural daylight / soft studio daylight
- real shadows
- physical contact shadows
- readable material texture
- realistic lens perspective
- practical tabletop, hand, hanger, package, use setup
- product-first composition
- restrained props

避免：

- plastic skin / plastic fabric
- glossy unreal surfaces
- floating product
- impossible shadows
- over-sharp AI texture
- random decorative props
- fantasy lighting
- fake UI
- fake review cards
- fake platform badges
- unreadable micro text

如果商品是定制类、配置类或上传图片类，设计素材只用中性占位卡表示，除非商品证据里明确给出具体图案。不要生成看起来像商品自带的假图案。

不允许把下面任何内容当作故事版交付：

- 文字分镜表
- 纯 prompt
- 纯镜头说明
- 只有 shot list，没有图片
- 只有素材建议，没有图片

图片故事版必须：

- 商品主导
- 有 DTC 创意，但必须基于证据
- 有记忆点
- 有商业可用性
- 足够真实，可以成为电商生产素材
- 横屏画幅正确
- 5 格保持一致
- 5 格动作连贯
- 只围绕一个清晰 creative lens

默认故事版格式：

```text
内容属性锁: 一句概括 target_buyer、content_angle、hook_type、core_message、proof_asset
创意大片方向: 一句简洁的 DTC Creative Film Treatment
同一拍摄世界锁: 一段紧凑的 Shooting World Lock
5 格 16:9 横屏连续关键帧图片: 这里必须嵌入一张实际生成的横屏 storyboard/contact-sheet 图，包含五个编号 16:9 商品证明创意画面；每格必须有内容任务、真实拍摄感和连续动作
```

默认不把每格画面写成表格。每格任务应该进入图片生成指令和最终图片，而不是作为文字故事版替代图片。

5 格逻辑：

1. Hook / 商品进入 / SKU 锚点
2. 买家疑虑 / 内容角度建立
3. 商品证明 / 机制 / 细节
4. 使用瞬间 / 利益点 / 反对点消除
5. CTA intent / 购买信心 / 最终商品主导状态

至少两格必须证明商品细节。

至少两格必须承载 DTC creative lens。

所有 5 格必须保持同一个商品真相。

## DTC 视觉真实感门槛

故事版应该像真实可生产的电商 / DTC 品牌素材，不像泛 AI lifestyle 广告。

如果出现以下问题，拒绝或重画：

- 竖屏或方图，不适合横屏视频预演
- 商品不可读
- 场景好看但没用
- 光线或阴影假
- 商品比例变化
- 手部或身体交互不符合物理逻辑
- 道具干扰商品决策
- 创意镜头变成无关美术风格
- 商品消失在视觉世界里
- 5 格缺少连续动作，像五张随机生成图
- 最后一格不能增强购买信心

## 脚本规则

默认 15 秒。用户要求 30 秒时才用 30 秒。

脚本必须严格匹配故事版。

脚本每一行必须承担一个内容任务：

```text
0-2s: hook + product entrance
2-5s: shopper tension / content angle
5-8s: product proof / reason to believe
8-11s: benefit / use case / objection handling
11-15s: CTA intent / purchase confidence
```

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
| 2-5s | ... | Why it matters | "..." |
| 5-8s | ... | Proof you can see | "..." |
| 8-11s | ... | Built for this use | "..." |
| 11-15s | ... | Check the details | "..." |
```

所有屏幕字幕和旁白必须是英文。

字幕规则：

- 字幕要短，优先 2-6 个英文词。
- 字幕承担内容任务，不重复画面废话。
- 字幕不能写画面没证明的卖点。
- 旁白可以补充解释，但不能替代 proof_asset。

## 交付前检查

回复前检查：

- 是否先展示产品图
- `## 2. 故事版` 是否已经嵌入真实图片
- 图片是否是横屏，不是竖屏或方图
- 5 个 panel 是否都是横屏 16:9 构图
- 5 格是否像同一次拍摄里的连续关键帧
- 真实拍摄感是否足够，是否有真实阴影、材质和物理接触
- 是否没有用文字分镜、表格或 prompt 替代故事版图片
- 商品真相是否保持
- 是否内部建立了 Content Attribute Card
- target_buyer、buyer_stage、content_angle、hook_type、core_message 是否清楚
- 是否内部选择了 DTC creative lens
- buyer event 是否有商品证据支持
- 商品是否在第 1 或第 2 格明确成为主角
- 商品是否持续可见、可检查
- 至少两格是否证明商品细节
- 至少两格是否承载创意镜头
- 每一格是否有内容任务，而不是只负责好看
- 脚本是否包含 hook、tension、proof、benefit、CTA intent
- 是否没有添加不支持的声明或场景
- 故事版是否像一个连续的 DTC 商品创意，而不是五张随机图
- 脚本是否匹配故事版
- 脚本文字是否为英文
- 默认输出是否只有三段
