# 扩展：语言

这是一个将 Aseprite 翻译成西班牙语的可能扩展示例。语言扩展的 `.aseprite-extension` 文件内容可以像这样：

```
spanish-language.aseprite-extension
|
+-- package.json
+-- es.ini
```

`package.json` 文件内容，例如：

```
{
  "name": "spanish-language",
  "displayName": "Spanish Translation",
  "description": "Translation to Spanish Example by Full Name",
  "version": "1.0",
  "author": { "name": "Full Name", "url": "https://twitter.com/your_username_or_homepage_url" },
  "categories": [
    "Languages"
  ],
  "contributes": {
    "languages": [
      { "id": "es",
        "path": "./es.ini",
        "displayName": "Español" }
    ]
  }
}
```

`contributes.languages.displayName` 属性在 **Aseprite v1.3-rc5** 中引入，用于在 *编辑 > 首选项 > 常规 > 语言* 组合框中显示语言名称，而不是语言代码/ID（例如 `es`）。

对于 `contributes.languages.id`，请使用 [ISO 639-1 语言代码](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)。

---

**另请参阅**

[扩展](../extensions.md)