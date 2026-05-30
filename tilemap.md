# Tilemap

自 **Aseprite v1.3** 起，可以使用 *tileset* 创建 *tilemap*。

什么是 **tilemap**？Tilemap 是一种特殊的图层，画布上的每个网格单元格都引用其 *tileset* 中的一个 tile（一个小图像）。可以通过 *图层 > 新建 > 新建 Tilemap 图层* 或按 <kbd>Space + N</kbd> 来创建新的 tilemap。

什么是 **tileset**？顾名思义，它是一组 tile 的集合，就像颜色调色板是一组颜色的集合一样。每个 tile 都有一个索引，并且可以在画布上每个 tilemap 网格单元格中的不同位置重复使用。

示例：

![Tilemap 示例](./tilemap/tilemap-example.png)

## 与索引颜色的相似之处

我们可以将 tilemap 与[索引图像](./color-mode.md#indexed)进行比较：

| Tilemap | 索引颜色
| ------- | --------
| **Tile**: 一个小图像，可以在 Tilemap 图层的多个位置重复使用 | **调色板条目**: 一种 RGBA 颜色，可以在索引图像的多个位置重复使用。
| **Tileset**: 相同大小的 tile 的集合。 | **调色板**: RGBA 颜色（调色板条目）的集合。
| **Tilemap 图层**: 一个二维图像，其中每个像素都是一个“tile 索引”，引用 tileset 中的 tile。每个 tilemap 都关联一个特定的 tileset。 | **索引图像**: 一个二维图像，其中每个像素通过索引引用一个调色板条目。
| **Tile 索引**: 从 0 到 N 的值（其中 N = tileset 中的 tile 数量，0 是 *空 tile*） | **调色板索引**: 从 0 到 N-1 的值（其中 N = 调色板条目的数量）

## 模式

当你在 Tilemap 图层中时，有 2 种主要模式，可以按 <kbd>Space + Tab</kbd> 在这些模式之间切换：

| 模式 |   | 描述
| ---- | - | ----
| *绘制像素* | ![](./tilemap/pixels-mode.png) |  在每个 tile 中绘制像素，即修改 tile 的内容/像素。这类似于修改常规图层（你修改像素）。 |
| *绘制 Tiles* | ![](./tilemap/tiles-mode.png) | 直接放置/获取 tile（不修改 tile 内容，而是修改 tilemap 信息） |

当我们在 tilemap 中绘制像素时，我们正在修改每个 tile 的内容，但有三种特殊模式指示我们应该如何处理 tile 之间的这些修改：

| 绘制像素  |   | 描述
| --------- | - | ----
| ![](./tilemap/manual-mode.png) | *手动* | 它将修改每个 tile 的内容，而不重新排序 tileset。如果你已经有一个固定的 tileset 并且不想改变每个 tile 在 tileset 中的位置，此模式很有用。<kbd>Space + 1</kbd>
| ![](./tilemap/auto-mode.png) | *自动* | 它在你绘制时尝试创建新 tile（或重用现有 tile），并且如果未在任何引用该 tileset 的 tilemap 中找到未使用的 tile，则会删除它们。这是默认模式，因为它尝试模拟常规图层，自动调整整个 tileset。<kbd>Space + 2</kbd>
| ![](./tilemap/stack-mode.png) | *堆叠* | 它将为对现有 tile 进行的每次修改创建一个新 tile，而不修改现有 tile，并堆叠所有新 tile。<kbd>Space + 3</kbd>

---

**另请参阅**

[颜色模式](./color-mode.md) |
[图层](./layers.md)