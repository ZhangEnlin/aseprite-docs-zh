# 扩展

自 [Aseprite v1.2-beta10](https://www.aseprite.org/release-notes/12/#aseprite-v1-2-beta10) 起，可以向 Aseprite 添加/移除扩展。扩展以 `.aseprite-extension` / `.zip` 文件的形式分发，可以通过 *编辑 > 首选项 > 扩展* （<kbd> Ctrl + K </kbd> 或 <kbd>⌘ K</kbd> / <kbd>⌘ ,</kbd>）来管理它们：

![首选项中的扩展](./extensions/extensions.png)

## 添加/移除扩展

在 *编辑 > 首选项 > 扩展* 中有一个“添加扩展”按钮。可以使用它来选择一个 `.aseprite-extension` 或 `.zip` 文件。安装扩展后，它将被解压到你的[配置目录](./preferences-folder.md)内的 `extensions` 子文件夹中。

> [!tip]
>
> [Aseprite v1.3.17.1](https://www.aseprite.org/release-notes/#aseprite-v1-3-17-1) 及之后的版本，可以直接拖动插件到 **首选项** 对话框（上图所示）里完成安装



## 文件内容

扩展/插件本质上与 `.zip` 文件完全相同，但可以将文件扩展名重命名为 `.aseprite-extension`，这样用户就可以在 Windows 资源管理器或 macOS Finder 中双击它。

- `.zip` 文件的内容取决于你想创建的扩展类型，但至少必须包含一个文件：`package.json` 文件。

- `.aseprite-extension` 文件的结构取决于扩展的类型：

  * [按键](./extensions/keys.md)

  * [调色板](./extensions/palettes.md)

  * [语言](./extensions/languages.md)

  * [主题](./extensions/themes.md)

  * [抖动矩阵](./extensions/dithering-matrices.md)

  * [带脚本的插件](https://github.com/aseprite/api/blob/master/api/plugin.md#plugin)