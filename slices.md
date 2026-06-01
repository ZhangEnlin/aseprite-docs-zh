# 切片

使用切片工具 ![Slice tool icon](./tools/slice-tool.png)（<kbd>Shift + C</kbd> 键），可以指示 Sprite 的区域，并为该区域指定一个名称/标签，以及一些用户定义的额外信息。支持指定[9-slice](https://en.wikipedia.org/wiki/9-slice_scaling)/9-patches信息。

使用此工具，可以：

1. 通过按住鼠标按钮、拖动鼠标，然后释放按钮来标记一个矩形区域以创建新的切片。
1. 如果标记的矩形接触到现有的切片，那些切片将被选中。
1. 可以拖放一组选定的切片，将它们移动到其他位置。或者可以从角落或边缘拖动来调整整组切片的大小。
1. 选择一些切片后，可以按 Delete 键或使用 *编辑 > 删除* 菜单选项将其删除。
1. 双击一个切片，你将看到[切片属性](#slice-properties)对话框。

## 切片属性

如果你双击一个切片，你将看到其属性：

![切片属性对话框](./slices/properties.png)

在这里可以指定：

1. 切片在画布中的边界
1. 一个 9-slices 属性，用于指定一个内部矩形，将边界细分为子切片
1. 一个轴心点，用于指定 Sprite 在切片内的中心/基准位置

## 导出切片

使用 [--split-slice 选项](cli.md/#split-slices) 将每个切片导出为不同的 Sprite。

或使用 [--data 选项](cli.md/#data) 或 *文件 > 导出 Sprite Sheet*菜单选项，并勾选 JSON 输出，将切片信息导出到一个 Sprite Sheet JSON 中。以下是导出数据的示例：

```json
{ ...
 "meta": {
  ...
  "slices": [
   { "name": "Button-patch",
     "color": "#0000ffff",
     "keys": [{ "frame": 0,
                "bounds": {"x": 118, "y": 118, "w": 20, "h": 21 },
                "center": {"x": 5, "y": 5, "w": 10, "h": 9 } }] }
  ]
}
```


**另请参阅**

[绘制](./drawing.md)