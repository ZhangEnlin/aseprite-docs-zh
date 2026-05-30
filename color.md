# 颜色

本节讲述 Aseprite 如何管理颜色。

首先，你需要了解，一个特定的精灵
（[新创建的](./new-sprite.md)或[一个已有的精灵](./open.md)）
拥有三个属性，它们会修改精灵的编辑和显示方式：

* 精灵的[颜色模式](./color-mode.md)
* [颜色配置文件](./color-profile.md)
* 以及[透明色](./transparent-color.md)
  （仅限于[索引图像](./color-mode.md#indexed)）

与此同时，还有两种活动颜色可用于绘制或擦除精灵的部分：

* 当前的[前景色](./color-bar.md#foreground-color)
* 当前的[背景色](./color-bar.md#background-color)

## 颜色模式

多种调整和命令根据当前活动颜色模式的不同，其工作方式也会有所差异。[RGB](https://en.wikipedia.org/wiki/RGB_color_model) 和 [索引](https://en.wikipedia.org/wiki/Indexed_color)是网络图像最常用的两种模式。

你应该在 **[颜色模式](./color-mode.md)** 一节中了解更多相关信息。

## 颜色配置文件

颜色配置文件指明了图像 RGB 值预期所在的[色彩空间](https://en.wikipedia.org/wiki/Color_space)。它用于将一个设备（例如，你用来创建图像的显示器）上的 RGB 值与另一个设备（例如，将要在其显示器上观看你图像的用户）上的 RGB 值进行匹配。互联网上的图像通常使用 [sRGB 色彩空间](https://en.wikipedia.org/wiki/SRGB)。

请在 **[颜色配置文件](./color-profile.md)** 一节中了解更多相关信息。

---

**另请参阅**

[颜色模式](./color-mode.md) |
[颜色配置文件](./color-profile.md) |
[颜色栏](./color-bar.md)