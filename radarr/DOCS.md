# Home Assistant Community Add-on: Radarr

电影组织/管理器，适用于 usenet 和 torrent 用户。

## 安装

此附加组件的安装非常简单，与安装任何其他 Home Assistant 附加组件没有区别。

1. 单击下面的 Home Assistant My 按钮以打开您 Home Assistant 实例上的附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

1. 单击“安装”按钮以安装附加组件。
1. 启动“Radarr”附加组件
1. 检查“Radarr”附加组件的日志以查看一切是否正常。
1. 单击“打开网页 UI”以打开 Radarr 界面。
1. 完成屏幕上显示的向导。

## 配置

_此附加组件不需要任何配置即可运行。_

## 已知问题和限制

- 此附加组件不支持 Home Assistant 的 Ingress 功能（即将附加组件放入 Home Assistant 侧边栏的切换开关）。
  需要考虑的变量太多以使其正常工作，如果我们这样做，很容易就会出现故障。您可以考虑使用 iframe 面板代替。

## 更新日志和发布

此代码库使用 [GitHub 的发布][releases] 功能保持更改日志。

发布基于 [语义版本控制][semver]，采用 `MAJOR.MINOR.PATCH` 格式。简言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 bug 修复和软件包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获取附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以进行一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以在这里 [打开一个问题][issue] GitHub。

## 作者和贡献者

这个代码库的最初设置者是 [Franck Nijhof][frenck]。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2024-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，在不受限制的条件下处理该软件，包括不限于使用、复制、修改、合并、发布、分发、再授权和/或销售该软件副本的权利，并允许提供软件的人这样做，须遵守以下条件：

上述版权声明和本许可声明应包含在所有软件副本或实质性部分中。

软件是按照“现状”提供的，不提供任何种类的明示或暗示的担保，包括但不限于对适销性、特定目的适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对因使用软件或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

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