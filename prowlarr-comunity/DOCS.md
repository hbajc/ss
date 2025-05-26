# Home Assistant Community Add-on: Prowlarr

基于流行的arr栈构建的索引管理器/代理，以集成您的各种PVR应用程序。

## 安装

该插件的安装非常简单，与安装任何其他Home Assistant插件没有不同。

1. 点击下面的Home Assistant我的按钮，以打开您Home Assistant实例上的插件。

   [![在您的Home Assistant实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装该插件。
1. 启动“Prowlarr”插件
1. 检查“Prowlarr”插件的日志以查看是否一切正常。
1. 点击“打开Web界面”以打开Prowlarr界面。
1. 完成屏幕上显示的向导。

## 配置

_该插件无需任何配置即可运行。_

## 已知问题和限制

- 此插件不支持Home Assistant的Ingress功能（即，将插件放入Home Assistant侧边栏的切换）。需要考虑的变量太多，无法使其正常工作，如果这样做，很容易破坏。您可以考虑使用iframe面板。

## 更新日志与发布

该存储库使用[GitHub的发布][releases]功能保持变更日志。

发布基于[语义版本控制][semver]，并使用`MAJOR.MINOR.PATCH`的格式。简而言之，版本将根据以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强功能。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题？

您有多种选择可以获得答案：

- [Home Assistant社区插件Discord聊天服务器][discord]以获取插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]以进行一般Home Assistant讨论和提问。
- Home Assistant [社区论坛][forum]。
- 在[/r/homeassistant][reddit]中加入[Reddit子论坛][reddit]。

您还可以在这里[提交问题][issue]到GitHub。

## 作者与贡献者

该存储库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权 (c) 2024 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，不受限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或销售软件副本的权利，并允许提供软件的人这样做，须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或实质性部分中。

本软件是按“原样”提供的，不提供任何形式的担保，无论是明示或暗示，包括但不限于对适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有者均不对因使用或与软件或使用或其他交易相关的任何索赔、损害或其他责任承担责任，无论是合同诉讼、侵权或其他诉讼。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_prowlarr&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-prowlarr/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-prowlarr/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-prowlarr/releases
[semver]: http://semver.org/spec/v2.0.0.html