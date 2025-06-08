## &#9888; 打开问题 : [🐛 [Portainer] 无法登录 / 创建容器 / 进入容器等 (已开于 2025-05-26)](https://github.com/alexbelgium/hassio-addons/issues/1877) 由 [@Joriex](https://github.com/Joriex)

# 家庭助理插件: Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建者](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

从以下地址派生 : https://github.com/hassio-addons/addon-portainer
已实现的更改 : 更新到最新版本；入口；SSL；通过插件选项设置密码；允许手动覆盖

_感谢所有为我的仓库加星的人！要加星，请单击下面的图片，然后它将在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers repo roster](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer 是一个开源轻量级管理用户界面，允许您
轻松管理您的 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了对 Docker 的详细
概述，并允许您管理容器、映像、网络和
卷。

## 恢复备份

打开插件选项并将密码设置为“空”。重启插件，它将允许恢复 portainer 的备份。您需要将备份放在一个可访问的文件夹中，例如 /share，以便在插件中挂载

## 警告

Portainer 插件非常强大，几乎可以让您访问
整个系统。虽然此插件是在小心和
安全考虑下创建和维护的，但如果落入错误或缺乏经验的手中，
可能会对系统造成损害。

## 安装

---

安装此插件相当简单，与安装其他插件
并没有什么不同。

1. 将我的插件库添加到您的家庭助理实例（在超管插件商店右上角，或者如果您已配置我的 HA，请点击下方按钮）
   [![打开您的家庭助理实例并显示带有特定库 URL 的添加插件库对话框。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以保存您的配置。
4. 根据您的偏好设置插件选项
5. 启动插件。
6. 检查插件的日志以查看是否一切正常。
7. 打开 webUI 并调整软件选项

## 配置

---

Webui 可以在 <http://homeassistant:port> 找到，或在侧边栏使用 Ingress。
默认用户名/密码 : 在启动日志中描述。
可以通过应用 webUI 进行配置，除了以下选项

```yaml
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #ssl 私钥文件，必须位于 /ssl
password: 定义管理员密码。如果保持为空，将允许手动恢复先前的备份。至少 12 个字符。
```

## 支持

在 github 上创建一个问题

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)