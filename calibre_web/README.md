# Home Assistant 插件: Calibre-web

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre_web%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre_web%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fcalibre_web%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库加星的人！要给我仓库加星请点击下面的图片，然后会在右上方显示。谢谢！_

[![为 @alexbelgium/hassio-addons 加星的用户](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/calibre_web/stats.png)

## 关于

---

[Calibre-web](https://github.com/janeczku/calibre-web) 是一个web应用，提供浏览、阅读和下载电子书的清晰界面，使用现有的Calibre数据库。还可以通过应用程序集成Google Drive并编辑元数据和Calibre库。

该插件基于docker镜像 https://github.com/linuxserver/docker-calibre-web

## 安装

---

安装此插件非常简单，与安装其他任何插件没有不同。

1. 将我的插件仓库添加到你的Home Assistant实例中（在右上角的超级管理员插件商店中，或者如果你已经配置了我的HA，可以点击下面的按钮）
   [![打开你的Home Assistant实例，并显示带有特定仓库URL的添加插件仓库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 单击 `保存` 按钮以存储你的配置。
4. 根据你的偏好设置插件选项。
5. 启动插件。
6. 检查插件的日志以查看一切是否顺利。
7. 打开webUI并调整软件选项。

## 配置

---

Webui可以在 <http://homeassistant:PORT> 找到。
默认用户名/密码 : 在启动日志中描述。
配置可以通过应用程序webUI进行，除了以下选项。

默认名称 : admin
默认密码 : admin123

```yaml
PGID: user
GPID: user
TZ: timezone
PASSWORD: 可选，为gui设置密码
CLI_ARGS: 可选，向calibre-web传递cli启动参数
localdisks: sda1 #输入你想挂载的驱动器的硬件名称，用逗号分隔，或其标签。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的smb服务器列表，使用逗号分隔
cifsusername: "username" # 可选，smb用户名，所有smb共享相同
cifspassword: "password" # 可选，smb密码
force_scheme_https: 如果你在访问ingress时遇到https的问题，请勾选此框以强制使用https
force_external_port: 如果你在访问ingress时遇到https的问题，请在此处记录用于访问HA的外部端口
```

## 支持

在github上创建一个issue

## 插图

---

![插图](https://calibre-web.com/img/slider/artistdetails.png)

[repository]: https://github.com/alexbelgium/hassio-addons