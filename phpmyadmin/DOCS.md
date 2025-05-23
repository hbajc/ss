# Home Assistant 社区插件：phpMyAdmin

phpMyAdmin是用于MySQL和MariaDB的数据库管理工具。可以通过用户界面执行常用操作（管理数据库、表、列、关系、索引、用户、权限等），同时仍然能够直接执行任何SQL语句。

此插件专门设计用于管理官方的Home Assistant MariaDB插件。

## 安装

此插件的安装相当简单，与安装其他Home Assistant插件没有太大区别。

1. 单击下面的 Home Assistant My 按钮，在您的 Home Assistant 实例中打开插件。

   [![在您的 Home Assistant 实例中打开该插件。][addon-badge]][addon]

1. 单击“安装”按钮以安装插件。
1. 启动“phpMyAdmin”插件。
1. 享受插件的功能！

## 配置

**注意**：_更改配置时，请记得重新启动插件。_

插件配置示例：

```yaml
log_level: info
```

**注意**：_这只是一个示例，不要复制粘贴！请创建您自己的配置！_

### 选项：`upload_limit`

默认情况下，上传的大小限制（对于导入等操作）被设置为64MB。可以通过此选项增加，例如，`100`将是100MB。

### 选项：`log_level`

`log_level`选项控制插件的日志输出级别，可以更改为更详细或更少详细，这在您处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常是）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，但不需要立即处理。
- `fatal`：发生了严重错误，插件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug`还会显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐的设置，除非您正在进行故障排除。

## 已知问题和限制

- 此插件需要核心的MariaDB插件版本2.0或更高版本。
- 此插件是为管理官方的Home Assistant MariaDB插件而创建的。它无法连接到其他MySQL或MariaDB服务器。

## 更新日志和发布

该仓库使用[GitHub的发布][releases]功能维护变更日志。

发布基于[语义版本控制][semver]，格式为`MAJOR.MINOR.PATCH`。简单来说，版本将基于以下方面进行增量更新：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有多种方式可以获得答案：

- [Home Assistant社区插件Discord聊天服务器][discord]以获取插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]以进行一般的Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入Reddit子论坛[/r/homeassistant][reddit]。

您还可以在这里[开一个问题][issue]GitHub。

## 作者与贡献者

该仓库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权 (c) 2021-2025 Franck Nijhof

在此特此授予任何获取本软件及其相关文档文件（“软件”）副本的个人免费许可，以不受限制地处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售该软件副本的权利，并允许向其提供该软件的人这样做，前提是遵守以下条件：

上述版权声明和本许可声明应包含在该软件的所有副本或实质性部分中。

该软件“按现状”提供，不附有任何类型的明示或暗示的保证，包括但不限于对适销性、特定用途适用性和不侵权的保证。在任何情况下，作者或版权持有人都不对因使用该软件或其他交易而引起的任何索赔、损害或其他责任承担责任，无论是合同、侵权或其他形式。

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