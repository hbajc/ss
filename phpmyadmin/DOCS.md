# Home Assistant Community Add-on: phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。经常使用的操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面进行，同时您仍然可以直接执行任何 SQL 语句。

此附加组件专门设计用于管理官方的 Home Assistant MariaDB 附加组件。

## 安装

安装此附加组件相当简单，与安装其他 Home Assistant 附加组件没有什么不同。

1. 点击下面的 Home Assistant 我的按钮以在您的 Home Assistant 实例中打开该附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装附加组件。
1. 启动“phpMyAdmin”附加组件。
1. 享受该附加组件！

## 配置

**注意**：_记得在更改配置时重新启动附加组件。_

示例附加组件配置：

```yaml
log_level: info
```

**注意**：_这只是一个示例，不要复制粘贴！创建您自己的！_

### 选项：`upload_limit`

默认情况下，上传的大小限制（用于导入等操作）设置为 64MB。可以通过此选项增加，例如，`100` 将是 100MB。

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，并可以调整为更详细或更简略，这在您处理未知问题时可能会很有用。可能的值包括：

- `trace`: 显示每个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）感兴趣的事件。
- `warning`: 不属于错误的特殊事件。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 某些事情严重出错。附加组件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

## 已知问题和限制

- 此附加组件需要核心 MariaDB 附加组件版本 2.0 或更高版本。
- 此附加组件用于管理官方 Home Assistant MariaDB 附加组件。它无法连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志与版本

此存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

版本基于 [语义版本控制][semver]，并采用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本会基于以下内容进行递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有多个选项可以获取答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子板块][reddit] 在 [/r/homeassistant][reddit]。

您还可以在这里 [提交问题][issue] 到 GitHub。

## 作者与贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

欲查看所有作者和贡献者的完整列表，请检查 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2021-2025 Franck Nijhof

特此免费授予任何获取本软件及相关文档文件（“软件”）副本的人，处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售该软件副本的权利，并允许向其提供软件的人这样做，前提是符合以下条件：

上述版权声明和此许可声明应包含在所有副本或软件的实质性部分中。

软件是“按原样”提供的，不提供任何形式的担保，无论是明示或暗示，包括但不限于对适销性、特定用途的适用性和不侵权的担保。在任何情况下，作者或版权持有人对于因使用软件或其他交易引起或与之相关的任何索赔、损害或其他责任，均不承担责任，无论是在合同诉讼、侵权或其他情况下。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_phpmyadmin&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-phpmyadmin/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-phpmyadmin/171729?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-phpmyadmin/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-phpmyadmin/releases
[semver]: https://semver.org/spec/v2.0.0.html