# 运行命令

运行命令窗口可以运行[菜单栏](./menu-bar.md#menu-bar)中的任何选项、任何已安装的脚本，或[键盘快捷键](./keyboard-shortcuts.md#keyboard-shortcuts)菜单中的任何命令。可以通过*视图 > 运行命令*或 <kbd>Ctrl + 空格键</kbd> 访问。

![运行命令示例](./run-command/run-command.gif)

## 运行命令

要运行命令，请在搜索框中搜索你要运行的命令的名称。在搜索框下方，将显示搜索结果。按 <kbd>Enter</kbd> 执行第一个结果；使用方向键选择其他结果。

![运行命令搜索/方向键示例](./run-command/search.gif)

## 数学表达式

运行命令窗口支持数学表达式。要输入数学表达式，请键入 <kbd>=</kbd>（等号），后跟一个数学表达式。结果将显示在输入框下方。如果数学表达式无效（例如：有一个未闭合的括号），则结果将为 `NaN`。

![数学表达式示例](./run-command/math.gif)


### 支持的符号、常量和函数

| 符号 | 描述
|-|-
| `+` | 加
| `-` | 减/取负
| `*` | 乘
| `/` | 除
| `^` | 指数/幂
| `%` | [取模](https://en.wikipedia.org/wiki/Modulo)（求余数）

| 常量 | 描述
|-|-
| `pi` | [Pi](https://en.wikipedia.org/wiki/Pi) 的值（`3.14159...`）。
| `e` | 用于[科学记数法](https://en.wikipedia.org/wiki/Scientific_notation#E_notation)的 E，例如（`2.4e8`）。

**支持的函数：**
* `abs(x)` 
* `acos(x)`
* `asin(x)`
* `atan(x)`
* `atan2(x, y)`
* `ceil(x)`
* `cos(x)`
* `cosh(x)`
* `exp(x)`
* `floor(x)`
* `ln(x)`
* `log(x)`
* `log10(x)`
* `pow(x, y)`
* `sin(x)`
* `sinh(x)`
* `sqrt(x)`
* `tan(x)`
* `tanh(x)`

## 内联 Lua 表达式

运行命令窗口支持内联 [Lua](https://www.lua.org/) 代码。要开始一行代码，请键入 <kbd>@</kbd>。

![lua 表达式示例](./run-command/lua.gif)

可以创建全局变量和函数，并通过另一个运行命令代码行进行访问；这些变量和函数在 Aseprite 实例关闭后重置。

---

**另请参阅**

[键盘快捷键](keyboard-shortcuts#keyboard-shortcuts.md)