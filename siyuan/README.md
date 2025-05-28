# Home assistant 插件: SiYuan

SiYuan 是一个以隐私为先的个人知识管理系统，支持细粒度的块级引用和 Markdown WYSIWYG。

看起来很受欢迎，但有订阅附加组件和可选的中国数据中心。使用时请谨慎

_感谢所有给我的代码库点星的人！要点星，请点击下面的图片，然后它将在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于 [docker 镜像](https://github.com/siyuan-note/siyuan)。

## 安装

安装这个插件非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository]添加到你的 Hass.io 实例。
1. 安装这个插件。
1. 设置访问代码和端口
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志，看看一切是否顺利。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 数据应该存放在 /addon_config/2effc9b9_siyuan
## 配置

```
port : 6806 #你想运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons