# Home Assistant 插件：5etools

一套基于浏览器的 D&D 5e 玩家和 DM 工具。下载从 5etools GitHub 发布的图片。没有在 jdeath 的仓库中托管/发布任何图片或内容。由于 Home Assistant 插件创建者不使用此插件，因此不提供支持。自托管的图片可能比 5etools 网站的版本落后一段时间。图片大小为 4 GB，因此安装将需要较长时间，请耐心等待。

_感谢每一个给我的仓库加星的人！要加星，请点击下面的图片，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

这个插件的安装非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例中。
1. 安装此插件。4 GB 的镜像将需要一段时间来下载。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 通过入口或 <your-ip>:port 打开 WebUI 应该可以正常工作。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons