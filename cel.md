# Cel

官方文档解释：Cel（源自[赛璐珞](http://en.wikipedia.org/wiki/Cel)）是位于特定帧和图层中，处于画布上特定 *xy* 坐标处的一个图像。

> [!tip]
>
> **本开源仓库作者补充**：
>
> 为了便于理解，按下 Tab 键打开 Aseprite 的[时间轴](move-cels.md)面板，你会看到一个网格。**每一个网格里的小点，就是一个 Cel** 。

![时间轴上的 Cel](./cel/cel-on-timeline.png)

帧和 Cel 之间的区别在于，帧是特定时间上所有图层的 Cel 的集合：

![时间轴上的帧](./cel/frame-on-timeline.png)

## 移动 Cel

使用[移动工具](./move-tool.md)在画布中拖放当前的 Cel。或者，也可以使用时间轴将 Cel 移动到另一个图层/帧位置。

## 更改不透明度

在 [RGB](./color-mode.md#rgb) 图像中，每个 Cel 有其自身的不透明度级别。通过右键单击 Cel 并选择 *属性*（或 *帧 > Cel 属性*），然后调整 *不透明度* 滑块来更改 Cel 的不透明度。

![更改 Cel 不透明度示例](./cel/cel-opacity.gif)

----

**另请参阅**

[链接 Cel](./linked-cels.md) |
[时间轴](./timeline.md)