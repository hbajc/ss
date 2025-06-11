# Home Assistant Community Add-on: Prowlarr

构建于流行的 arr 栈之上的索引管理器/代理，以便与您的各种 PVR 应用程序集成。

## 安装

此附加组件的安装相当简单，与安装任何其他 Home Assistant 附加组件没有区别。

1. 点击下面的 Home Assistant 我的按钮以在您的 Home Assistant 实例中打开该附加组件。

   [![在您的 Home Assistant 实例中打开这个附加组件。][addon-badge]][addon]

1. 点击 “安装” 按钮以安装附加组件。
1. 启动 “Prowlarr” 附加组件。
1. 检查 “Prowlarr” 附加组件的日志，以查看一切是否顺利。
1. 点击 “打开网页 UI” 以打开 Prowlarr 界面。
1. 完成屏幕上显示的向导。

## 配置

_此附加组件无需任何配置即可运行。_

## 已知问题和限制

- 此附加组件不支持 Home Assistant 的 Ingress 功能（即将附加组件放入 Home Assistant 侧边栏的切换）。  
  考虑到太多变量使其正常工作，如果我们想要这样做，很容易就会破坏。您可以考虑使用 iframe 面板代替。

## 变更日志与发布

该存储库使用 [GitHub 的发布][releases] 功能保留变更日志。

发布基于 [语义版本控制][semver]，使用格式 `MAJOR.MINOR.PATCH`。简而言之，版本将基于以下内容进行增加：

- `MAJOR`:  不兼容或重大更改。
- `MINOR`: 向后兼容的新特性和增强功能。
- `PATCH`: 向后兼容的 bug 修复和包更新。

## 支持

有问题吗？

您有几种选择可以得到答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 提供附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您还可以在这里 [提交问题][issue] 到 GitHub。

## 作者与贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

##许可证

MIT 许可证

版权所有 (c) 2024 Franck Nijhof

特此免费授予任何获得此软件及其相关文档文件（“软件”）副本的人，使用软件的权利，不受限制，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售软件副本的权利，并允许向其提供软件的人这样做，具体条件如下：

上述版权声明和此许可声明应包含在软件的所有副本或实质性部分中。

软件是按 “原样” 提供的，不作任何类型的明示或暗示的保证，包括但不限于对适销性、特定用途的适用性和不侵权的保证。在任何情况下，作者或版权持有者均不对因软件或使用或其他交互而引起的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面。

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