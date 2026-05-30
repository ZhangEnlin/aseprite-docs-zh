# 选择

你可以使用其中一个选择工具来选择 Sprite 的某些部分，
例如矩形选框工具 ![Marquee Tool Icon](./tools/marquee-tool.png)（按 <kbd>M</kbd> 键），
然后[移动它](./move-selection.md)或[变换它](./transformations.md)
（[缩放](./resize.md)、[旋转](./rotate.md)等）。当你选择了
Sprite 的一部分时，你会看到
[蚂蚁线](https://en.wikipedia.org/wiki/Marching_ants)效果：

![蚂蚁线](./selecting/marching-ants.gif)

当你进行选择时，你选择的是活动的[cel](./cel.md)，
因此所有变换仅会应用于该特定的 cel。

## 添加/减去/交集

在[上下文栏](./context-bar.md)中，你可以找到一组修改器，
用于更改对所选区域执行的操作：![修改器](./selecting/modifiers.png)

默认情况下，当你按下鼠标左键，拖动它，然后
松开时，它将替换整个选择区域。但你可以
使用其他选项修改此行为（每个选项都有一个键盘
快捷键）：

* ![替换选择](./selecting/replace-selection.png)：默认操作，用新选择替换整个选择区域（拖动鼠标左键）
* ![添加到选择](./selecting/add-selection.png)：在现有选择和新选择之间创建并集（拖动鼠标左键 + 按住 <kbd>Shift</kbd> 键）
* ![从选择中减去](./selecting/subtract-selection.png)：从现有选择中减去新选择（拖动鼠标左键 + 按住 <kbd>Alt + Shift</kbd> 键，或者：拖动鼠标右键）
* ![与选择交集](./selecting/intersect-selection.png)：将现有选择与新选择相交（拖动鼠标左键 + 按住 <kbd>Ctrl + Shift</kbd>）

可以从 [*编辑 > 键盘快捷键 > 操作修饰键*](./keyboard-shortcuts.md#action-modifiers) 自定义这些键。

## 选择内容

你可以选择：
- 整个 Sprite 画布，使用 *选择 > 全部* (<kbd>Ctrl + A</kbd> 或 <kbd>⌘ A</kbd>)
- 活动 [cel](./cel.md) 的边界，使用 *编辑 > 变换* (<kbd>Ctrl + T</kbd> 或 <kbd>⌘ T</kbd>)
- 活动帧的内容（非透明像素），在图层上使用 <kbd>Ctrl + 鼠标左键单击</kbd>（可以应用添加/减去/交集修改器的键盘快捷键）

## 取消选择和重新选择

你可以使用 *选择 > 取消选择* (<kbd>Ctrl + D</kbd> 或 <kbd>⌘ D</kbd>) 隐藏当前选择。然后你可以使用
*选择 > 重新选择* (<kbd>Ctrl + Shift + D</kbd> 或 <kbd>⇧ ⌘ D</kbd>) 使其再次出现。

## 反选

你可以使用
*选择 > 反选* (<kbd>Ctrl + Shift + I</kbd> 或 <kbd>⇧ ⌘ I</kbd>) 反转选择区域。

---

**另请参阅**

[变换](./transformations.md) |
[移动选择](./move-selection.md)