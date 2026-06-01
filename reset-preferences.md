# 重置首选项

Aseprite 的首选项存储在[配置文件夹](./preferences-folder.md)中的一个 `aseprite.ini` 文件里。

通过 *编辑 > 首选项 > 定位配置文件* 来访问此文件夹。要重置所有配置，可以关闭 Aseprite 并删除 `aseprite.ini` 所在位置的所有文件：

![首选项文件夹中的文件](./preferences/preffiles.png)

如果你无法启动程序，以下是各平台上手动重置首选项的步骤。



## 在 Windows 上

1. 关闭 Aseprite
1. 按下 <kbd>Windows 键 + R</kbd>（或 `开始菜单 > 运行...` 选项）。这将显示运行程序的对话框。然后输入以下内容并按 `Enter` 键。

   ```bash
   %AppData%\Aseprite
   ```

1. 删除该文件夹中的文件（主要是 `aseprite.ini`）
1. 重启 Aseprite



## 在 macOS 上

1. 关闭 Aseprite

1. 打开 Spotlight 搜索（<kbd>⌘ + 空格键</kbd>）

1. 使用 <kbd>⌘ V</kbd> 粘贴一下内容，并按 Enter 键：

   ```bash
   ~/Library/Application Support/Aseprite
   ```

   ![Spotlight 搜索](./preferences/spotlight.png)

1. 删除该文件夹中的文件（主要是 `aseprite.ini`）

1. 重启 Aseprite



## 在 Linux 上

1. 关闭 Aseprite
1. 打开终端
1. 输入：

   ```bash
   xdg-open ~/.config/aseprite
   ```

1. 删除该文件夹中的文件（主要是 `aseprite.ini`）
1. 重启 Aseprite

---

**另请参阅**

[故障排除](./troubleshooting.md) |
[首选项](./preferences.md) |
[首选项文件夹](./preferences-folder.md)