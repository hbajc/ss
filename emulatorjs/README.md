# 家庭助理插件：EmulatorJS
基于浏览器的网络模拟，便携，几乎可以在任何设备上运行，支持多种复古游戏机。使用Libretro和EmulatorJS之间的多种模拟器混合。

_感谢所有给我的代码库加星的人！要加星，请点击下方图片，然后会显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件基于来自linuxserver的[docker镜像](https://github.com/linuxserver/docker-emulatorjs)。基于浏览器的网络模拟，便携，几乎可以在任何设备上运行，支持多种复古游戏机。使用Libretro和EmulatorJS之间的多种模拟器混合。

## 安装

此插件的安装相当简单，与安装任何其他Hass.io插件没有区别。

1. [将我的Hass.io插件库][repository]添加到你的Hass.io实例中。
1. 安装此插件。
1. 点击`保存`按钮以保存你的配置。
1. 创建目录 /share/emulatorjs 用于存储你的游戏/艺术文件。
1. 创建 /share/emulatorjs/config 和 /share/emulatorjs/data 。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 将rom文件放入/share/emulatorjs/data/EMULATORNAME/roms中的正确文件夹。
1. 转到管理端口。
1. 点击扫描你添加了游戏的模拟器。
1. 点击模拟器框，执行步骤1和步骤2。
1. 打开WebUI应访问PlayerUI，转到你的本地homeassistant IP:port或管理端口。
1. 你的游戏应该可用。
1. 查阅官方文档以获取设置支持：https://github.com/linuxserver/docker-emulatorjs
1. 如果启动插件导致你的设置被清除，请停止插件并重新启动。有时映射到/share/emulatorjs可能会失败。

## 配置

```
adminport : 3000 #你想要运行管理界面的端口。
port: 89 #你想要运行前端的端口。
```

Webui可以在 `<your-ip>:port` 找到。应该可以通过ingress访问。管理端口无法通过ingress访问。

[repository]: https://github.com/jdeath/homeassistant-addons