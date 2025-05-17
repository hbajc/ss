# 家庭助理附加组件：Prowlarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=检查%20代码%20基)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请%20我%20喝%20咖啡%20(无%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请%20我%20喝%20咖啡%20使用%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库星标的人！要给仓库星标，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![星标者名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/prowlarr/stats.png)

## 关于

---

[Prowlarr](https://github.com/Prowlarr/Prowlarr)是一个基于流行的arr .net/reactjs基础栈构建的索引器管理器/代理，可以与您的各种PVR应用程序集成。
此附加组件基于docker镜像 https://github.com/linuxserver/docker-prowlarr

## 安装

---

该附加组件的安装非常简单，与安装其他任何附加组件没有区别。

1. 将我的附加组件库添加到您的家庭助理实例中（在顶部右侧的管理器附加组件商店中，或者如果您已经配置了我的HA，请点击下面的按钮）
   [![打开您的家庭助理实例并显示添加附加组件库对话框，预填特定的库URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此附加组件。
3. 点击`保存`按钮以保存您的配置。
4. 根据您的偏好设置附加组件选项。
5. 启动附加组件。
6. 检查附加组件的日志以查看一切是否顺利。
7. 打开webUI并调整软件选项。

## 配置

---

WebUI可以在 <http://homeassistant:PORT> 找到。
默认的用户名/密码：在启动日志中描述。
配置可以通过应用webUI进行，除了以下选项：

```yaml
PGID: 用户
GPID: 用户
TZ: 时区
localdisks: sda1 # 将你的驱动器对应的硬件名称以逗号分隔放入，或者是它的标签，例如：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的smb服务器列表，以逗号分隔
cifsusername: "用户名" # 可选，smb用户名，适用于所有smb共享
cifspassword: "密码" # 可选，smb密码
```

## 支持

在github上创建一个问题

## 插图

---

![插图](https://wiki.servarr.com/assets/prowlarr/hist_1_history.png)

[仓库]: https://github.com/alexbelgium/hassio-addons