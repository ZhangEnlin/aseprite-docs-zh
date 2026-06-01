# 连续图层

连续图标 ![断开图层图标](./continuous-layers/broken-layer.png) 指示了在复制 [Cel](./cel.md) 时产生的行为。例如[新建帧](./new-frame.md)、[复制帧](./copy-frames.md) 或 [复制 Cel](./copy-cels.md)。总结有以下两种行为：

1. ![普通图层图标](./continuous-layers/broken-layer.png) 当前图层为普通图层（具有不连续的 Cel ）：新创建的 Cel 将是不链接的（ Cel 本身被复制)。
1. ![连续图层图标](./continuous-layers/continuous-layer.png) 当前图层是连续的：新 Cel 以[链接方式](./linked-cels.md)创建。

通常，对于[背景图层](./layers.md#background-layer)（包含静态内容），推荐使用连续的 Cel ，而对于每个帧都有不同 Cel 的图层，则推荐使用不连续模式：

![连续图层与普通图层](./continuous-layers/cont-vs-dis.png)

此选项可以根据你正在处理的具体情况进行切换。修改该选项不会改变已有的 Cel ，因此它只影响未来的操作。

---

**另请参阅**

[链接 Cel](./linked-cels.md) |
[图层](./layers.md) |
[新建帧](./new-frame.md) |
[复制帧](./copy-frames.md) |
[时间轴](./timeline.md)