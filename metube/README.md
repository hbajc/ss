# Home assistant 附加组件: MeTube

用于youtube-dl（使用yt-dlp分支）的Web GUI，支持播放列表。允许你从YouTube和其他数十个网站下载视频（https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md）。

_感谢所有给我的仓库点赞的人！要给它点赞，请点击下方图像，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件基于 [docker 镜像](https://github.com/alexta69/metube)。

## 安装

此附加组件的安装非常简单，与安装其他Hass.io附加组件没有区别。

1. [将我的Hass.io附加组件库][repository]添加到你的Hass.io实例。
1. 安装此附加组件。
1. 点击`保存`按钮以存储你的配置。
1. 下载目录默认设为/share/metube，可以更改为共享中的任何内容。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. WebUI应该可以通过入口访问，或通过<你的-ip>:端口访问。

## 配置

```
port : 8081 #你想使用的端口。
```

Webui可以在`<你的-ip>:端口`找到。

[repository]: https://github.com/jdeath/homeassistant-addons