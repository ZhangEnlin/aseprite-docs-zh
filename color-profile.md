# 颜色配置文件

我们可以将屏幕上的一个像素视为一个带有三个特定 RGB 值的小矩形，每个值可以看作一个从 0.0 到 1.0 的数字（或者从 0 到 255 的整数）。它指示了在 3D 空间中的一个位置，其中每个值分别是每个轴（红色、绿色和蓝色）上的一个坐标：

![RGB 立方体](./color-profile/rgb-cube.png)

但是，在这个 3D 立方体中的一个位置意味着什么呢？我们知道
*RGB=(0, 0, 0)* 代表黑色，
*RGB=(255, 0, 0)* 代表红色，*RGB=(255, 255, 255)* 是白色，等等。但[白色](https://en.wikipedia.org/wiki/White_point)具体是什么？
当你的显示器被校准，并且制造商说“好的，这就是白色”时，所使用的环境光是什么？

每个必须处理颜色的设备（显示器、打印机、相机、扫描仪等）都必须经过校准，以便将周围环境中的光线转换为图片中的特定 RGB 值，或者反过来，将立方体中的这些 RGB 值转换为[光波](https://en.wikipedia.org/wiki/Light)。

颜色配置文件指明了这些 RGB 值位于哪个[色彩空间](https://en.wikipedia.org/wiki/Color_space)中。这意味着什么是纯红色、纯蓝色、纯绿色或纯白色。
它用于将一个设备（例如，你用来创建图像的显示器）上的 RGB 值与另一个设备（例如，将要在其显示器上观看你图像的用户）上的 RGB 值进行匹配。

互联网上的图像通常使用
[sRGB 色彩空间](https://en.wikipedia.org/wiki/SRGB)，
但 [PNG 文件](https://en.wikipedia.org/wiki/Portable_Network_Graphics)和
[JPEG 文件](https://en.wikipedia.org/wiki/JPEG)可以嵌入
特定的 [ICC 颜色配置文件](https://en.wikipedia.org/wiki/ICC_profile)，
其中包含其 [RGB 色域](https://en.wikipedia.org/wiki/Gamut)
和[伽马校正](https://en.wikipedia.org/wiki/Gamma_correction)。
从 Aseprite v1.2.10-beta2 开始，你也可以
[在 `.aseprite` 文件中保存颜色配置文件](https://github.com/aseprite/aseprite/blob/master/docs/ase-file-specs.md#color-profile-chunk-0x2007)。

你可以通过[精灵属性](./sprite-properties.md)来分配或转换当前精灵的颜色配置文件。并且你可以通过 *编辑 > 首选项 > 颜色* 来配置 Aseprite 管理颜色配置文件的方式：

![颜色管理首选项](./color-profile/color-management-preferences.png)

---

**另请参阅**

[颜色](./color.md) |
[精灵属性](./sprite-properties.md)