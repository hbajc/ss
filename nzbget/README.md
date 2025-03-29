# 家庭助理附加组件：nzbget

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnzbget%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的项目加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers repo roster](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载趋势](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/nzbget/stats.png)

## 关于

[nzbget](http://nzbget.net/) 是一个 Usenet 下载器，使用 C++ 编写，旨在通过很少的系统资源实现最大下载速度。
此附加组件基于 Docker 镜像 https://github.com/linuxserver/docker-nzbget

## 配置

Webui 可在 <http://homeassistant:PORT> 找到。
默认的用户名/密码 : 登录:nzbget，密码：tegbzn6789
可以通过应用的 WebUI 进行配置，除了以下选项

```yaml
PGID: 用户
GPID: 用户
TZ: 时区
localdisks: sda1 # 将驱动器的硬件名称以逗号分隔或者其标签放入。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的 smb 服务器，以逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "密码" # 可选，smb 密码
```

## 安装

安装此附加组件非常简单，与安装其他任何附加组件没有区别。

1. 将我的附加组件仓库添加到您的家庭助理实例中（在左上角的主管附加组件商店中，或者如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的家庭助理实例并显示添加附加组件仓库对话框，特定仓库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此附加组件。
1. 点击 `保存` 按钮以存储您的配置。
1. 根据您的喜好设置附加组件选项
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否正常。
1. 打开 WebUI 并调整软件选项

## 支持

在 GitHub 上创建 issue

## 插图

![插图](https://nzbget.com/img/slider/artistdetails.png)

[仓库]: https://github.com/alexbelgium/hassio-addons