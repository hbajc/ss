# Home assistant 插件: EmulatorJS
基于浏览器的仿真，可移植到几乎任何设备上，适用于许多复古游戏机。使用了Libretro和EmulatorJS之间的混合仿真器。
 
_感谢每一个关注我仓库的人！要给我仓库加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于来自linuxserver的[docker镜像](https://github.com/linuxserver/docker-emulatorjs)。基于浏览器的仿真可移植到几乎任何设备上，适用于许多复古游戏机。使用了Libretro和EmulatorJS之间的混合仿真器。

## 安装

这个插件的安装非常简单，与安装其他任何Hass.io插件并无区别。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例。
1. 安装这个插件。
1. 点击`保存`按钮以存储你的配置。
1. 创建目录/share/emulatorjs以存储你的游戏/艺术文件。
1. 创建/share/emulatorjs/config和/share/emulatorjs/data。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 将rom放置在/share/emulatorjs/data/EMULATORNAME/roms中的正确文件夹内。
1. 进入管理端口。
1. 点击扫描以检测你为其添加了游戏的仿真器。
1. 点击仿真器框，执行步骤1和步骤2。
1. 打开WebUI应该会进入PlayerUI，访问你的本地homeassistant IP:port或管理端口。
1. 你的游戏应该可用。
1. 请参考官方文档以获得设置支持: https://github.com/linuxserver/docker-emulatorjs
1. 如果启动插件导致设置丢失，请停止插件，然后重新启动。有时映射到/share/emulatorjs会出错。

## 配置

```
adminport : 3000 # 你希望运行管理界面的端口。
port: 89 # 你希望运行前端的端口
```

Webui可以在`<your-ip>:port`找到。应该可以通过ingress访问。管理员端口无法通过ingress访问。

[repository]: https://github.com/jdeath/homeassistant-addons