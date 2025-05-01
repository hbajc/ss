# Home Assistant Community Add-on: phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。常用的操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面执行，同时您仍然可以直接执行任何 SQL 语句。

该插件专门设计用于管理官方 Home Assistant MariaDB 插件。

## 安装

安装此插件非常简单，与安装其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮，在您的 Home Assistant 实例中打开该插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“phpMyAdmin”插件。
1. 享受该插件！

## 配置

**注意**：_请记得在更改配置后重新启动插件。_

示例插件配置：

```yaml
log_level: info
```

**注意**：_这只是一个示例，请不要复制粘贴！自己创建一个！_

### 选项: `upload_limit`

默认情况下，上传大小限制（用于导入等操作）设置为 64MB。可以通过此选项进行增加，例如，`100` 将为 100MB。

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或 less 详细，这在您处理未知问题时可能非常有用。可能的值有：

- `trace`: 显示每一个细节，比如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不错误的特殊情况。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 发生了可怕的错误。插件变得不可用。

请注意，每个级别自动包括更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排除故障。

## 已知问题和限制

- 此插件需要核心 MariaDB 插件版本 2.0 或更高版本。
- 此插件用于管理官方 Home Assistant MariaDB 插件。它不能连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志与发布

该存储库使用 [GitHub 的发布][releases] 功能记录变更日志。

发布基于 [语义化版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行增加：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种方法可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您还可以在这里 [打开一个问题][issue] GitHub。

## 作者 & 贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2021-2025 Franck Nijhof

特此免费授予任何获得此软件及相关文档文件（统称“软件”）的个人以处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售软件的副本，并允许向其提供软件的人员按以下条件这样做：

上述版权声明和本许可声明应包含在软件的所有副本或实质性部分中。

软件“按原样”提供，不提供任何种类的明示或暗示的保证，包括但不限于对适销性、特定用途的适用性和非侵权的保证。在任何情况下，作者或版权持有者不对因与软件或软件的使用或其他交易相关的任何索赔、损害或其他责任负责，无论是合同诉讼、侵权还是其他。

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