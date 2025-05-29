## &#9888; 打开问题: [🐛 [Portainer] 无法登录 / 创建容器 / 进入容器等 (创建于 2025-05-26)](https://github.com/alexbelgium/hassio-addons/issues/1877) 通过 [@Joriex](https://github.com/Joriex)

# 家庭助理插件: Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

派生自: https://github.com/hassio-addons/addon-portainer
实施的更改: 更新到最新版本；入口；ssl；通过插件选项设置密码；允许手动覆盖

_感谢每一个为我的项目加星的人！要为它加星，请单击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理您的 Docker 主机或 Docker 集群。

管理 Docker 变得前所未有的简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 恢复备份

打开插件选项并将密码设置为“空”。重启插件，它将允许从备份中恢复 Portainer。您需要将备份放入一个可访问的文件夹，如 /share，以便在插件中挂载。

## 警告

Portainer 插件非常强大，几乎可以让您访问整个系统。虽然这个插件是小心创建和维护的，并且考虑了安全性，但在错误或缺乏经验的手中，它可能会损坏您的系统。

## 安装

---

安装此插件非常简单，与安装其他任何插件没有不同。

1. 将我的插件库添加到您的家庭助理实例中（在管理插件商店的右上角，或者如果您已经配置了我的 HA，单击下面的按钮）
   [![打开您的 Home Assistant 实例，显示带有预填特定仓库URL的添加插件库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 单击 `保存` 按钮以保存您的配置。
4. 根据您的偏好设置插件选项。
5. 启动插件。
6. 检查插件日志以查看是否一切顺利。
7. 打开 webUI 并调整软件选项。

## 配置

---

Webui 可以在 <http://homeassistant:port> 找到，或在您的侧边栏中使用 Ingress。
默认用户名/密码：在启动日志中描述。
可以通过应用程序 webUI 进行配置，除了以下选项

```yaml
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #ssl密钥文件，必须位于 /ssl
password: 定义管理员密码。如果为空，将允许手动恢复以前的备份。至少 12 个字符。
```

## 支持

在 github 上创建问题

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)