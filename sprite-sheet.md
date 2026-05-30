# Sprite Sheet

Sprite Sheet 是一张包含同一 Sprite 的多个帧的大图像。
例如，可以保存这个动画：

![奔跑的人](./sprite-sheet/running-guy.gif)

作为水平的 Sprite Sheet：

![水平 Sprite Sheet](./sprite-sheet/running-guy-horz.png)

垂直的：

![垂直 Sprite Sheet](./sprite-sheet/running-guy-vert.png)

或者矩阵式的：

![矩阵 Sprite Sheet](./sprite-sheet/running-guy-matrix.png)

在下面的部分，你将了解如何将此类图像导入
Aseprite 以及如何导出它们。

## 导入

要导入 Sprite Sheet，请使用 *文件 > 导入 Sprite Sheet* 选项。
然后可以选择要导入的文件，并指定偏移 `x`、
`y` 以及 Sprite 的 `width`、`height`。

![导入 Sprite Sheet 01](./sprite-sheet/running-guy-import-01.png)

如果 Sprite 之间存在间隙，可以使用填充（Padding），
并且 Sheet 类型会影响 Sprites 的获取顺序。

![导入 Sprite Sheet 02](./sprite-sheet/running-guy-import-02.png)

## 导出

要导出 Sprite Sheet，请使用 *文件 > 导出 Sprite Sheet* 选项。
可以选择所有可见图层或特定图层，
并根据标签选择帧。

![导出 Sprite Sheet](./sprite-sheet/running-guy-export.png)

## 从命令行自动化

（*正在进行中*）

## 纹理图集

纹理图集是一张巨大的图像，包含了游戏将使用的所有图形、Sprite 和
图像。它之所以被称为"纹理"，是因为该图像
可以加载到显存中，以便在屏幕上利用硬件加速渲染图形。