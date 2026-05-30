# 扩展：按键

自 **Aseprite v1.2.35** 起，可以创建带有键盘快捷键的扩展。一个带有键盘快捷键的扩展的 `.aseprite-extension` 文件内容应类似于：

```
keys-example.aseprite-extension
|
+-- package.json
|
+-- my-keys.aseprite-keys
```

`package.json` 文件内容：

```
{
  "name": "my-keys-example",
  "displayName": "My Keys Example",
  "description": "Keys to do something",
  "version": "1.0",
  "author": { "name": "Full Name", "url": "https://twitter.com/your_username_or_homepage_url" },
  "categories": [
    "Keys"
  ],
  "contributes": {
    "keys": [
      { "id": "my-keys", "path": "./my-keys.aseprite-keys" }
    ]
  }
}
```

**`my-keys.aseprite-keys` 的示例**内容（该文件类似于[首选项文件夹](https://www.aseprite.org/docs/preferences/)中的 [user.aseprite-keys](https://www.aseprite.org/docs/files/#useraseprite-keys)，可以通过[编辑 > 键盘快捷键](./keyboard-shortcuts.md)创建/导出）：

```
<?xml version="1.0" encoding="utf-8" ?>
<keyboard version="1">
    <commands>
        <key command="Options" shortcut="J" />
        <key command="KeyboardShortcuts" shortcut="K" />
    </commands>
</keyboard>
```

在 aseprite 扩展中为自定义功能创建键盘快捷键时，你必须首先为其创建一个新命令。然后可以使用该命令的标题，通过 `.aseprite-keys` 文件将功能绑定到快捷键上。

可以在 [API 文档](https://www.aseprite.org/api/plugin#pluginnewcommand)中阅读更多关于如何创建命令的内容。

---

**另请参阅**

[扩展](../extensions.md)