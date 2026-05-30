# Sprite 属性

你可以通过 *Sprite > 属性* 菜单 (<kbd>Ctrl + P</kbd> 或 <kbd>⌘ P</kbd>) 更改一些 Sprite 属性：

![Sprite 属性对话框](./sprite-properties/sprite-properties.png)

你可以：

* 更改[透明颜色](./transparent-color.md)（适用于[索引颜色模式](./color-mode.md#indexed)）
* 更改像素宽高比
* 分配或转换[颜色配置文件](./color-profile.md)

## 颜色配置文件

在 *Sprite 属性* 对话框中，你有两个按钮：一个用于**分配**其他
颜色配置文件，另一个用于**转换**为其他颜色配置文件：

* 如果你为 Sprite **分配**一个新的颜色配置文件，像素值
  将不会被修改，只是将新的颜色配置文件分配给
  Sprite。你会注意到图片中的颜色将发生变化，
  因为现在 RGB 值是相同的，但[色彩空间](./color-profile.md)
  已改变。例如，“纯红”值 (255, 0, 0) 现在可能
  与之前的“纯红”不同。
* 如果你**转换**颜色配置文件，像素值将从
  一个色彩空间转换到另一个色彩空间，因此颜色在视觉上不应该
  有差异，但每个 RGB 值都将被调整以适配
  新的色彩空间（因此几乎所有像素值都将被修改）。

---

**另请参阅**

[新建 Sprite](./new-sprite.md) |
[颜色配置文件](./color-profile.md) |
[透明颜色](./transparent-color.md)