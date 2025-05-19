# Home Assistant Community Add-on: Radarr

电影组织者/管理器，适用于usenet和torrent用户。

## 安装

此附加组件的安装非常简单，与安装其他Home Assistant附加组件没有区别。

1. 点击下面的Home Assistant我的按钮以在您的Home Assistant实例中打开该附加组件。

   [![在您的Home Assistant实例中打开此附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装该附加组件。
1. 启动“Radarr”附加组件
1. 检查“Radarr”附加组件的日志，以查看一切是否顺利。
1. 点击“打开网页界面”以打开Radarr界面。
1. 完成屏幕上显示的向导。

## 配置

_此附加组件在运行时不需要任何配置。_

## 已知问题和限制

- 此附加组件不支持Home Assistant的Ingress功能（即将附加组件放入Home Assistant侧边栏的切换）。
  必须考虑的变量太多，以至于无法使其正常工作，如果我们这样做，很容易就会出错。您可以考虑使用iframe面板代替。

## 更新日志与版本

该存储库使用[GitHub的版本][releases]功能保留更改日志。

版本基于[语义化版本控制][semver]，并使用`MAJOR.MINOR.PATCH`格式。简单来说，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord聊天服务器][discord]，用于附加组件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]，用于一般的Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入[/r/homeassistant][reddit]的[Reddit子版块][reddit]。

您还可以在这里[报告问题][issue] GitHub。

## 作者与贡献者

该存储库的最初设置者是[Franck Nijhof][frenck]。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权 (c) 2024-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，在不受限制的情况下使用软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售软件副本的权利，以及允许向其提供软件的人这样做，但须符合以下条件：

上述版权声明和本许可声明应包括在所有软件的副本或实质性部分中。

该软件是按“现状”提供的，不附带任何形式的担保，无论是明示还是暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人对因使用软件或与软件或其他交易相关的任何索赔、损害或其他责任均不承担责任，无论是在合同、侵权或其他方面。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_radarr&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-radarr/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-radarr/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-radarr/releases
[semver]: http://semver.org/spec/v2.0.0.html