# 家庭助手插件：ytptube

yt-dlp的Web GUI，支持播放列表和频道（https://github.com/arabcoders/ytptube）。

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于[docker图像](https://github.com/arabcoders/ytptube)。

# YTPTube功能

* 支持多下载。
* 随机美丽背景。`可以禁用或更改源`。
* 可以处理直播流。
* 计划任务，将频道或播放列表排队，在指定时间自动下载。
* 根据选定事件向目标发送通知。
* 每个链接支持 `cli 选项` 和 `cookies`。
* 允许用逗号分隔的多个URL排队。
* 预设系统，以重用常用的yt-dlp选项。
* 简单的文件浏览器。`默认禁用`。
* 内置视频播放器 **支持侧车外部字幕**。
* 新的 `POST /api/history` 端点，允许同时发送一个或多个链接。
* 新的 `GET /api/history/add?url=http://..` 端点，允许通过GET请求添加单个项目。
* 现代前端UI。
* 使用SQLite作为数据库后端。
* 支持基本身份验证。
* 支持curl_cffi，查看 [yt-dlp文档](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#impersonation)
* 为非技术用户提供WebUI的基本模式，隐藏大多数常规功能。
* 容器中捆绑的工具：curl-cffi，ffmpeg，ffprobe，aria2，rtmpdump，mkvtoolsnix，mp4box。
* 自动重新排队即将到来的直播流。
* 根据自定义条件应用 `yt-dlp` 选项。
* 自定义浏览器扩展、书签和iOS快捷方式，以将链接发送到YTPTube实例。

## 安装

安装此插件需要几个额外步骤。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装此插件。
1. 单击 `保存` 按钮以存储配置。
1. 下载目录默认设置为/share/ytptube，可以更改为共享目录中的任何位置。
1. 启动插件。它会失败。
1. SSH进入家庭助手并输入 `chown hassio /addon_configs/2effc9b9_ytptube`
1. 启动插件。它会失败。
1. 再次SSH进入家庭助手并输入 `chown hassio /share/ytptube` 或如果你更改了下载目录则输入新的下载目录。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 通过<你的IP>:端口打开WebUI。Ingress不工作。

## 配置

```
port : 8081 #你想要运行的端口。
```

Webui可以在`<你的IP>:端口`找到。

[repository]: https://github.com/jdeath/homeassistant-addons