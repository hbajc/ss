# Home assistant add-on: Changedetection.io

**最佳且最简单的自托管免费开源网站变更检测跟踪、监控和通知服务。Visualping、Watchtower等的替代方案。旨在简单性——主要目标是免费监控哪些网站有文本更改。免费开源网页变更检测**

#### 示例用例

- 产品和服务的价格变动
- _缺货通知_和_重新入库通知_
- 政府部门更新（更改通常仅在其网站上发布）
- 新软件发布、安全建议，当您不在其邮件列表中时。
- 节日的变更
- 房地产上市变更
- 知道您最喜欢的威士忌何时打折，或在其他特别优惠被宣布之前获悉
- 来自政府网站的 COVID 相关新闻
- 大学/组织网站上的新闻
- 检测和监控 JSON API 响应的变化
- JSON API 监控和警报
- 法律和其他文件的变更
- 当网站上出现文本时通过通知触发 API 调用
- 使用 JSON 过滤器和 JSON 通知将 API 联系在一起
- 根据网页内容的变化创建 RSS 源
- 监控 HTML 源代码以发现意外更改，加强您的 PCI 合规性
- 您有一份非常敏感的 URL 列表进行监控，您 _不_ 想使用付费替代方案。（记住，_您_ 是产品）

_需要一个实际的 Chrome 运行器，支持 Javascript 吗？我们支持通过 WebDriver 和 Playwright 获取！</a>_

#### 主要特性

- 丰富的触发器过滤器，例如“基于文本触发”、“按选择器移除文本”、“忽略文本”、“提取文本”，还可以使用正则表达式！
- 使用 xPath 和 CSS 选择器定位元素，轻松监控复杂的 JSON，使用 JsonPath 规则
- 在快速的非 JS 和基于 Chrome JS 的“获取器”之间切换
- 轻松指定检查网站的频率
- 在提取文本之前执行 JS（适用于登录，参见 UI 中的示例！）
- 重写请求头，指定 `POST` 或 `GET` 以及其他方法
- 使用“可视选择器”帮助选定特定元素

_感谢所有关注我代码库的人！要关注，请单击下面的图像，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 主要特性


## 安装

此附加组件的安装相当简单，与安装任何其他 Hass.io 附加组件没有区别。

1. [将我的 Hass.io 附加组件库][repository]添加到您的 Hass.io 实例。
1. 安装此附加组件。
1. 转到 ip:port。Ingress 有点工作，但页面渲染不正确。


## 如何使用启用 Playwright JS 的获取器，而不是内置的明文/HTTP 客户端

Changedetection.io 附加组件本身只能使用内置的明文/HTTP 客户端抓取网站。

许多现代网页使用 JavaScript 填充内容，它们更具动态性，有时需要真实的 Chrome 浏览器来抓取内容，尽管许多可能在内置的“获取器”上正常工作。

您可以配置 Changedetection.io 使用 Playwright 获取器抓取页面，否则它将使用普通的非 JS 内置浏览器进行抓取。使用 Playwright 获取器提供完整的 Changedetection.io 功能，包括 JS 浏览器步骤以获取内容和可视过滤选择器。

要使用 Playwright 获取器，Changedetection.io 附加组件需要与由 alexbelgium 制作的无浏览器 Chrome 附加组件一起使用。

要安装无浏览器 Chrome 附加组件，请在 Homeassistant 中添加 alexbelgium/hassio-addons 库（https://github.com/alexbelgium/hassio-addons/）。从 Homeassistant 界面安装并启动该附加组件。要使用 Playwright 获取器，只需在添加要监控的新网站时，在“请求”选项卡中勾选“Playwright Chromium/Javascript”，或将其设为所有监控网站的系统标准，转到您的 Changedetection.io 附加组件的 Web 界面 > 设置 > 抓取并选择“Playwright Chromium/Javascript”。

有关无浏览器 Chrome 附加组件的更多信息：https://github.com/alexbelgium/hassio-addons/tree/master/browserless_chrome

这两个附加组件需要在同一台机器上运行。在 Raspberry Pi 4B 上测试版本为 Home Assistant 2023.5.3/Supervisor 2023.04.1/Operating System 10.1，但应该可以在任何其他版本和 amd64 设备上正常工作。

注意：无浏览器 Chrome 附加组件在抓取网站时相当耗费资源，无论是 RAM 还是 CPU。在 RPi 4B 上运行良好，但在旧设备上可能会很慢。最大同时抓取数量限制为 1。


[repository]: https://github.com/jdeath/homeassistant-addons