# Home assistant 插件: Changedetection.io

**最好的、最简单的自托管免费开源网站变更检测、跟踪、监控和通知服务。是 Visualping、Watchtower 等的替代方案。旨在简单——主要目标是免费监控哪些网站有文本变化。免费开源网页变更检测**

#### 示例用例

- 产品和服务的价格发生变化
- _缺货通知_ 和 _重新入库通知_
- 政府部门更新（更改通常仅在其网站上）
- 新软件发布、安全公告，当您未在其邮件列表中时。
- 节日变更
- 房地产列表变更
- 知道您最喜欢的威士忌在特价销售时，或者在其他特别优惠公布之前
- 政府网站上的COVID相关消息
- 大学/组织网站上的新闻
- 检测和监控 JSON API 响应中的变化
- JSON API 监控和警报
- 法律和其他文件中的变更
- 当网站上出现文本时通过通知触发 API 调用
- 使用 JSON 过滤器和 JSON 通知将 APIs 连接在一起
- 根据网页内容的变化创建 RSS 源
- 监控 HTML 源代码中的意外变化，加强您的 PCI 合规性
- 您有一份非常敏感的 URL 清单需要监控，而您不想使用付费替代品。（记住，_您_ 是产品）

_需要一个支持 Javascript 的实际 Chrome 运行器吗？我们支持通过 WebDriver 和 Playwright 进行抓取！</a>_

#### 主要特性

- 许多触发过滤器，例如“基于文本触发”、“按选择器移除文本”、“忽略文本”、“提取文本”，还可以使用正则表达式！
- 使用 xPath 和 CSS 选择器定向元素，轻松监控复杂 JSON 的 JsonPath 规则
- 在快速非 JS 和基于 Chrome JS 的“抓取器”之间切换
- 轻松指定网站检查的频率
- 在提取文本之前执行 JS（适用于登录，查看 UI 中的示例！）
- 重写请求头，指定 `POST` 或 `GET` 等其他方法
- 使用“可视选择器”帮助目标特定元素

_感谢每一个给我的仓库点赞的人！要给它点个赞，请点击下面的图片，然后在右上角，就可以了。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要特性


## 安装

此插件的安装相当简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 访问 ip:port。Ingress 有点作用，但页面渲染不正确


## 如何使用启用 Playwright JS 的抓取器而不是内置的纯文本/HTTP 客户端

Changedetection.io 插件本身只能使用内置的纯文本/HTTP 客户端抓取网站。

许多现代网页使用 JavaScript 填充内容，它们更具动态性，有时需要真实的 Chrome 浏览器来抓取内容，尽管许多可能与内置的“抓取器”一起使用。

您可以配置 Changedetection.io 使用 Playwright 抓取器抓取页面，否则将使用纯非 JS 内置浏览器进行抓取。使用 Playwright 抓取器提供完整的 Changedetection.io 功能，包括 JS 浏览器步骤以抓取内容和可视过滤选择器。

要使用 Playwright 抓取器，Changedetection.io 插件需要与由 alexbelgium 制作的无浏览器 Chrome 插件配合使用。

要安装无浏览器 Chrome 插件，请在 Homeassistant 中添加 alexbelgium/hassio-addons 库（https://github.com/alexbelgium/hassio-addons/）。从 Homeassistant 界面安装并启动该插件。要使用 Playwright 抓取器，只需在“请求”选项卡中添加要监控的新站点时勾选“Playwright Chromium/Javascript”或将其设置为所有监控网站的系统标准，访问 Changedetection.io 插件的 Web 界面 > 设置 > 抓取并选择“Playwright Chromium/Javascript”。

有关无浏览器 Chrome 插件的更多信息：https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

这两个插件需要在同一台机器上运行。已经在 Raspberry Pi 4B 上测试通过 Home Assistant 2023.5.3/Supervisor 2023.04.1/Operating System 10.1，但应该适用于任何其他版本和 amd64 设备。

注意：无浏览器 Chrome 插件在抓取网站时相当消耗资源，无论是 RAM 还是 CPU。在 RPi 4B 上运行良好，可能在旧设备上较慢。最大并发抓取限制为 1。


[repository]: https://github.com/jdeath/homeassistant-addons