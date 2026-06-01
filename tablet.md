# 数位板

## Windows

自 Windows 8 起，Microsoft 引入了一个新的 API 来让你的数位板与 Windows 程序配合使用：Pointer API（指针 API）。

自 Aseprite v1.2.19.1 起，可以配置偏好使用的 API：

![数位板部分](./tablet/tablet.png)

* *Windows 8/10 Pointer API*：此选项对大多数现代设备可能就足够了，可以试试你的数位板在此选项下效果如何（使用此选项可能比使用 Wintab 效果更好）
* *[Wintab](./wintab.md)*：这是目前支持在旧系统（Windows Vista/7）和旧设备上实现压感的默认选项。
* *Wintab（直接数据包处理）*：此选项在某些设备上可能效果不佳，但在其他设备上可能有助于避免数据包丢失并获得更平滑的笔触。

按下 *确定*/*应用* 按钮将立即更改数位板设置，无需重启程序。

## Linux/X11

在 X11 上，数位板/触控笔/笔设备似乎是通过设备名称/品牌名称来检测的，而不是通过设备功能。

有一些预定义的 ID 用于检测触控笔，但这可能还不够（如 [#3176](https://github.com/aseprite/aseprite/issues/3176) 所述）

如果 Aseprite 检测不到你的笔的压感，自 **Aseprite v1.2.35** 起，可以尝试执行以下步骤：

1. 关闭 Aseprite
2. 在终端/控制台中运行 `xinput --list`
3. 检查输出，看看哪个设备可能与你的触控笔相关（[输出示例](https://github.com/aseprite/aseprite/issues/3176#issuecomment-1111799083)）
4. 在[首选项文件夹](./preferences-folder.md)中打开 `aseprite.ini` 文件
5. 搜索 `[general]` 部分，并在 `x11_stylus_id` 选项中添加你的触控笔的名称（该名称必须与 `xinput --list` 输出中
   第一列显示的名称一致）：
   
   ```bash
   [general]
   x11_stylus_id = Your Stylus Name
   ```
6. 保存文件并启动 Aseprite

> [!tip]
>
> 如果这符合你当前的情况，请在 [#3176](https://github.com/aseprite/aseprite/issues/3176) 中添加一条新评论，说明你的设备名称，以告知我们。

---

**另请参阅**

[Wintab](./wintab.md) |
[故障排除](./troubleshooting.md)