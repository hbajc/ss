# Home assistant add-on: EmulatorJS
 在浏览器中的基于网络的模拟，便携于几乎任何设备，适用于许多复古控制台。使用了Libretro和EmulatorJS之间的多种仿真器的混合。

_感谢所有给我的仓库点星的人！要点星，请点击下面的图片，然后会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于来自linuxserver的[Docker镜像](https://github.com/linuxserver/docker-emulatorjs)。在浏览器中的基于网络的模拟，便携于几乎任何设备，适用于许多复古控制台。使用了Libretro和EmulatorJS之间的多种仿真器的混合。

## 安装

此插件的安装非常简单，与安装其他Hass.io插件没有区别。

1. 将我的Hass.io插件库添加到您的Hass.io实例中。
1. 安装此插件。
1. 点击`保存`按钮以存储您的配置。
1. 创建目录/share/emulatorjs以存储您的游戏/艺术文件。
1. 创建/share/emulatorjs/config和/share/emulatorjs/data。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 将rom文件放在/share/emulatorjs/data/EMULATORNAME/roms中的正确文件夹中。
1. 进入管理端口。
1. 点击扫描您添加游戏的模拟器。
1. 点击模拟器框，完成第1步和第2步。
1. 打开WebUI应进入PlayerUI，访问您本地的homeassistant IP:端口或管理端口。
1. 您的游戏应该可用。
1. 查阅官方文档以获取设置支持：https://github.com/linuxserver/docker-emulatorjs
1. 如果启动插件导致您的设置被清除，请停止插件并重新启动。有时映射到/share/emulatorjs可能不起作用。

## 配置

```
adminport : 3000 # 您想在其上运行管理界面的端口。
port: 89 # 您想在其上运行前端的端口。
```

Webui可以在`<your-ip>:port`找到。应该可以通过ingress访问。管理员端口无法通过ingress访问。

[repository]: https://github.com/jdeath/homeassistant-addons