# 家庭助手插件：Prowlarr

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fprowlarr%2Fconfig.json)

[![Codacy徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub超级检查器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！想给我加星请点击下面的图片，然后它会显示在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/prowlarr/stats.png)

## 关于

---

[Prowlarr](https://github.com/Prowlarr/Prowlarr) 是一个索引器管理器/代理，基于流行的arr .net/reactjs基础栈，旨在与您的各种PVR应用集成。
这个插件基于 Docker 镜像 https://github.com/linuxserver/docker-prowlarr

## 安装

---

安装这个插件非常简单，与安装其他插件没有什么不同。

1. 将我的插件库添加到您的家庭助手实例中（在超级用户插件商店的右上角，或者如果您已经配置了我的HA，请点击下面的按钮）
   [![打开您的家庭助手实例并显示添加插件库对话框，特定插件库URL预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装这个插件。
3. 点击`保存`按钮以保存您的配置。
4. 设置插件选项以符合您的偏好
5. 启动插件。
6. 检查插件的日志以查看一切是否顺利。
7. 打开WebUI并调整软件选项

## 配置

---

Webui可以在<http://homeassistant:PORT>找到。
默认用户名/密码：在启动日志中描述。
配置可以通过应用的WebUI完成，除以下选项外：

```yaml
PGID: user
GPID: user
TZ: timezone
localdisks: sda1 # 输入要挂载的驱动器的硬件名称，多个名称用逗号分隔，或使用其标签，例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的smb服务器列表，用逗号分隔
cifsusername: "username" # 可选，smb用户名，所有smb共享相同
cifspassword: "password" # 可选，smb密码
```

## 支持

在GitHub上创建一个问题

## 插图

---

![插图](https://wiki.servarr.com/assets/prowlarr/hist_1_history.png)

[repository]: https://github.com/alexbelgium/hassio-addons