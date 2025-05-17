# Home Assistant Community Add-on: Netboot.xyz
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

Netboot.xyz PXE 服务器用于 Homeassistant OS

## 关于

netboot.xyz 是一种从 BIOS 中一个地方通过 PXE 启动各种操作系统安装程序或实用工具的方法，而无需去检索运行工具的介质。iPXE 用于提供一个用户友好的菜单，让您轻松选择您想要的操作系统，以及任何特定类型的版本或可启动标志。

您可以远程将 ISO 附加到服务器，作为 Grub 中的救援选项进行设置，甚至可以将您的家庭网络设置为默认引导到它，以便它始终可用。

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
这个附加组件的安装相当简单，并且与安装任何其他自定义 Home Assistant 附加组件没有不同。<br />
只需点击上面的链接或将我的库添加到 hassio 附加组件库: <https://github.com/FaserF/hassio-addons>

## 配置

**注意**: _记得在更改配置后重启附加组件。_

示例附加组件配置：

```yaml
path: /media/netboot/image
path_config: /media/netboot/config
dhcp_range: 192.168.178.200
```
<br />

**注意**: _这只是一个示例，不要复制和粘贴！创建你自己的！_

### 选项: `path`

这个选项是必需的。根据你的 ISO 文件以及其他文件的位置进行更改。

注意：它必须在 /media 文件夹中的某个地方！其他文件夹对该附加组件不可见。

### 选项: `path_config`

这个选项是必需的。根据你的 netboot.xyz 配置文件及其他文件的位置进行更改。

注意：它必须在 /media 文件夹中的某个地方！其他文件夹对该附加组件不可见。

### 选项: `dhcp_range`

这个选项是必需的。根据你的网络进行更改。尝试在最后的范围中使用更高的 IP（例如：100 或 200）

## Ingress

该附加组件支持 Homeassistant Ingress。但似乎有些错误。

## 后安装
第一次启动之前，我建议查看 netboot 配置。<br />
前往 <http://YOUR-HOMEASSISTANT-IP:3000> -> 菜单 -> boot.cfg<br />

### Windows
1. 根据你的 WinPE 位置更改以下行： <br />
   set win_base_url <http://YOUR-SERVER-IP:PortForTheNGINXserver/WinPE> <br />

   例如，如果你将提取的文件直接托管在 netboot.xyz 服务器上，而你的 IP 地址是 192.168.178.2: <br />
   set win_base_url <http://192.168.178.2:85/WinPE> <br />

2. 将 Windows PE 文件复制到你的 $path 文件夹 -> WinPE -> x64<br />
   示例: /media/netboot/image/WinPE/x64<br />

3. 提取 Windows ISO 并将文件复制到你的 $path 文件夹中的任何位置，例如：<br />
   /media/netboot/image/windows<br />

4. 安装 Samba Share Homeassistant 附加组件并启动它<br />
   这是将 win10 ISO 提供给 winPE 所需的<br />

5. 在启动 WinPE 后输入以下行<br />
net use Z: \ \YOUR-SERVER-IP\$path /user:YOUR-SERVER-IP\mySambaUser myPassword<br />
net use Z: \ \192.168.178.2\media\netboot\image\windows /user:192.168.178.2\mySambaUser myPassword<br />
Z:\setup.exe <br />

更多信息： <br />
<https://netboot.xyz/faq/windows/>

### 自动化 Windows 安装过程

修改你的 WinPE：<br />
1. 在你的 WinPE 位置创建一个 Main.cmd 文件，在一个名为 "Scripts" 的新文件夹中 <br />
   例如：/media/netboot/image/WinPE/x64/Scripts/Start.cmd<br />
   然后将上述两行添加到该脚本中<br />
   然后修改 wpeinit 使用该脚本。
2. 创建一个 autounattend.xml 文件。你可以在这里找到我的一些示例： <https://github.com/FaserF/WindowsPostInstaller/tree/master/autounattend><br />

查看 <https://github.com/netbootxyz/netboot.xyz/discussions/757><br />

## 支持

有问题或麻烦吗？

你可以在这里 [开一个问题][issue] GitHub。
请记住，此软件仅在 armv7 上的 Raspberry Pi 4 上经过测试。

### 已知问题
1. 在 PXE 启动后，若不在路由器的设置中配置 PXE DHCP 选项，引导将会出现多次超时<br />
2. 对 boot.cfg 的更改似乎被 netboot.xyz 忽略。它将始终使用默认配置。 <https://github.com/netbootxyz/netboot.xyz/discussions/861> <br />

## 作者与贡献者

该程序最初来自 Netboot.xyz 项目。有关更多信息，请访问此页面： <https://netboot.xyz/>
hassio 附加组件由 [FaserF] 带给你。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 FaserF & Netboot.xyz 项目

特此免费授予任何获得本软件及相关文档文件（统称“软件”）副本的人在不受限制的情况下处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售软件副本的权利，以及允许此软件被提供给的人这样做，前提是满足以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或实质性部分中。

本软件按“原样”提供，不提供任何明示或暗示的担保，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人都不对因软件或使用或其他交易中的软件而引起的任何索赔、损害或其他责任负责，无论是合同、侵权或其他形式。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues