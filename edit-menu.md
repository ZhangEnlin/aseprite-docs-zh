# 编辑菜单

**编辑菜单**包含用于修改当前精灵以及 Aseprite 设置的选项/命令。

## 撤销、重做和撤销历史

* **撤销**：撤销上一步操作。*快捷键：* <kbd>Ctrl + Z</kbd>。
* **重做**：重做上一步操作。*快捷键：* <kbd>Ctrl + Y</kbd>。
* **撤销历史**：请参阅[撤销历史](./undo-history.md#undohistory)部分。

## 剪切、复制和粘贴

* **剪切**：剪切活动[选区](./selecting.md#selecting)的内容。*快捷键：* <kbd>Ctrl + X</kbd>。
* **复制**：复制选中的内容、[图层](./layers.md#layers)、[Cel](./cel.md#cel) 或帧；例如，如果选中了一个图层，该图层将被复制。*快捷键：* <kbd>Ctrl + C</kbd>。
* **合并复制**：为每个可见图层复制选中的内容，合并为一个图像。*快捷键：* <kbd>Ctrl + Shift + C</kbd>。
* **粘贴**：粘贴剪贴板内容（可以是图层、Cel、精灵的一部分等）。*快捷键：* <kbd>Ctrl + V</kbd>。
* **特殊粘贴**：
    * *粘贴为新精灵*：粘贴为一个新的[精灵](./sprite.md#spritestructure)。
    * *粘贴为新图层*：粘贴为一个新的图层。
    * *粘贴为新参考图层*：粘贴为一个新的[参考图层](./reference-layer.md#referencelayer)。
* **删除**：删除选中的内容、图层、Cel 或帧。*快捷键：* <kbd>Del</kbd>。

## 填充与描边

* **填充**：使用[前景色](./color-bar.md#foreground-color)填充活动选区。*快捷键：* <kbd>F</kbd>。
* **描边**：使用前景色勾勒活动选区内部的轮廓。*快捷键：* <kbd>S</kbd>。

## 旋转与翻转

* **旋转**：请参阅[旋转画布](./rotate-canvas.md#rotate-canvas)部分。
* **水平翻转**：水平翻转精灵或选区。*快捷键：* <kbd>Shift + H</kbd>。
* **垂直翻转**：垂直翻转精灵或选区。*快捷键：* <kbd>Shift + V</kbd>。
* **变换**：选择 Cel 内容。*快捷键：* <kbd>Ctrl + T</kbd>。
* **移位**：将选区的像素向选定方向移动一次。移位时，选区末端的像素将循环回绕。

![移位示例](./edit-menu/shift.gif)

## 新建画笔和从选区新建精灵

* **新建画笔**：创建一个新画笔。请参阅[画笔](./brushes.md#custom-pattern-brushes)部分。*快捷键：* <kbd>Ctrl + B</kbd>。
* **从选区新建精灵**：从选区内容创建一个新精灵。请参阅[新建精灵](./new-sprite.md#new-sprite-from-selection)部分。*快捷键：* <kbd>Ctrl + Alt + N</kbd>。

## 替换颜色

请参阅[替换颜色](./replace-color.md#replace-color)部分。

## 反相

反转选区或 Cel 中的所有颜色。

该菜单底部有几个重要的按钮：

* *R*、*G*、*B* 和 *A* 按钮控制是否应反转某个分量，例如：*R* 按钮被选中，因此 *R*（红色）分量可以被反转。
* 底部按钮控制反相应应用于活动的时间轴选区（*Selected*）还是精灵中的所有 Cel （*All*）。如果[选中了精灵的一部分](./selecting.md#selecting)：在 *Selected* 模式下，反相只会应用于所选时间轴元素的选中内容；在 *All* 模式下，反相将应用于精灵所有 Cel 的选中内容。

![分量按钮和选择按钮的图像](./edit-menu/invert-buttons.png)

## 调整

请参阅[调整](./adjustments.md#adjustments)部分。

## FX

请参阅 [FX](./fx.md#fx) 部分。

## 插入文本

请参阅[文本工具](./text-tool.md#text-tool-&-insert-text)部分。

## 键盘快捷键

请参阅[键盘快捷键](./keyboard-shortcuts.md#keyboard-shortcuts)部分。

## 首选项

请参阅[首选项](./preferences.md#preferences)部分。

---

**另请参阅**

[菜单栏](./menu-bar.md#menu-bar)