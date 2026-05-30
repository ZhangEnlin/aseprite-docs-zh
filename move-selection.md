# 移动选区

在[选取](./selecting.md)了 [活动 cel](./cel.md) 的一部分后，你可以使用鼠标拖放或使用方向键来移动选中的像素区域：

![移动选区示例](./move-selection/move-selection.gif)

如果你正在从[背景图层](./layers.md#background-layer)移动一个像素区域，选区将被当前的[背景色](./color-bar.md#background-color)清除。如果你移动透明图层，该区域将被透明色清除。

移动选区时，你可以在[上下文栏](./context-bar.md)中找到变换选项。

![上下文栏示例](./move-selection/contextbar.png)

- X 位置
- Y 位置
- 宽度
- 高度
- 旋转
- 倾斜

这些值可以通过上下文栏或[变换](./transformations.md)来编辑。