# 家庭助理插件：MyIP

MyIP 是一个高级 IP 工具，旨在提供有关您的 IP 地址的广泛信息和诊断。它非常适合需要查看和分析其 IP 详细信息、检查网站可访问性、进行 DNS 泄漏测试等用户。

_感谢每一个给我的库加星的人！要给它加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker镜像](https://github.com/jason5ng32/MyIP)。

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 单击 `保存` 按钮以存储您的配置。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。

## 配置

```
port : 18966 #您想要运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons