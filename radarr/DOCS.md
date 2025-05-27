# Home Assistant Community Add-on: Radarr

用于usenet和torrent用户的电影组织/管理器。

## 安装

这个插件的安装非常简单，与安装任何其他Home Assistant插件没有什么不同。

1. 点击下面的Home Assistant My按钮以打开您Home Assistant实例中的插件。

   [![在您的Home Assistant实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“Radarr”插件
1. 检查“Radarr”插件的日志以查看一切是否正常。
1. 点击“打开WEB UI”以打开Radarr界面。
1. 完成屏幕上显示的向导。

## 配置

_这个插件运行不需要任何配置。_

## 已知问题和限制

- 这个插件不支持Home Assistant的Ingress功能（即，将插件放入Home Assistant侧边栏的切换）。
  需要考虑的变量太多，无法使其正常工作，如果我们这样做，很容易出现问题。您可以考虑使用iframe面板来代替。

## 更新日志和发布

这个仓库使用[GitHub的发布][releases]功能来保持变更日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将根据以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强功能。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题？

您有几种方式可以获得答案：

- 在[Home Assistant Community Add-ons Discord聊天服务器][discord]上获取插件支持和功能请求。
- 在[Home Assistant Discord聊天服务器][discord-ha]上进行一般Home Assistant讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入[/r/homeassistant][reddit]的[Reddit子版块][reddit]。

您还可以在这里[提交问题][issue]到GitHub。

## 作者与贡献者

这个仓库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2024-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（以下简称“软件”）副本的人，按照无任何限制的方式处理软件的权限，包括在不限制使用、复制、修改、合并、出版、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，享有所附带的以下条件：

上述版权声明和本许可证声明应包含在软件的所有副本或重要部分中。

该软件是“按原样”提供的，不提供任何类型的保证，明确或隐含，包括但不限于对适销性、特定用途适用性和不侵权的保证。在任何情况下，作者或版权持有人均不对因使用该软件或与该软件的使用或其他交易有关的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权或其他情况下。

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