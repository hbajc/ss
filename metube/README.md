# Home assistant add-on: MeTube

youtube-dl 的网络 GUI（使用 yt-dlp 分支），支持播放列表。允许您从 YouTube 和其他众多网站下载视频（https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md）。

_感谢所有给我的仓库加星的人！要加星，请点击下面的图像，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://github.com/alexta69/metube)。

## 安装

此插件的安装非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `Save` 按钮以保存您的配置。
1. 下载目录默认是 /share/metube，可以更改为共享中的任何内容。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. WebUI 应该可以通过入侵或 <您的 IP>:端口 访问。

## 配置

```
port : 8081 #您想要运行的端口。
```

Webui 可以在 `<您的 IP>:端口` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons