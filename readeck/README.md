# 家庭助手附加组件: Readeck

Readeck 是一个简单的网络应用程序，让您保存您喜欢的网页的珍贵可读内容，并想要永远保留。把它看作是一个书签管理器和稍后阅读工具。

_感谢所有给我的仓库加星的人！想要加星请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个附加组件基于 [docker image](https://codeberg.org/readeck/readeck)。

## 特性

### 🔖 书签

喜欢您正在阅读的页面吗？将链接粘贴到 Readeck 中，您就完成了！

### 📸 文章、图片和视频

Readeck 为您保存网页的可读内容，您可以稍后阅读。它还会检测页面是图像还是视频，并相应地调整其处理方式。

### ⭐ 标签、收藏、档案

将书签移动到档案或收藏夹，并添加您想要的任意数量的标签。

### 🖍️ 高亮

高亮书签中的重要内容，以便稍后轻松找到。

### 🗃️ 集合

如果您需要一个专门的部分来存储过去两周的所有书签，并用“猫”标记，Readeck 允许您将此搜索查询保存到一个集合中，以便您稍后访问。

### 🧩 浏览器扩展

想在浏览时保留某个内容？无需复制和粘贴链接。安装浏览器扩展程序，一键保存书签！

- [适用于 Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/readeck/)
- [适用于 Google Chrome](https://chromewebstore.google.com/detail/readeck/jnmcpmfimecibicbojhopfkcbmkafhee)
- [更多信息和源代码](https://codeberg.org/readeck/browser-extension)

### 📖 电子书导出

有什么比在电子阅读器上阅读您收集的文章更好的呢？您可以将任何文章导出为电子书文件（EPUB）。您甚至可以将一个集合导出为一本书！

此外，如果您的电子阅读器支持 OPDS，您可以直接从阅读器访问 Readeck 的目录和集合。

### 🔎 全文搜索

无论您需要查找文章的模糊文本，还是查找带有特定标签或来自特定网站的所有文章，我们都能满足您的需求！

### 🚀 快速！

Readeck 是对所谓的无聊但经过验证的技术的一种现代尝试。它保证非常快速的响应时间和平滑的用户体验。

### 🔒 为您的隐私和长期存档而构建

您喜欢的这篇文章明年还会在线吗？10年后呢？也许不会；也许一切都消失了，文本和图片均不在。因此，为了您的隐私和文章的长期保存，文本和图片在您保存链接的瞬间就存储在您的 Readeck 实例中。

除了视频之外，您浏览器向外部网站发送的请求不会产生任何请求。

## 安装

1. [将我的 Hass.io 附加库][repository]添加到您的 Hass.io 实例中。
1. 安装此附加组件。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动附加组件。
1. 退出附加组件并重新启动（第一次启动需要启动两次！）
1. 检查附加组件的日志以查看是否一切顺利。
1. 打开 WebUI 应该可以通过入口或 `<your-ip>:port` 访问。

## 更新
由于源代码未托管在 GitHub 上，因此很难自动更新此项。如果想要最新版本，请发布问题。

## 配置

```
port : 8000 #您想运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons