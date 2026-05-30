# 扩展：抖动矩阵

用于抖动矩阵扩展的 `.aseprite-extension` 文件内容结构：

```
dithering-matrix-example.aseprite-extension
|
+-- package.json
|
+-- matrix1.png
+-- matrix2.png
+-- ...
```

`package.json` 文件内容：

```json
{
  "name": "my-matrices",
  "displayName": "My Dithering Matrices",
  "description": "Dithering matrices created by ...",
  "version": "1.0",
  "publisher": "yournickname",
  "contributes": {
    "ditheringMatrices": [
      {
        "id": "matrix1",
        "name": "Matrix 1",
        "path": "./matrix1.png"
      },
      {
        "id": "matrix2",
        "name": "Matrix 2",
        "path": "./matrix2.png"
      }
      ...
    ]
  }
}
```

---

**另请参阅**

[扩展](./extensions.md)