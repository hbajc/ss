# 家庭助手插件：EmulatorJS
基于浏览器的模拟，可以在几乎所有设备上使用，适用于许多复古控制台。该插件结合了Libretro和EmulatorJS的多种模拟器。

_感谢每一个为我的仓库点星的人！要点星，请点击下方的图片，然后它将在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件基于来自 linuxserver 的 [docker 镜像](https://github.com/linuxserver/docker-emulatorjs)。基于浏览器的模拟，可以在几乎所有设备上使用，适用于许多复古控制台。该插件结合了Libretro和EmulatorJS的多种模拟器。

## 安装

该插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
2. 安装此插件。
3. 点击 `Save` 按钮以保存您的配置。
4. 创建目录 /share/emulatorjs 以存储您的游戏/艺术文件。
5. 创建 /share/emulatorjs/config 和 /share/emulatorjs/data。
6. 启动插件。
7. 检查插件的日志以确认一切正常。
8. 将游戏镜像放入 /share/emulatorjs/data/EMULATORNAME/roms 目录的正确文件夹中。
9. 进入 Admin 端口。
10. 点击扫描您添加游戏的仿真器。
11. 点击仿真器框，执行步骤 1 和步骤 2。
12. 打开 WebUI 应该会进入 PlayerUI，访问您的本地 homeassistant IP:port 或管理员端口。
13. 您的游戏应该可以使用。
14. 请查阅官方文档以获取设置支持：https://github.com/linuxserver/docker-emulatorjs
15. 如果启动插件导致您的设置被清除，请停止插件并重新启动。有时映射到 /share/emulatorjs 的功能会出问题。

## 配置

```
adminport : 3000 # 您希望运行管理员界面的端口。
port: 89 # 您希望运行前端的端口。
```

Webui 可以在 `<your-ip>:port` 找到。应通过入口访问。管理员端口不提供通过入口访问。

[repository]: https://github.com/jdeath/homeassistant-addons