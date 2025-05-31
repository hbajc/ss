# 家庭助手插件：nzbget

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/给我买咖啡%20(没有%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/使用%20Paypal%20给我买咖啡-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图像，随后会在右上角。谢谢！_

[![Star寄宿者名单 for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/nzbget/stats.png)

## 关于

[nzbget](http://nzbget.net/) 是一个USENET下载器，使用C++编写，旨在通过使用很少的系统资源来实现最大下载速度。
此插件基于docker镜像 https://github.com/linuxserver/docker-nzbget

## 配置

Webui可以在<http://homeassistant:PORT>找到。
默认用户名/密码：登录名：nzbget，密码：tegbzn6789
除以下选项外，所有配置均可通过应用的WebUI完成。

```yaml
PGID: 用户
GPID: 用户
TZ: 时区
localdisks: sda1 #将您的驱动器的硬件名称放入，以逗号分隔，或其标签。例如：sda1，sdb1，MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，挂载的smb服务器列表，以逗号分隔
cifsusername: "用户名" # 可选，smb用户名，适用于所有smb共享
cifspassword: "密码" # 可选，smb密码
```

## 安装

此插件的安装相当简单，与安装任何其他插件没有区别。

1. 将我的插件仓库添加到您的家庭助手实例中（在管理界面的插件商店的右上角，或者如果您已经配置了我的HA，请点击以下按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，该对话框预填特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击`保存`按钮以存储您的配置。
4. 设置插件选项以满足您的偏好。
5. 启动插件。
6. 检查插件的日志，以查看是否一切顺利。
7. 打开WebUI并调整软件选项。

## 支持

在GitHub上创建一个问题。

## 插图

![插图](https://nzbget.com/img/slider/artistdetails.png)

[repository]: https://github.com/alexbelgium/hassio-addons