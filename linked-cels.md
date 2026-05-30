# 链接 Cel

要创建链接 cel，必须在[连续图层](./continuous-layers.md)中[复制 cel](./copy-cels.md)（即，一个带有连续图标 ![连续图标](./continuous-layers/continuous-layer.png) 的图层)。

当两个或连续多个 cel 需要共享同样的图像时，就可以使用链接 cel 。链接的 cel 在[时间轴](./timeline.md)中如下所示：

![链接 Cel](./linked-cels/linked-cels.png)

创建好链接 cel 之后，修改其中一个 cel 时，所有链接的 cel 都会被修改。通过这种方式，可以将相同的更改传播到多个帧中。

例如，现在有一个静态背景：月亮，那它应该使用链接cel，这样只需在一个 cel 中进行更改，就能在整个动画中看到更改效果。



## 取消链接 Cel

有一种取消链接 cel 的方法，在时间轴中使用右键点击并选择*取消链接*选项：

![取消链接 Cel](./linked-cels/unlink-cels.gif)

取消链接的 cel 将包含它们自己的图像副本。修改它们，这些更改将不会传播到其他 cel。

---

**另请参阅**

[连续图层](./continuous-layers.md)