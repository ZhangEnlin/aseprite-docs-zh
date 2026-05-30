# 文件

Aseprite 使用多种文件格式来保存和加载不同的信息。你需要知道的主要一点是，当你使用 [*文件 > 保存* 菜单](./save.md)时，你的作品会保存在你的本地计算机上。这里不涉及“云端”或远程服务器功能，因此请记得备份你的作品，或者使用类似 Dropbox、Drive、OneDrive 等云文件夹服务，如果你想保证作品安全或在多台计算机之间共享的话。

## .aseprite

Aseprite 有自己的文件格式来[保存](./save.md)你的作品：`.aseprite` 文件（或 `.ase`，[两者是一样的](/faq/#is-there-any-difference-between-ase-and-aseprite-files)）。
当你将精灵保存为 `.aseprite` 文件时，你将能够完整保留所有信息（[颜色模式](./color-mode.md)、[图层](./layers.md)、[帧](./animation.md)、调色板、[标签](./tags.md)、[切片](./slices.md)等）。

通常，你会想要[导出你的作品](./exporting.md)为其他格式（`.png`、`.gif` 等）用于发布目的或在游戏中使用你的素材。但请将原始的 `.aseprite` 文件保存在安全的地方，以便在需要时修改精灵。

这些文件的内部结构在 [Aseprite 文件格式规范](https://github.com/aseprite/aseprite/blob/main/docs/ase-file-specs.md)中有描述。

## .aseprite-extension

可以创建 `.aseprite-extension` 格式的扩展，该格式是一个 `.zip` 文件，其中包含一组特定的文件，更多信息请参阅[扩展](./extensions.md)页面中的[文件内容](./extensions.md#file-content)部分。

## .lua

在 *文件 > 脚本 > 打开脚本文件夹* 文件夹中用于[脚本目的](./scripting.md)的脚本。

## 首选项

[首选项](./preferences.md)保存在[首选项文件夹](./preferences-folder.md)内的多个文件中：

### aseprite.ini

在 *编辑 > 首选项* 对话框中指定的主要选项/配置位于此文件中。

### user.aseprite-brushes

自定义画笔存储在此文件中（一个 XML 文件）。未来我们将提供更多选项来在不同文件之间导出/导入画笔。

### user.aseprite-keys

你自定义的键盘快捷键存储在此文件中，当你导出/导入键盘快捷键时，也使用相同的 `.aseprite-keys` 文件格式（一个 XML 文件）。

### sessions

`sessions` 文件夹包含一些用于[数据恢复过程](./data-recovery.md)的备份文件。

---

**另请参阅**

[保存](./save.md) |
[导出](./exporting.md) |
[首选项](./preferences.md) |
[Aseprite 文件格式规范](https://github.com/aseprite/aseprite/blob/main/docs/ase-file-specs.md)