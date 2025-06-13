## &#9888; 开放问题 : [🐛 [Portainer] 无法登录 / 创建容器 / 进入容器等 (打开时间: 2025-05-26)](https://github.com/alexbelgium/hassio-addons/issues/1877) 提交者 [@Joriex](https://github.com/Joriex)

# Home Assistant 插件: Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy 勋章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20基础)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/买我一杯咖啡%20(无%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/用%20Paypal%20买我一杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

从以下项目分叉: https://github.com/hassio-addons/addon-portainer
实施的更改 : 更新至最新版本；入口；ssl；通过插件选项设置密码；允许手动覆盖

_感谢每一个给我的仓库加星的人！要加星，请点击下面的图片，然后会显示在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 仓库列表](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer 是一个开源的轻量级管理 UI，允许您
轻松管理您的 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。 Portainer 提供了详细的
Docker 概览，让您能够管理容器、镜像、网络和
卷。

## 恢复备份

打开插件选项并将密码设置为“empty”。重启插件，它将允许从备份中恢复 Portainer。您需要将备份放置在可访问的文件夹中，例如 /share，以便在插件中挂载。

## 警告

Portainer 插件非常强大，几乎可以让您访问
整个系统。虽然此插件是在谨慎和
安全考虑下创建和维护的，但若在错误或经验不足的手中，
它可能会损坏您的系统。

## 安装

---

安装此插件非常简单，与安装任何其他插件没有什么区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在超管插件商店右上角，或者如果您已配置我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，预填特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以存储您的配置。
4. 根据您的偏好设置插件选项。
5. 启动插件。
6. 检查插件的日志，查看是否一切顺利。
7. 打开 WebUI 并调整软件选项。

## 配置

---

Webui 可以在 <http://homeassistant:port> 找到，或者通过侧边栏使用 Ingress。
默认用户名/密码 : 在启动日志中描述。
可以通过应用程序的 WebUI 进行配置，以下选项除外：

```yaml
ssl: true/false
certfile: fullchain.pem #ssl 证书，必须位于 /ssl
keyfile: privkey.pem #ssl 秘钥文件，必须位于 /ssl
password: 定义管理员密码。如果保留为空，将允许手动恢复先前的备份。至少 12 个字符。
```

## 支持

在 GitHub 上创建一个问题

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)