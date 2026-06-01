# 图层

一个精灵图可以细分为多个图层。可以在[时间轴](./timeline.md)中看到它们：

![时间轴中的图层](./layers/layer-in-timeline.png)

每个图层都有几个选项：

![图层图标](./layers/layer-options.png)

<span style='color: hotpink'>*图层名称*</span>：用于标识该图层的文本。可以通过双击图层，或通过*图层 > 属性*菜单（<kbd>Shift + P</kbd> 键）来更改图层名称。

<span style='color: hotpink'>*Cel*</span>：一组 [cel](./cel.md)，即特定图层在特定帧中包含可见内容的帧。

<span style='color: hotpink'>*可见*</span>：指示该图层是可见的 ![可见图层图标](./layers/visible-layer.png) 还是隐藏的 ![隐藏图层图标](./layers/hidden-layer.png)。可以使用*图层 > 可见*菜单或 <kbd>Shift + X</kbd> 键来切换图层可见性。

<span style='color: hotpink'>*锁定*</span>：如果图层被锁定 ![锁定图层图标](./layers/locked-layer.png)，你就无法在其上绘制。默认情况下，所有图层都是解锁/可编辑的 ![可编辑图层图标](./layers/editable-layer.png)。

<span style='color: hotpink'>*连续*</span>：此选项用于指示为该特定图层创建 [cel](./cel.md) 时，你偏好哪种类型。
更多信息请参见[连续图层](./continuous-layers.md)部分。

### 常用操作

* [添加新图层](./new-layer.md)
* [移动图层](./move-layers.md)
* [复制图层](./copy-layers.md)

## 背景图层

背景图层是一个不透明图层（没有 alpha/透明成分），无法移动。当你在*文件 > 新建*窗口中选择不透明颜色，或打开一个不包含 alpha 成分的文件（例如 `.png` 文件）时，默认会创建它。

一个精灵图只能包含一个背景图层，并且它始终位于[时间轴](./timeline.md)中图层堆栈的底部。

当你选中背景图层的一部分并将其清除（使用*编辑 > 清除*菜单）时，选区将被当前的[背景色](./color-bar.md)清除。

## 透明图层

所有带有 alpha 通道的图层都称为透明图层。在同一个精灵图中可以有多个透明图层。可以使用[时间轴](./timeline.md)按需要堆叠它们。并且可以使用[移动工具](./move-tool.md) ![移动工具图标](./tools/move-tool.png) 来移动这些图层。

当选中透明图层的一部分并将其清除（使用 *编辑 > 清除*菜单）时，选区将被[透明色](./transparent-color.md)清除。

使用 *图层 > 新建 > 新建图层*菜单或 <kbd>Shift + N</kbd> 来创建一个新的透明图层。

## 从图层转为背景

如果没有背景图层，可以使用 *图层 > 转换为 > 背景* 菜单将任何透明图层转换为背景。所有透明像素将被当前的[背景色](./color-bar.md#background-color)填充。

> 以前，在 Aseprite v1.2 中，此选项为*图层 > 从图层创建背景*

## 从背景转为图层

如果你想将背景转换为透明图层（例如，因为你想用[移动工具](./move-tool.md) ![移动工具图标](./tools/move-tool.png) 移动它)，可以使用 *图层 > 转换为 > 图层* 菜单。

> 以前，在 Aseprite v1.2 中，此选项为*图层 > 从背景创建图层*

## 图层组

可以[将图层分组](./layer-group.md)，以便将一组图层作为一个
单元来处理。

## 瓦片贴图图层

从 **Aseprite v1.3** 开始，可以通过 *图层 > 新建 > 新建瓦片贴图图层* 菜单或使用 <kbd>Space + N</kbd> 来创建[瓦片贴图图层](./tilemap.md)。也可以通过任何常规透明图层使用 *图层 > 转换为 > 瓦片贴图* 来创建（瓦片将根据当前的网格设置创建）。

## 从选区新建图层

* <kbd>Ctrl + J</kbd> 或 <kbd>⌘ J</kbd>：复制[选区](./selecting.md)并从中创建一个新图层
* <kbd>Ctrl + Shift + J</kbd> 或 <kbd>⇧ ⌘ J</kbd>：剪切[选区](./selecting.md)并从中创建一个新图层

---

**另请参阅**

[时间轴](./timeline.md) |
[连续图层](./continuous-layers.md) |
[移动工具](./move-tool.md)