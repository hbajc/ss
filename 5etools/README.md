# Home assistant add-on: 5etools

一套基于浏览器的工具，供《龙与地下城》第五版的玩家和DM使用。下载自5etools GitHub的已发布图像。jdeath的存储库中没有托管或发布任何图像或内容。不提供支持，因为Home Assistant Addon的创建者并不使用此工具。自托管的图像可能会比5etools网站的版本晚一个修订。图像大小为4 GB，因此安装将需要较长时间，请耐心等待。

_感谢所有为我的存储库加星的朋友们！要加星，请点击下面的图像，然后它将位于右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件使用 [docker image](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

此附加组件的安装相当简单，与安装其他Hass.io附加组件没有区别。

1. [将我的Hass.io附加组件存储库][repository]添加到您的Hass.io实例中。
1. 安装此附加组件。4 GB的图像将需要一些时间下载。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动该附加组件。
1. 检查附加组件的日志，看看一切是否正常。
1. WebUI通过入口或<your-ip>:port打开应该可以工作。

## 配置

```
port : 8080 #您想要运行的端口。
```

Webui可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons