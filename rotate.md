# 旋转精灵图或选区

任何选区都可以使用[手柄](./rotate.md#handles)或[菜单选项](./rotate.md#menu-options)进行旋转，这两种方法都将使用选定的[算法](./rotate.md#rotation-algorithms)围绕[枢轴点](./rotate.md#rotation-pivot)旋转选区。

## 旋转枢轴

![旋转枢轴](./rotate/pivot-point-context-bar.png)

选区围绕一个单一的定义点（![旋转枢轴](./rotate/pivot-point.png)）旋转。默认情况下，枢轴点设置在选区的中心，在你开始旋转图像之前不可见。

它的位置和可见性设置可以通过任何选区工具的上下文栏进行更改。旋转枢轴也可以通过按住<kbd>左键单击</kbd>并拖动该点来用鼠标移动：

![旋转枢轴设置](./rotate/pivot-point-settings.gif)
![使用鼠标移动旋转枢轴](./rotate/pivot-point-mouse-move.gif)

<div style="font-style:italic;text-align:right;">精灵图作者：<a href="https://twitter.com/ThKasparrr">@ThKasparrr</a></div>

## 手柄

通过将鼠标移动到手柄的外部（![手柄](./rotate/handle.png)），按住<kbd>左键单击</kbd>并在画布上拖动鼠标，可以旋转选区：

![旋转手柄](./rotate/rotate-handles.gif)

鼠标光标会随之改变，以指示拖动手柄将调整选区大小还是旋转选区：

|        |                   调整大小                   |                   旋转                   |
| ------ | :----------------------------------------: | :----------------------------------------: |
| 光标   | ![调整大小手柄](./cursor/resize-handle.png) | ![旋转手柄](./cursor/rotate-handle.png) |

使用 <kbd>Shift</kbd> 键可以吸附角度（0º、45º、90º 等）。

## 菜单选项

![编辑 > 旋转](./rotate/edit-rotate.png)

可以使用*编辑 > 旋转*下的菜单选项将选区旋转 90º 或 180º。

![旋转菜单选项](./rotate/rotate-menu-options.gif)

## 旋转算法

![旋转算法](./rotate/rotation-algorithms.png)

有两种可用的旋转算法：

- 快速旋转
- [RotSprite](https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#RotSprite)

虽然 RotSprite 被广泛认为是一种能产生更好结果的算法，但选择取决于你的偏好。

![快速旋转与 RotSprite](./rotate/rotation-algorithm.gif)

---

**另请参阅**

[翻转](./flip.md) |
[调整大小](./resize.md) |
[移动](./move-selection.md)