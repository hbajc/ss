# 家庭助理插件：Readeck

Readeck 是一个简单的网络应用程序，让你保存你喜欢并希望永久保留的网页中的可读内容。把它看作是一个书签管理器和稍后阅读工具。

_感谢每一个给我的仓库点星的人！如果想点星，请点击下面的图片，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://codeberg.org/readeck/readeck)。

## 功能

### 🔖 书签

喜欢你正在阅读的页面吗？在 Readeck 中粘贴链接，完成！

### 📸 文章、图片和视频

Readeck 为你保存网页的可读内容，以便稍后阅读。它还会检测页面是否为图片或视频，并相应地调整处理方式。

### ⭐ 标签、收藏、归档

将书签移动到归档或收藏，并添加尽可能多的标签。

### 🖍️ 高亮

高亮书签中的重要内容，以便稍后轻松找到。

### 🗃️ 收藏夹

如果你需要一个专门的部分，包含过去两周内所有带有“猫”标签的书签，Readeck 允许你将此搜索查询保存到一个收藏夹中，以便稍后访问。

### 🧩 浏览器扩展

在浏览时想为稍后保留一些内容？无需复制和粘贴链接。安装浏览器扩展，轻松一键保存书签！

- [适用于 Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/readeck/)
- [适用于 Google Chrome](https://chromewebstore.google.com/detail/readeck/jnmcpmfimecibicbojhopfkcbmkafhee)
- [更多信息和源代码](https://codeberg.org/readeck/browser-extension)

### 📖 电子书导出

有什么比在电子阅读器上阅读你收集的文章更好的呢？你可以将任何文章导出为电子书文件（EPUB）。你甚至可以将一个收藏导出为一本书！

更棒的是，你可以直接从你的电子阅读器访问 Readeck 的目录和收藏夹（如果它支持 OPDS）。

### 🔎 全文搜索

无论你需要查找一篇文章中模糊的文本，还是特定标签或特定网站的所有文章，我们都为你提供帮助！

### 🚀 快速！

Readeck 是对所谓无聊但经过验证的技术的现代看法。它保证快速的响应时间和平滑的用户体验。

### 🔒 保护你的隐私和长期存档

你喜欢的这篇文章明年还会在线吗？十年后呢？或许不会；也许它会消失，包括文本和图片。因此，为了你的隐私以及长久保存，文本和图片会在你保存链接的那一刻存储在你的 Readeck 实例中。

除了视频外，没通过你的浏览器向外部网站发出过请求。

## 安装

1. 将我的 Hass.io 插件仓库 [添加到你的 Hass.io 实例][repository]。
1. 安装这个插件。
1. 点击“保存”按钮以存储你的配置。
1. 启动插件。
1. 退出插件并再次启动（第一次需要启动两次！）
1. 检查插件的日志，查看是否一切正常。
1. 打开 WebUI 应该可以通过 ingress 或 <你的-ip>:端口 访问。

## 更新
因为源代码没有托管在 GitHub 上，所以很难自动更新。如果想要最新版本，请发布问题。

## 配置

```
port : 8000 #你希望使用的端口。
```

Webui 可以在 `<你的-ip>:端口` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons