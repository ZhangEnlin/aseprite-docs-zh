# 扩展：调色板

调色板扩展的 `.aseprite-extension` 文件内容：

```
palette-example.aseprite-extension
|
+-- package.json
|
+-- my-palette.gpl
```

`package.json` 文件内容：

```
{
  "name": "palette-example",
  "displayName": "Palette Example",
  "description": "Palette created by Full Name",
  "version": "1.0",
  "author": { "name": "Full Name", "url": "https://twitter.com/your_username_or_homepage_url" },
  "categories": [
    "Palettes"
  ],
  "contributes": {
    "palettes": [
      { "id": "Palette-Example", "path": "./my-palette.gpl" }
    ]
  }
}
```

---

**另请参阅**

[扩展](../extensions.md)