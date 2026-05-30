# 扩展：主题

主题扩展是一种修改 Aseprite 用户界面（UI）外观和感觉的方式。[主题](https://github.com/aseprite/themes)仓库中有一组已知的主题。

主题扩展的 `.aseprite-extension` 文件内容：

```
theme-example.aseprite-extension
|
+-- package.json
|
+-- theme.xml
|
+-- sheet.png
|
+-- sheet.aseprite-data
```

`package.json` 文件内容：

```
{
  "name": "your-theme",
  "displayName": "Your Theme",
  "description": "Your Theme",
  "version": "1.0",
  "author": { "name": "Your Name", "email": "your@email.com", "url": "http://your.website/" },
  "publisher": "aseprite",
  "license": "CC-BY-4.0",
  "categories": [
    "Themes"
  ],
  "contributes": {
    "themes": [
      { "id": "your-theme", "path": "." }
    ]
  }
}
```

给定的 `"path"` 属性是一个目录（通常是 `.`，表示 `package.json` 文件所在的同一目录），此目录必须包含一组文件：

* [`theme.xml`](#theme-xml)
* [`sheet.png`](#sheet-png)
* [`sheet.aseprite-data`](#sheet-aseprite-data)

## theme.xml

这是主题中最复杂的文件，它分为几个部分：

```xml
<?xml version="1.0" encoding="utf-8" ?>
<theme name="..." screenscaling="2" uiscaling="1">
  <authors>...</authors>
  <fonts>...</fonts>
  <dimensions>...</dimensions>
  <colors>...</colors>
  <parts>...</parts>
  <styles>...</styles>
</theme>
```

作为示例，可以查看官方默认的 [theme.xml](https://github.com/aseprite/aseprite/blob/master/data/extensions/aseprite-theme/theme.xml)。

在理想情况下，Aseprite 应该只使用 `<style>` 元素，但由于我们以渐进的方式从旧版本迁移主题，Aseprite 在代码中混合使用了 `<dimensions>`、`<colors>` 和 `<parts>`（而不是仅使用 `<styles>`）。也许将来我们可以只引用 `<styles>`，但目前所有这些类型的元素都是必需的。

### &lt;theme&gt;

主 `<theme>` 元素包含三个属性：

```xml
<theme name="..."
       screenscaling="2"
       uiscaling="1">
</theme>
```

`name` 属性只是一种识别主题的方式，但它会被忽略，UI 中将使用 `package.json` 文件中的 `displayName`。

`screenscaling="2"` 是一种指定首选默认 *"编辑 > 首选项 > 常规 > 屏幕缩放"* 因子的方式（2 表示 200%），`uiscaling` 是指定默认 *"UI 缩放"* 因子的方式（1 表示 100%）。

### &lt;authors&gt;

一个用于指明主题作者的部分：

```xml
<theme>
  <authors>
    <author name="Your Name" url="http://your.website/" />
  </authors>
</theme>
```

### &lt;fonts&gt;

一个用于指明主题中使用字体的部分。你需要指定两种字体：`default` 和 `mini`：

```xml
<theme>
  <fonts>
    <font id="default" font="Aseprite" />
    <font id="mini" font="Aseprite Mini" />
  </fonts>
</theme>
```

这里的 `Aseprite` 和 `Aseprite Mini` 字体在 Aseprite 发行版自带的默认 [`fonts.xml` 文件](https://github.com/aseprite/aseprite/blob/master/data/fonts/fonts.xml)中定义。作为替代方案，可以不通过 `font="..."` 属性指定预定义字体，而是定义自己的 `<font />` 元素，就像分发的 `fonts.xml` 文件中那样。

### &lt;dimensions&gt;

`<dimensions>` 部分包含一组 `<dim>` 元素，这些元素为程序的不同尺寸指定了一组整数值（像素）：

```xml
<theme>
  <dimensions>
    <dim id="..." value="integer value..." />
    <dim id="..." value="integer value..." />
    ...
  </dimensions>
</theme>
```

### &lt;colors&gt;

`<colors>` 部分包含一组 `<color>` 元素，这些元素指定了 UI 中使用的一些颜色：

```xml
<theme>
  <colors>
    <color id="..." value="#rrggbb" />
    <color id="..." value="#rrggbb" />
    ...
  </colors>
</theme>
```

### &lt;parts&gt;

```xml
<theme>
  <parts>
    <part id="..." ... />
    <part id="..." ... />
    ...
  </parts>
</theme>
```

### &lt;styles&gt;

```xml
<theme>
  <styles>
    <style id="...">...</style>
    <style id="...">...</style>
    ...
  </styles>
</theme>
```

## sheet.png

一个包含每个主题部件内容的[精灵表](./sprite-sheet.md)。这意味着对于 `theme.xml` 中的每个 `<part>` 元素：

```xml
<theme>
  <parts>
     <part ... />
     ....
  </parts>
</theme>
```

你将在 `<part>` 的区域中拥有一个精灵。

## sheet.aseprite-data

这是一个 Aseprite 使用的辅助文件。当我们加载 `sheet.png` 文件时，如果 Aseprite 找到此 `sheet.aseprite-data` 文件，它将为 `theme.xml` 中的每个主题部件创建一个切片（当我们从 Aseprite 保存 `sheet.png` 时也是如此，主题部件将与切片保持同步）：

```xml
<?xml version="1.0" encoding="utf-8"?>
<sprite>
  <slices theme="theme.xml" />
</sprite>
```

---

**另请参阅**

[扩展](./extensions.md)