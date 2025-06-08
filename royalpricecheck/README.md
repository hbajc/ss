# 家庭助理插件: 皇家价格检查

## 描述
如果皇家加勒比邮轮的附加费用变便宜则通知。可以重新定价邮轮、饮品套餐、互联网、 excursions等。

_感谢所有给我的仓库点赞的人！点赞请点击下方图片，然后它将位于右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 安装

此插件的安装相当简单，与安装其他Hass.io插件没有什么不同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例中。
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。它会失败，这是正常的。
1. 转到 /addon-configs/2effc9b9_royalpricecheck。
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`（见下文）。
1. 再次运行插件并检查日志。
1. 确认工作正常后，使用自动化每天运行一次。

## Config.yaml
参见 `https://github.com/jdeath/CheckRoyalCaribbeanPrice`

## 自动运行
1. 创建一个自动化，每天运行一次此插件（在随机时间）。

```
alias: 启动皇家价格检查
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
1. 编辑 `/addon-configs/2effc9b9_royalpricecheck/config.yaml`。
1. 配置通知的行。

对于Home Assistant通知，其应类似于以下内容：
```
# config.yaml
apprise:
  urls:
    - 'hassio://192.168.X.XX/eyXXXXXXXXXXXXXXXX.eyXXXXXXXXXXXXXXXXXxx'
```
其中 `eyXXX.eyXXX` 字符串是Home Assistant的长期访问令牌。长期访问令牌可以在用户的Home Assistant个人资料页面底部的“长期访问令牌”部分创建。

更多细节请见: `https://github.com/caronc/apprise/wiki/Notify_homeassistant`

更多细节请见: `https://github.com/caronc/apprise` 你可以包含多条URL行以发送电子邮件等。
# 添加到侧边栏
由于没有WebUI，因此无法在侧边栏中显示此插件。但是，你可以将以下代码添加到你的Home Assistant `configuration.yaml`中，以通过侧边栏条目显示日志。

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