# Home Assistant 插件: phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。常用的操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面执行，同时您仍然可以直接执行任何 SQL 语句。

此插件专门设计用于管理官方 Home Assistant MariaDB 插件。

## 安装

按照以下步骤在您的系统上安装该插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到 "phpMyAdmin" 插件并点击它。
点击 "安装" 按钮。

## 配置

**注意**: _当配置更改时，请记得重启该插件。_

示例插件配置：

```yaml
log_level: info
```

**注意**: _这只是一个示例，请不要复制粘贴！自己创建一个！_

### 选项: `upload_limit`

默认情况下，上传的大小限制（用于导入等操作）设置为 64MB。可以通过此选项增加，例如，`100` 将为 100MB。

### 选项: `log_level`

`log_level` 选项控制插件输出日志的级别，可以更改为更详细或更简洁的日志，这在处理未知问题时可能会很有用。可能的值有：

- `trace`: 显示每一个细节，例如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）感兴趣的事件。
- `warning`: 特殊情况，并不表示错误。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 发生了严重错误。插件变得不可用。

请注意，每个级别会自动包含来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

## 已知问题和限制

- 此插件需要核心 MariaDB 插件版本 2.0 或更高。
- 此插件创建用于管理官方 Home Assistant MariaDB 插件。它无法连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志与发布

该仓库使用 [GitHub 的发布][releases] 功能来维护变更日志。

发布基于 [语义版本控制][semver]，采用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行增量更新：

- `MAJOR`: 不兼容或重大变更。
- `MINOR`: 向后兼容的新功能和增强功能。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您可以在 [此处提出问题][issue] GitHub。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_phpmyadmin&repository_url=https%3A%2F%2Fgithub.com%2Ferik73%2Frepository
[contributors]: https://github.com/erik73/addon-phpmyadmin/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-phpmyadmin/171729?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/erik73/addon-phpmyadmin/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/erik73/addon-phpmyadmin/releases
[semver]: https://semver.org/spec/v2.0.0.html