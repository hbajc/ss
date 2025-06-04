# Home assistant 组件: SiYuan

SiYuan 是一个以隐私为第一的个人知识管理系统，支持精细化的块级引用和 Markdown 所见即所得。

看起来很受欢迎，但有订阅附加功能和可选的中国数据中心。使用时请谨慎。

_感谢所有给我的仓库加星的朋友！要加星，请点击下面的图像，然后会显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此组件基于 [docker 镜像](https://github.com/siyuan-note/siyuan)。

## 安装

该附加组件的安装非常简单，与安装任何其他 Hass.io 附加组件没有不同。

1. [将我的 Hass.io 附加组件库][repository] 添加到你的 Hass.io 实例。
1. 安装此附加组件。
1. 设置访问代码和端口。
1. 点击 `保存` 按钮以保存你的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看是否一切正常。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 数据应存储在 /addon_config/2effc9b9_siyuan。
## 配置

```
port : 6806 #你希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons