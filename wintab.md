# Wintab

Wintab (`WinTab32.dll`) 是一个由 Wacom 创建的古老 API，用于让类似数位板的设备与 Windows 程序通信。在 Windows 8 之前，这是用于访问 Wacom 和其他品牌数位板压力信息的“事实上的”标准。从 Windows 8 开始，Microsoft 引入了新的官方 API：Pointer API/Windows Ink。

从 **Aseprite v1.2.34**（和 **v1.3-beta12**）开始，由于我们收到了大量与有缺陷的第三方 `WinTab32.dll` 相关的崩溃报告，
我们已默认切换到 Windows Pointer API。（Wintab 选项仍然在[数位板选项](./tablet.md)中可用。）

在 Aseprite 的早期版本中，我们最初尝试加载此 Wintab 库，但这可能会导致程序随机崩溃。有时可以通过重新安装驱动程序、重启 Windows、在[数位板选项](./tablet.md)中使用 Pointer API，或者仅仅通过 *编辑 > 首选项 > 数位板*（或在旧版本中通过 *编辑 > 首选项 > 实验性*）禁用 Wintab 使用来解决这个问题：

![不要加载 WinTab 驱动](./wintab/disable-wintab.png)

## Aseprite 无法启动

如果你甚至无法启动程序，可以使用 `-disable-wintab` 参数（从 Aseprite v1.2 起可用）执行 Aseprite：

```bash
"C:\Program Files\Aseprite\Aseprite.exe" -disable-wintab
```

这将避免加载 `WinTab32.dll` 文件。你的数位板可能无法正常工作，但至少 Aseprite 可以执行并使用你的鼠标/触控板（或者可以尝试 [Windows Pointer API](./tablet.md)）。

## Steam

在 Steam 上，可以在 Aseprite 启动选项中添加 `-disable-wintab` 选项：

1.  在你的 Steam 库中右键点击 Aseprite 并打开其“属性”：

    ![打开 Aseprite 属性](./steam/steam-1-open-properties.png)

2.  点击“设置启动选项”按钮：

    ![打开启动选项](./steam/steam-2-launch-options.png)

3.  添加 `-disable-wintab` 选项并按下“确定”：

    ![添加 disable wintab 选项](./steam/steam-3-disable-wintab.png)

---

**另请参阅**

[数位板](./tablet.md) |
[故障排除](./troubleshooting.md)