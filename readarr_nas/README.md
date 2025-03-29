# Home Assistant 附加组件: Readarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Freadarr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Freadarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Freadarr%2Fconfig.json)

[![Codacy徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后在右上角点击。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/readarr/stats.png)

## 关于

---

[Readarr](https://github.com/Readarr/Readarr) 是一个用于 Usenet 和 BitTorrent 用户的电子书收藏管理器。它可以监视多个 RSS 源，以获取来自您喜欢的作者的新书，并将与客户端和索引器接口以抓取、排序和重命名它们。是电子书管理和自动化（Sonarr 的电子书版本）。
此附加组件基于 docker 镜像 https://github.com/linuxserver/docker-readarr

## 安装

---

此附加组件的安装非常简单，与安装其他任何附加组件没有什么不同。

1. 将我的附加组件库添加到您的 Home Assistant 实例中（在超级用户附加组件商店右上角，或者如果您已配置我的 HA，则点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加附加组件库对话框，带有预填的特定库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此附加组件。
3. 点击 `保存` 按钮以存储您的配置。
4. 根据您的偏好设置附加组件选项。
5. 启动附加组件。
6. 检查附加组件的日志以查看是否一切顺利。
7. 打开 WebUI 并调整软件选项。

## 使用

Webui 可以在 <http://homeassistant:8787/readarr> 找到，或者通过点击 `打开 Web UI` 按钮使用 ingress ☝️。

默认用户名/密码：在启动日志中描述。

## 配置

可以通过三种方式进行配置：

### 附加组件选项

```yaml
PGID: user
GPID: user
TZ: timezone
localdisks: sda1 #填写要挂载的硬件名称，以逗号分隔，或其标签。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smb 服务器列表，以逗号分隔
cifsusername: "username" # 可选，smb 用户名，适用于所有 smb 共享
cifspassword: "password" # 可选，smb 密码
connection_mode: ingress_noauth (默认，禁用身份验证以允许无缝的 ingress 集成)，noingress_auth (禁用 ingress 以允许更简单的外部 URL，启用身份验证)，ingress_auth (同时启用 ingress 和身份验证)
```

### 在 Readarr 中

从应用程序内进行的所有常规配置。

### ENV 覆盖文件：`/config/addons_config/readarr_nas.yml`

为了获得更多控制，您可以通过将环境变量作为键在有效的 `.yaml` 文件中定义它们。

```yaml
TZ: Europe/Paris
```

更多信息：www.github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

## 支持

在 GitHub 上创建一个问题。

## 插图

---

![插图](https://readarr.com/img/slider/artistdetails.png)

[库]: https://github.com/alexbelgium/hassio-addons