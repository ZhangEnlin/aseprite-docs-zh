# 数据恢复

当 Aseprite 运行时，它会保存一些临时数据，以便在你的计算机（或 Aseprite）崩溃，或者你在没有保存精灵的情况下关闭 Aseprite 时恢复你的精灵。（即使你保存了精灵，原始备份也会在你的磁盘上至少保留几周。）

## 从之前的会话打开精灵

要从之前的会话恢复精灵，你必须使用“主页”选项卡中的“恢复文件”选项：

<p><img src="./data-recovery/home-tab.png" alt="主页选项卡" class="x2" /></p>

如果 Aseprite 崩溃（未正确关闭）并且某些精灵未被保存，你将看到“恢复文件”选项显示为一个按钮：

<p><img src="./data-recovery/home-tab-after-crash.png" alt="主页选项卡" class="x2" /></p>

此选项会打开“恢复文件”选项卡，可以在其中双击某个项目（或选中它并按下“恢复精灵”）来从之前的会话中恢复精灵：

<p><img src="./data-recovery/recover-files-tab.png" alt="主页选项卡" class="x2" /></p>

## 首选项

在 *编辑 > 首选项 > 文件* 部分，可以配置备份数据的保存方式和保存时长：

![数据恢复首选项](./data-recovery/recover-data-preferences.png)

* *每隔 X 秒/分钟自动保存恢复数据*：
  指示 Aseprite 应每隔 X 秒或分钟为每个已编辑的精灵自动保存备份数据（到磁盘上）（默认 2 分钟）。
* *将已编辑的精灵数据保留 Y 天/周/月*：对于每个被编辑过的精灵，Aseprite 将会在磁盘上保留备份数据指定的天数/周数/月数（默认 1 周）。
* *将关闭的精灵在内存中保留 Z 秒/分钟/小时*：如果你不小心关闭了一个精灵，Aseprite 将会在内存中（包含撤销信息）至少保留该精灵给定的时间（默认 15 分钟）。可以通过 *文件 > 打开最近文件 > 重新打开关闭的文件* 菜单选项（快捷键 Ctrl+Shift+T 或 ⇧⌘T）来重新打开一个已关闭的文件。

## 内部原理

备份数据保存在你的[首选项文件夹](./preferences-folder.md)内一个名为 `sessions` 的子文件夹中：

![Sessions 文件夹](./data-recovery/sessions-folder-focused.png)

`sessions` 文件夹可能包含多个子文件夹（对应 Aseprite 的每次运行）：

![Sessions 文件夹内部](./data-recovery/in-sessions-folder.png)

这些文件夹的名称（例如 `20180405-165510-1128`）有其含义，即 `YYYYMMDD-HHMMSS-PID`：

* `YYYY`、`MM`、`DD`：会话开始（Aseprite 启动时）的日期（年、月、日）。
* `HH`、`MM`、`SS`：会话开始当天的时间（时、分、秒）。
* `PID`：处理该会话文件夹的 Aseprite 实例的进程号/标识符。

这些文件夹中的每一个都包含有用的数据，可以用来恢复你在崩溃中可能丢失的一些精灵。

如果你无法使用“主页”选项卡中的“恢复文件”选项恢复会话，但你在[首选项文件夹](./preferences-folder.md)中有这些 `sessions/YYYYMMDD-HHMMSS-PID` 文件夹之一，可以将其中一个文件夹压缩为 `.zip` 文件并发送至 [support@aseprite.org](mailto:support@aseprite.org)，我们可以尝试恢复你的数据。

---

**另请参阅**

[故障排除](./troubleshooting.md) |
[首选项文件夹](./preferences-folder.md) |
[关于数据恢复内部原理的博客文章](https://dev.aseprite.org/2015/06/14/data-recovery/)