## &#9888; 开放问题 : [🐛 [Portainer] 无法登录 / 创建容器 / 进入容器等 (开始于2025-05-26)](https://github.com/alexbelgium/hassio-addons/issues/1877) 由 [@Joriex](https://github.com/Joriex)

# Home Assistant 插件：Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/给我买杯咖啡%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/用Paypal给我买杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

从以下地址取用 : https://github.com/hassio-addons/addon-portainer
实施的变更 : 更新到最新版本；入口；ssl；通过插件选项设置密码；允许手动覆盖

_感谢所有给我的仓库加星的朋友们！要加星请点击下面的图片，然后会显示在右上角。谢谢！_

[![给@alexbelgium/hassio-addons的星标用户](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer是一个开源轻量级管理UI，允许你
轻松管理你的Docker主机或Docker Swarm集群。

管理Docker从未如此简单。Portainer提供了详细的
Docker概述，并允许你管理容器、镜像、网络和
卷。

## 恢复备份

打开插件选项，将密码设置为“空”。重启插件，它将允许从备份中恢复Portainer。你需要将你的备份放在可访问的文件夹中，例如/share，以便在插件中挂载。

## 警告

Portainer插件非常强大，并几乎可以让你访问
整个系统。虽然此插件是在谨慎和
安全的考虑下创建和维护的，但在错误或缺乏经验的
手中，可能会损坏系统。

## 安装

---

安装此插件非常简单，与安装任何其他插件没有不同。

1. 将我的插件库添加到你的Home Assistant实例中（在监督插件商店右上角，或如果你已经配置了我的HA，点击下面的按钮）
   [![打开你的Home Assistant实例并显示添加插件库的对话框，预填特定库的URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击`保存`按钮以保存你的配置。
4. 根据你的偏好设置插件选项。
5. 启动插件。
6. 检查插件的日志，查看一切是否正常。
7. 打开WebUI并调整软件选项。

## 配置

---

Webui可以在<http://homeassistant:port>找到，或使用Ingress在你的侧边栏中。
默认的用户名/密码 : 在启动日志中描述。
可以通过应用WebUI进行配置，除了以下选项

```yaml
ssl: true/false
certfile: fullchain.pem #ssl证书，必须位于/ssl中
keyfile: privkey.pem #ssl密钥文件，必须位于/ssl中
password: 定义管理员密码。如果保持空白，将允许手动恢复先前的备份。至少12个字符。
```

## 支持

在GitHub上创建一个问题

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)