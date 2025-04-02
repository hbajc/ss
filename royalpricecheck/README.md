# Home assistant 插件：皇家价格检查

## 描述
如果皇家加勒比邮轮附件降价，发送通知。可以重新定价邮轮、饮品套餐、互联网、游览等。

_感谢每一个为我的库点赞的人！要点赞，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装这个插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动插件。它会失败，这是正常的。
1. 转到 /addon-configs/2effc9b9_royalpricecheck
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`（见下文）
1. 再次运行插件并检查日志
1. 确认正常工作后，使用自动化每天运行一次

## Config.yaml
请参阅 `https://github.com/jdeath/CheckRoyalCaribbeanPrice`

## 自动运行
1. 创建一个自动化，每天运行一次这个插件（在随机时间）

```
alias: 开始皇家价格检查
description: ""
trigger:
  - platform: time
    at: "06:00:00"
condition: []
action:
  - delay: "{{ (range(0, 1)|random|int) }}:{{ (range(1, 59)|random|int) }}:00"
  - service: hassio.addon_start
    data:
      addon: 2effc9b9_royalpricecheck
mode: single
```

# 发送通知
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`
1. 配置通知的行

对于 Home Assistant 通知，它应该看起来像这样：
```
# config.yaml
apprise:
  urls:
    - 'hassio://192.168.X.XX/eyXXXXXXXXXXXXXXXX.eyXXXXXXXXXXXXXXXXXxx'
```
其中 `eyXXX.eyXXX` 字符串是 Home Assistant 的长期访问令牌。长期访问令牌可以在用户的 Home Assistant 个人资料页面底部的“长期访问令牌”部分创建。

更多详细信息请参见： `https://github.com/caronc/apprise/wiki/Notify_homeassistant`

更多详细信息请参见： `https://github.com/caronc/apprise` 您可以包含多个 URL 行以发送电子邮件等。

# 添加到侧边栏
由于没有 WebUI，无法显示在侧边栏中。但是，您可以将以下代码添加到您的 Home Assistant `configuration.yaml` 中，通过侧边栏条目显示日志。

```
panel_custom:
  - name: panel_rewards
    sidebar_title: 奖励
    sidebar_icon: mdi:medal
    url_path: 'hassio/addon/2effc9b9_royalpricecheck/logs'
    module_url: /api/hassio/app/entrypoint.js
    embed_iframe: true
    require_admin: true
```

# 问题

[repository]: https://github.com/jdeath/homeassistant-addons