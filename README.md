# 光影 · 相机成像实验室

用 HTML、CSS 和 JavaScript 实现的交互式相机成像模拟器。调节镜头与曝光参数，实时观察取景、景深、虚化、噪点和运动拖影，并了解不同相机镜头的成像原理。

![相机成像模拟器界面](docs/camera-preview.png)

## 直接运行

下载或克隆仓库后，用 Chrome、Edge 或 Safari 打开根目录的 **`camera-simulator.html`**。

成品 HTML 已内嵌脚本、样式和图片，可以离线运行，无需安装依赖或启动服务器。

```bash
git clone https://github.com/thomasDJMax/wcd.git
cd wcd
```

如需通过本地服务器访问，也可在仓库目录执行：

```bash
python3 -m http.server 8000
```

然后打开 <http://localhost:8000/camera-simulator.html>。

## 可以做什么

- 切换广角、标准、长焦、微距、鱼眼与变焦镜头，查看各类镜头的说明和成像示意。
- 调节焦距、光圈、快门、ISO、对焦距离和拍摄距离，观察参数如何影响画面。
- 点击主体或背景对焦，使用自动对焦、构图网格和参数复位。
- 开启主体运动，对比快快门与慢快门产生的拖影。
- 在微距模式体验理想薄透镜的 1∶1 成像。
- 拍摄当前模拟画面并保存为 PNG。
- 在桌面与手机浏览器中使用响应式界面。

## 修改与构建

编辑 `src/camera-template.html`，或替换 `assets/` 中的 PNG 素材，然后运行：

```bash
python3 build.py
```

构建脚本仅使用 Python 标准库，将素材嵌入根目录的 `camera-simulator.html`。构建后重新打开或刷新该 HTML 即可。

```text
.
├── camera-simulator.html       # 可直接运行的离线成品
├── build.py                    # 标准库构建脚本
├── src/
│   └── camera-template.html    # 页面、样式与模拟逻辑
├── assets/
│   ├── background.png         # 花园背景
│   └── subject.png            # 带透明通道的花瓶主体
└── docs/
    ├── 使用说明.md             # 操作、公式与模型说明
    └── camera-preview.png      # 界面预览
```

## 成像模型

模拟器采用 36×24 mm 全画幅传感器、理想薄透镜和分层场景。薄透镜公式、投影倍率、弥散圆与景深计算相互对应；微距包含理想延伸曝光损失。鱼眼采用等距映射，曝光、虚化、ISO 噪点与运动模糊使用教学近似。

这是一款帮助理解相机参数的教学模拟器。模型未包含具体镜头的真实镜组、衍射、像差、内对焦结构及传感器标定。固定机位变焦主要改变取景范围；透视关系由拍摄位置决定。

完整操作与模型范围见 [使用说明](docs/使用说明.md)。场景素材由 AI 生成，并已包含在仓库内。

## 验证

六类镜头、参数调节、对焦、网格、主体运动、微距 1∶1、复位和拍照预览均已进行浏览器交互验证。桌面 1536×1024、手机 390×844 已检查布局；JavaScript 语法检查通过。

数值示例：50 mm、f/2.8、对焦 3 m 时，景深约为 2.73–3.33 m；ISO 翻倍增加一档亮度，快门时间减半减少一档亮度，f/2.8 改为 f/5.6 减少两档亮度。

## 参考

- [尼康：理解焦距](https://www.nikonusa.com/learn-and-explore/c/tips-and-techniques/understanding-focal-length)
- [斯坦福：高斯成像](https://www-graphics.stanford.edu/courses/cs178-11/applets/gaussian.html)
- [斯坦福：景深演示](https://www.graphics.stanford.edu/courses/cs178/applets/dof.html)
