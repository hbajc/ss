# Home assistant add-on: 5etools

一套基于浏览器的工具，供D&D 5e的玩家和DM使用。从5etools GitHub下载的图片。不在jdeath的仓库中托管/发布任何图片或内容。由于Home Assistant插件创建者不使用此项，因此不提供支持。自托管的图像可能会比5etools网站落后一个版本。图像为4 GB，因此安装将需要很长时间，请耐心等候。

_感谢所有给我的仓库加星的人！要加星，请单击下面的图像，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用[docker镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

此插件的安装相当简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 安装此插件。4 GB的镜像下载需要一段时间。
1. 单击`Save`按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 打开的WebUI应通过ingress或<your-ip>:port工作。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons