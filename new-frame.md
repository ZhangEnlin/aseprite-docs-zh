# 新建帧

可以通过以下方式添加帧：

* *帧 > 新建帧*（<kbd>Alt + N</kbd>）：在下一个位置创建当前帧的副本。
* *帧 > 新建空白帧*（<kbd>Alt + B</kbd>）：创建一个新的空白帧。（所有
   [透明图层](./layers.md#transparent-layers) 带有空
   cel，而[背景图层](./layers.md#background-layer)则
   用当前的背景色清除。）
* *帧 > 复制 Cel*（<kbd>Alt + D</kbd>）：复制当前 cel，或
   创建当前时间轴选区的副本，放到下一个
   位置/帧。
* *帧 > 复制链接 Cel*（<kbd>Alt + Shift + D</kbd> 或 <kbd>Alt + M</kbd>）：创建
  当前 cel（或当前时间轴选区）的链接到
  下一个位置/帧。

状态栏中的小 `+` 号可用于添加新帧（就像按 <kbd>Alt + N</kbd> 一样）：

![新建帧按钮](./new-frame/new-frame-button.png)

## 新建帧

使用*视图 > 新建帧*（<kbd>Alt + N</kbd> 键）可以创建一个新帧，它
是当前帧的精确副本。对于[连续图层](./continuous-layers.md)
cel 将被[链接](./linked-cels.md)。

## 新建空白帧

当使用 <kbd>Alt + B</kbd> 添加一个新的空白帧时，所有
[透明图层](./layers.md#transparent-layers) 将不
包含 cel，而[背景图层](./layers.md#background-layer)
将被[背景色](./color-bar.md#background-color)清除。

当你在动画末尾之后[移动](./move-cels.md)或
[复制 cel](./copy-cels.md) 时，也会创建空白帧。

## 复制 Cel

一些信息：[What is the difference between ‘duplicated cell’ and ‘duplicated linked cell’](https://community.aseprite.org/t/913)