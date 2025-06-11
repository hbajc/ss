# Home Assistant Community Add-on: phpMyAdmin

phpMyAdmin 是一个用于 MySQL 和 MariaDB 的数据库管理工具。可以通过用户界面执行常用操作（管理数据库、表、列、关系、索引、用户、权限等），同时仍然能够直接执行任何 SQL 语句。

这个附加组件是专门设计用来管理官方 Home Assistant MariaDB 附加组件的。

## 安装

安装这个附加组件非常简单，和安装其他 Home Assistant 附加组件没有区别。

1. 点击下面的 Home Assistant My 按钮，以在您的 Home Assistant 实例中打开附加组件。

   [![在您的 Home Assistant 实例中打开这个附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装附加组件。
1. 启动“phpMyAdmin”附加组件。
1. 享受这个附加组件吧！

## 配置

**注意**：_记得在配置更改时重启附加组件。_

示例附加组件配置：

```yaml
log_level: info
```

**注意**：_这只是一个示例，请不要复制粘贴！请创建您自己的！_

### 选项：`upload_limit`

默认情况下，上传的大小限制（用于导入等操作）设置为 64MB。可以通过此选项增加，例如，`100` 将是 100MB。

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值有：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常发生，但不是错误。
- `error`：运行时错误，不需要立即处理。
- `fatal`：发生了严重错误，附加组件变得不可用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您在进行故障排除。

## 已知问题和限制

- 这个附加组件需要核心的 MariaDB 附加组件版本 2.0 或更高。
- 这个附加组件是为管理官方 Home Assistant MariaDB 附加组件而创建的。它不能连接到其他 MySQL 或 MariaDB 服务器。

## 更新日志与版本

这个仓库使用 [GitHub 的版本][releases] 功能维护更改日志。

版本基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将基于以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题？

您有几种选择来获取答案：

- [Home Assistant Community Add-ons Discord 频道][discord] 以获取附加组件支持和功能请求。
- [Home Assistant Discord 频道][discord-ha] 进行一般 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您也可以在这里 [打开问题][issue] GitHub。

## 作者与贡献者

这个仓库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021-2025 Franck Nijhof

特此免费授予任何获得本软件及其相关文档文件（“软件”）副本的人使用软件的权利，包括无限制地使用、复制、修改、合并、出版、分发、再授权和/或出售软件副本的权利，并允许软件被提供给的人这样做，须遵守以下条件：

上述版权声明和本许可证声明应包含在所有软件的副本或实质部分中。

该软件按“原样”提供，不附有任何形式的明示或暗示的担保，包括但不限于对适销性、特定用途适用性及非侵权的担保。在任何情况下，作者或版权持有者对任何索赔、损害或其他责任不承担任何责任，无论是因合同、侵权或其他原因引起的，均不对软件或使用或其他交易中的责任承担责任。

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