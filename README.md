# Storyboard DTC Product Creative Skill

把真实商品转成 DTC 风格的商品主导创意故事版。

这个 skill 的核心不是泛广告创意，而是：

```text
商品真相
-> 内容属性
-> 买家决策逻辑
-> DTC creative lens
-> 商品证明故事版
-> 英文短视频脚本
```

默认只输出：

```markdown
## 1. 产品图

## 2. 故事版

## 3. 15 秒或者 30 秒视频脚本文字
```

## 核心原则

商品最重要。

DTC 创意只能增强商品表达，不能改商品。

如果创意会改变商品的形状、材质、颜色、包装、功能、使用方式、比例、功效声明或买家决策逻辑，必须删掉创意。

## 内容属性

这个 skill 不是只选镜头风格，必须先有内容属性。

内部会建立：

```text
target_buyer
buyer_stage
content_angle
hook_type
core_message
product_promise
reason_to_believe
objection
proof_asset
cta_intent
```

这些字段决定故事版和英文脚本。

## 内部流程

```text
读取商品证据
+ 锁定 Product Truth
+ 判断商品行为
+ 建立 Content Attribute Card
+ 找 shopper_tension
+ 选择 content_angle 和 hook_type
+ 选择 DTC creative lens
+ 设计 product_entrance
+ 组织 5 格 16:9 商品创意故事版
+ 写 15 秒或 30 秒英文脚本
```

## DTC content angle

可选内容角度：

- problem-solution
- objection handling
- feature-to-benefit
- use-case demo
- comparison
- social identity
- customization / choice
- trust proof
- sensory proof
- routine integration

## DTC creative lens

可选创意镜头：

- proof-first demo
- before-trigger-after
- mechanism reveal
- configuration reveal
- scale / fit / compatibility proof
- visual metaphor
- restrained color-world
- social proof scene
- curiosity gap

这些只在内部使用，不作为默认输出章节。

## 使用示例

```text
用 storyboard-dtc-product-creative，基于这个商品链接输出产品图、DTC 商品创意故事版、15 秒英文脚本。商品必须保持真实，创意不能改变商品。
```

```text
用这个产品图做 DTC 商品创意故事版。产品为主，先锁商品真相，再选择一个 DTC creative lens，输出 5 格 16:9 连续关键帧和英文脚本。
```

```text
用这个商品做 DTC 内容创意，重点不是漂亮图，而是先明确 target_buyer、content_angle、hook_type、proof_asset 和 CTA intent，再输出故事版和英文脚本。
```

## 不做什么

- 不默认做 Meta 广告批量生成
- 不默认做竞品调研
- 不默认做 Reddit / Facebook Ads Library research
- 不默认输出 DTC 理论
- 不把商品变成创意道具
- 不为了视觉冲击改变 SKU
