# Home Assistant 附加组件: MeTube

用于 youtube-dl（使用 yt-dlp 分支）的 Web GUI，支持播放列表。允许您从 YouTube 和其他多个网站下载视频（https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md）。

_感谢所有给我的代码库点过星的人！要点星，请点击下面的图片，然后会出现在右上方。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件基于 [docker 镜像](https://github.com/alexta69/metube)。

## 安装

该附加组件的安装非常简单，与安装任何其他 Hass.io 附加组件没有区别。

1. [将我的 Hass.io 附加组件库][repository] 添加到您的 Hass.io 实例。
1. 安装此附加组件。
1. 点击 `Save` 按钮以保存您的配置。
1. 下载目录默认为 /share/metube，可以更改为共享中的任何内容。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切正常。
1. 通过入口或 <your-ip>:port 打开 WebUI 应该可以正常工作。

## 配置

```
port : 8081 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons