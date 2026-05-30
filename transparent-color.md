# 透明颜色

在 [RGB](./color-mode.md#rgb) 和 [灰度](./color-mode.md#grayscale) Sprite 中，透明像素是 `Alpha=0` 的颜色，但在[索引](./color-mode.md#indexed)颜色模式下，调色板中存在一个特定且特殊的索引，它将代表[透明图层](./layers.md#transparent-layers)的透明颜色：

![透明颜色](./transparent-color/transparent-color-property.png)

这意味着图层中引用此特定索引的像素将不可见（只有背景图层可以将“透明颜色”显示为纯色）。

你可以使用[颜色栏](./color-bar.md)中的鼠标中键，或通过 [*Sprite > 属性*](./sprite-properties.md) 菜单选项来更改透明颜色。

---

**另请参阅**

[颜色](./color.md) |
[颜色模式](./color-mode.md) |
[Sprite 属性](./sprite-properties.md)