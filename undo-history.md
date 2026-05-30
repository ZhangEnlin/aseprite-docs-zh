# 撤销历史

撤销历史是 sprite 状态的列表。每次对 sprite 执行操作时，都会保存一个新状态。当你使用 *编辑 > 撤销*（<kbd>Ctrl+Z</kbd>）或 *编辑 > 重做*（<kbd>Ctrl+Y</kbd>）时，你正在这个状态列表中前后移动。

撤销历史的内存限制可以在[首选项](./preferences.md#undo)菜单中更改。

## 撤销历史菜单

![撤销历史菜单](./undo-history/undo-history.png)

撤销历史菜单显示了 sprite 的撤销历史。可以通过 *编辑 > 撤销历史* 访问。

点击某个条目会将 sprite 的当前状态更改为所点击的那一个状态。在对 sprite 进行操作（创建新条目）后，根据是否启用非线性撤销历史设置，新状态要么添加到前面的状态前面，要么替换掉前面的状态。

### 非线性撤销历史

默认情况下，撤销历史是线性运作的：当使用撤销（将当前 sprite 状态向后移动一个条目）时，下一个操作将擦除所有可以被重做的步骤。如果启用了这个非线性历史并使用了撤销，下一个操作将会将新的 sprite 状态添加到列表中，同时保留旧状态不变。

非线性撤销历史可以在[首选项](./preferences.md#undo)菜单中打开/关闭。

| 启用 | 禁用 |
| - | - |
| ![启用非线性撤销历史的示例](./undo-history/non-linear-on.gif) | ![禁用非线性撤销历史的示例](./undo-history/non-linear-off.gif) |

---

**另请参阅**

[首选项](./preferences.md#preferences) |
[编辑菜单](./edit-menu.md#edit-menu)