# 故障排除

如果你在启动 Aseprite 时遇到问题（例如，启动后立即关闭），可以尝试：

1. [重置你的首选项](./reset-preferences.md)
1. 使用 [debug 选项](./debug.md)，这将生成一个 `Aseprite-v1.2-DebugOutput.txt` 文件
1. 仅限 Windows：检查生成的 `Aseprite-v1.2-DebugOutput.txt` 文件的最后一行是否为：`PEN: Wintab library loaded`。如果是这种情况，请尝试[禁用 Wintab](./wintab.md)。
1. 在其他情况下，请通过 [support@aseprite.org](mailto:support@aseprite.org) 联系我们，并附上 `Aseprite-v1.2-DebugOutput.txt` 文件。

也可以尝试在以下位置寻找你的问题：

* [Aseprite 社区](https://community.aseprite.org)
* [Steam 综合讨论论坛](http://steamcommunity.com/app/431730/discussions/0/)
* [Steam Bug 报告论坛](http://steamcommunity.com/app/431730/discussions/2/)
* [GitHub 上已关闭的 Bug](https://github.com/aseprite/aseprite/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aclosed%20%20label%3Abug)

## 崩溃/数据丢失

如果发生崩溃，你也许可以[恢复一些 Sprite](./data-recovery.md)。

## 数位板问题

如果你的数位板（或数位板的压感）无法使用，请查看[数位板](./tablet.md)页面。

## macOS 渲染问题

Aseprite 在 macOS 上使用异步渲染 ([CALayer's drawsAsynchronously](https://developer.apple.com/documentation/quartzcore/calayer/1410974-drawsasynchronously?language=objc))。自 Aseprite v1.2.20 起，如果你遇到一些问题，例如屏幕上出现黑色矩形，可以禁用此功能（但无论如何，如果你正在使用像 Display P3 这样的[颜色配置文件](./color-profile.md)，性能将显著下降）。

要禁用此功能：
1. 关闭 Aseprite
2. 在[首选项文件夹](./preferences-folder.md)中打开 `aseprite.ini` 文件
3. 搜索 `[general]` 部分并添加此选项 `osx_async_view = false`
   ```text
   [general]
   osx_async_view = false
   ```

4. 保存文件并启动 Aseprite

---

**另请参阅**

[重置首选项](./reset-preferences.md) |
[数据恢复](./data-recovery.md) |
[调试](./debug.md) |
[数位板](./tablet.md)