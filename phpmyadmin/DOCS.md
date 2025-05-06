# Home Assistant 插件：phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。常用操作（管理数据库、表、列、关系、索引、用户、权限等）可以通过用户界面执行，同时您仍然可以直接执行任何 SQL 语句。

这个插件专门设计用于管理官方的 Home Assistant MariaDB 插件。

## 安装

请按照以下步骤在您的系统上安装插件：

添加仓库 `https://github.com/erik73/hassio-addons`。
找到“phpMyAdmin”插件并点击它。
点击“安装”按钮。

## 配置

**注意**：_在更改配置时，请记得重启插件。_

插件配置示例：

```yaml
log_level: info
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的配置！_

### 选项：`upload_limit`

默认情况下，上传的大小限制（例如导入操作）设置为 64MB。可以通过此选项增加，例如，`100` 将设置为 100MB。

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不是错误的异常情况。
- `error`：运行时错误，不需要立即处理。
- `fatal`：出现了严重错误。插件变得无法使用。

请注意，每个级别自动包含来自更高严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

## 已知问题和限制

- 此插件需要核心 MariaDB 插件版本 2.0 或更高版本。
- 此插件创建用于管理官方 Home Assistant MariaDB 插件。它无法连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志和版本

该仓库使用 [GitHub 的发布][releases] 功能维护更改日志。

版本基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您可以在这里 [提出问题][issue] GitHub。

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