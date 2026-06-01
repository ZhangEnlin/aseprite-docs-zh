# 首选项文件夹

Aseprite 的配置存储在个人用户配置目录中的多个文件中：

![首选项文件夹中的文件](./preferences/preffiles.png)

可以通过 *编辑 > 首选项 > 定位配置文件* 选项访问此文件夹。

不过，也可以根据你的平台，通过不同方式手动找到该文件夹：

## 在 Windows 上

按 <kbd>Windows 键 + R</kbd>（或 `开始菜单 > 运行...` 选项），然后输入以下内容并按 `Enter` 键：

```bash
%AppData%\Aseprite
```



## 在 macOS 上

打开 Spotlight 搜索（<kbd>⌘ 空格</kbd>），然后使用 <kbd>⌘ V</kbd> 粘贴以下文本并按 <kbd>Enter</kbd> 键：

```bash
~/Library/Application Support/Aseprite
```

   ![Spotlight 搜索](./preferences/spotlight.png)

## 在 Linux 上

打开终端，粘贴以下命令并按 <kbd>Enter</kbd> 键

```bash
xdg-open ~/.config/aseprite
```

## 特殊配置

从 Aseprite v1.2.16.3 开始，出于测试目的，可以使用指向其他文件夹的 `ASEPRITE_USER_FOLDER` [环境变量](https://en.wikipedia.org/wiki/Environment_variable) 来重新配置首选项文件夹的位置。

---

**另请参阅**

[首选项](./preferences.md) |
[重置首选项](./reset-preferences.md)