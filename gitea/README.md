# Home Assistant 插件：Gitea

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fgitea%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库加星的人！要加星，请点击下面的图像，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/gitea/stats.png)

## 关于

[Gitea](https://about.gitea.com/) 是一个轻松自托管的全能软件开发服务，它包括Git托管、代码审查、团队协作、包注册和CI/CD。它类似于GitHub、Bitbucket和GitLab。

各种调整和配置选项的添加。
该插件基于[docker镜像](https://hub.docker.com/r/gitea/gitea)。

## 配置

```yaml
certfile: fullchain.pem # ssl证书，必须位于/ssl中
keyfile: privkey.pem # ssl密钥文件，必须位于/ssl中
ssl: 应用程序是否应该使用https
APP_NAME: 应用程序名称
DOMAIN: 要访问的域名 # 默认：homeassistant.local
ROOT_URL: 自定义根URL，除非有特定的需求，否则不需要
```

Webui可以在 `<your-ip>:port` 找到。

## 安装

安装此插件非常简单，与安装任何其他Hass.io插件并无不同。

1. [将我的Hass.io插件库][repository]添加到您的Hass.io实例。
1. 安装此插件。
1. 点击“保存”按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 访问webui，您将在那里初始化应用程序。
1. 重新启动插件，以应用应应用的任何选项。

[repository]: https://github.com/alexbelgium/hassio-addons