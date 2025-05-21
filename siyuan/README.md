# Home assistant 插件：SiYuan

SiYuan 是一个以隐私为本的个人知识管理系统，支持细粒度的区块级引用和 Markdown WYSIWYG。

似乎很受欢迎，但有订阅插件和可选的中国数据中心。使用时请谨慎。

_感谢所有关注我的仓库的人！要关注它，请点击下面的图片，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于 [docker 镜像](https://github.com/siyuan-note/siyuan)。

## 安装

安装这个插件非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到你的 Hass.io 实例中。
1. 安装这个插件。
1. 设置访问代码和端口。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 数据应该存储在 /addon_config/2effc9b9_siyuan 中。

## 配置

```
port : 6806 # 你想运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons