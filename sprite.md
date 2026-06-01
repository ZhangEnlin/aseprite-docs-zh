# Sprite 结构

在 Aseprite 中，一个文档/文件/Sprite 具有以下属性：

1. 它有一个以像素为单位的[尺寸](./sprite-size.md)（宽度和高度）。

1. 它有一个[颜色模式](./color-mode.md)，这告诉你图像可以处理多少种颜色。Sprite 中的所有图像都处于一种特定模式下，你不能在同一个 Sprite 中混合 RGB 

   图像和索引图像。

1. 一个[颜色配置文件](./color-profile.md)，指示 RGB 值所在的色彩空间。

1. 它包含一组图层。可以在[时间轴](./timeline.md)中看到它们。这里最重要的概念是存在两种图层：

   - [背景图层](./layers.md#background-layer)用于不透明的 Sprite
   - [透明图层](./layers.md#transparent-layers)

   一个 Sprite 只能包含一个背景图层，但可以包含多个透明图层。

1. 它包含动画帧。每个帧都有一个持续时间，即当动画播放时，该帧必须在屏幕上停留多少毫秒。

1. 每个图层/帧的交汇处称为 [cel](./cel.md)，其中包含你最终可以进行[绘制](./drawing.md)的图像。

[时间轴](./timeline.md)以网格形式向你展示 Sprite 的整个结构。行是图层，列是帧，矩阵中的每个小格子是一个 [cel](./cel.md)：

<img src="./sprite/sprite-components.png" alt="Cels 矩阵" class="xN" />

可以看到一些额外的元素，如[标签](./tags.md)和[链接 cel](./linked-cels.md)。这些元素对于组织同一个 Sprite 的多个动画，以及在不同动画（或同一动画的不同部分）中复用帧非常有用。

---

**另请参阅**

[颜色模式](./color-mode.md) |
[保存](./save.md) |
[Sprite 尺寸](./sprite-size.md)