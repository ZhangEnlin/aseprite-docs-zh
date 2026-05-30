# 选区

可以使用其中一个选区工具来框选 Sprite 的某些部分，例如矩形选框工具 ![Marquee Tool Icon](./tools/marquee-tool.png)（按 <kbd>M</kbd> 键），
然后 [移动它](./move-selection.md) 或 [变换它](./transformations.md)（[缩放](./resize.md)、[旋转](./rotate.md) 等）。当你选择了 Sprite 的一部分时，你会看到 [蚂蚁线](https://en.wikipedia.org/wiki/Marching_ants) 效果：
![蚂蚁线](./selecting/marching-ants.gif)

当进行选区操作时，生效的是当前活动的[cel](./cel.md)，因此所有变换仅会应用于该 cel。

## 添加/减去/交集

在[上下文栏](./context-bar.md)中，可以找到一组修改器，用于更改对所选区域执行的操作：![修改器](./selecting/modifiers.png)

默认情况下，当你按下鼠标左键，拖动它，然后松开时，它将替换整个选区。但可以使用其他选项修改此行为（每个选项都有一个键盘快捷键）：

* ![替换选区](./selecting/replace-selection.png)：默认操作，用新选区替换整个选区（拖动鼠标左键）
* ![添加到选区](./selecting/add-selection.png)：在现有选区和新选区之间创建并集（拖动鼠标左键 + 按住 <kbd>Shift</kbd> 键）
* ![从选区中减去](./selecting/subtract-selection.png)：从现有选区中减去新选区（拖动鼠标左键 + 按住 <kbd>Alt + Shift</kbd> 键，或者：拖动鼠标右键）
* ![与选区交集](./selecting/intersect-selection.png)：将现有选区与新选区相交（拖动鼠标左键 + 按住 <kbd>Ctrl + Shift</kbd>）

可以从 [*编辑 > 键盘快捷键 > 操作修饰键*](./keyboard-shortcuts.md#action-modifiers) 自定义这些键。

## 选择内容

可以选择：
- 整个 Sprite 画布，使用 *选择 > 全部* (<kbd>Ctrl + A</kbd> 或 <kbd>⌘ A</kbd>)
- 活动 [cel](./cel.md) 的边界，使用 *编辑 > 变换* (<kbd>Ctrl + T</kbd> 或 <kbd>⌘ T</kbd>)
- 活动帧的内容（非透明像素），在图层上使用 <kbd>Ctrl + 鼠标左键单击</kbd>（可以应用添加/减去/交集修改器的键盘快捷键）

## 取消选区和重新选区

可以使用 *选择 > 取消选择* (<kbd>Ctrl + D</kbd> 或 <kbd>⌘ D</kbd>) 隐藏当前选择。然后可以使用 *选择 > 重选* (<kbd>Ctrl + Shift + D</kbd> 或 <kbd>⇧ ⌘ D</kbd>) 使其再次出现。

## 反选

可以使用 *选择 > 反选* (<kbd>Ctrl + Shift + I</kbd> 或 <kbd>⇧ ⌘ I</kbd>) 反转选区。

---

**另请参阅**

[变换](./transformations.md) |
[移动选区](./move-selection.md)