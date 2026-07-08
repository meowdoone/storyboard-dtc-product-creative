# DTC 运动库

## 用途

让故事版图片可以继续做视频 demo。每个动作都必须有清楚的起点、动作和终点。

```text
start_state -> action -> end_state
```

## Product Motions

| motion_id | 适用商品 | start_state | action | end_state |
|---|---|---|---|---|
| pick-up | 可手持商品 | 商品静置 | 手拿起 | 商品进入使用位置 |
| unbox | 包装/套装 | 包装关闭 | 打开并取出 | 商品和部件可见 |
| align | 定制/贴合/安装 | 商品和参考物分离 | 对齐 | 位置被确认 |
| apply | 护理/贴片/涂抹 | 商品接近身体/表面 | 涂抹/贴合 | 使用状态可见 |
| pour | 液体/食品/清洁 | 容器倾斜前 | 倒出 | 质地或用量可见 |
| tap | 数码/开关/屏幕 | 手指接近 | 点击 | 状态变化 |
| plug-in | 数码/车载/家电 | 接口分离 | 插入 | 连接关系成立 |
| wear | 穿戴/配饰 | 商品离开身体 | 穿戴 | 上身/佩戴状态 |
| unfold | 服饰/收纳/折叠 | 折叠状态 | 展开 | 完整形态可见 |
| fold | 收纳/服饰 | 展开状态 | 折叠 | 便携/收纳状态 |
| hang | 服饰/家居 | 商品手持 | 挂起 | 完整轮廓可见 |
| compare | 替代品/多选项 | 两个方案同框 | 手部指向/切换 | 差异清楚 |
| wipe | 清洁/屏幕/护理 | 表面有状态 | 擦拭 | 可见清理/接触过程 |
| rotate | 包装/工艺/细节 | 正面 | 旋转 | 多角度可见 |
| reveal | 定制/套装/礼品 | 遮挡 | 揭开 | 关键卖点出现 |
| pack | 旅行/收纳 | 商品散开 | 放入包/盒 | 便携状态 |
| hand-pass | 社交/礼物/家庭 | 一人持有 | 递交 | 另一人接住 |
| texture-touch | 材质型商品 | 手指接近 | 触摸/按压 | 材质反馈可见 |

## Camera Motions

- locked-off demo
- slow push-in
- top-down tracking
- handheld follow
- rack focus
- macro push-in
- orbit reveal
- match cut
- whip pan
- settle to hero frame

## Motion QA

失败条件：

- 上一格和下一格动作接不上。
- 商品动作和人物动作没有关系。
- 镜头运动盖过商品。
- 动作需要视频才能理解，但图片帧没有关键状态。
- 5 格像随机摆拍，不像动作链。

