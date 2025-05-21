# 家庭助手插件：Portainer

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fportainer%2Fconfig.json)

[![Codacy徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

派生自： https://github.com/hassio-addons/addon-portainer
已实施更改：更新到最新版本；Ingress；SSL；通过插件选项设置密码；允许手动覆盖

_感谢每一个点赞我的仓库的人！要给它加星，只需点击下面的图像，然后它会在右上角。谢谢！_

[![@alexbelgium/hassio-addons的星标用户列表](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/portainer/stats.png)

## 关于

---

Portainer是一个开源的轻量级管理界面，使您能够轻松管理Docker主机或Docker Swarm集群。

管理Docker从未如此简单。Portainer提供了详细的Docker概述，允许您管理容器、镜像、网络和卷。

## 恢复备份

打开插件选项并将密码设置为“空”。重启插件，将允许从备份中恢复Portainer。您需要将备份放在可访问的文件夹中，例如/share，以便在插件中挂载。

## 警告

Portainer插件非常强大，并可以让您几乎访问整个系统。虽然此插件是在考虑安全性和细心维护的情况下创建和维护的，但在不当或缺乏经验的手中，它可能会损坏您的系统。

## 安装

---

安装此插件非常简单，与安装其他任何插件没有什么不同。

1. 将我的插件库添加到您的家庭助手实例（在监督者插件商店右上角，或者如果您已配置我的HA，点击下面的按钮）
   [![打开您的家庭助手实例并显示添加插件库对话框，预填特定插件库URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击`保存`按钮以存储您的配置。
4. 根据您的偏好设置插件选项。
5. 启动插件。
6. 查看插件的日志，以确认一切正常。
7. 打开Web界面并调整软件选项。

## 配置

---

Web界面可以在<http://homeassistant:port>上找到，或在侧边栏中使用Ingress。
默认的用户名/密码：在启动日志中描述。
配置可以通过应用的Web界面完成，除了以下选项外。

```yaml
ssl: true/false
certfile: fullchain.pem #ssl证书，必须位于/ssl
keyfile: privkey.pem #ssl密钥文件，必须位于/ssl
password: 定义管理员密码。如果保持为空，将允许手动恢复以前的备份。至少12个字符。
```

## 支持

在GitHub上创建一个问题

## 插图

---

![插图](https://github.com/hassio-addons/addon-portainer/raw/main/images/screenshot.png)