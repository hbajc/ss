# Home assistant add-on: wDOSg

wDOSg (网页 DOS 游戏) 是一个集中的 DOS 游戏库，允许您从 IGDB 获取元数据，并通过 js-dos 在浏览器中运行游戏，使用极简的配置。

_感谢每一个给我仓库加星的人！要加星请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件使用 [docker 镜像](https://github.com/SoulRaven80/wdosg)。

## 安装

安装此附加组件需要一些额外的工作。
1. 查阅官方 [仓库](https://github.com/SoulRaven80/wdosg)
1. 获取一个 Twitch 开发者账户 [说明](https://api-docs.igdb.com/#account-creation)。
1. [将我的 Hass.io 附加组件仓库][repository] 添加到您的 Hass.io 实例中。
1. 点击 `保存` 按钮以存储您的配置。
1. 此附加组件需要 CLIENT_ID 和 SECRET。它会为您获取令牌。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切正常。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问
1. 默认用户/密码 = wdosg@wdosg.com / wdosg
1. 查阅官方文档制作一个 jsdos 包。这有点麻烦！最新版本可以直接从您自己的游戏 zip 包中制作。确保 zip 文件中的游戏直接位于 zip 的根目录，而不是在 zip 内的文件夹中！
1. 上传您的包并玩游戏。
1. 设置将位于 /addon_configs/2effc9b9_wdosg

## 配置

```
port : 3001 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons