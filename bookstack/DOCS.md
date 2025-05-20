# Home Assistant 社区附加组件：Bookstack

BookStack 是一个简单、自托管、易于使用的信息组织和存储平台。请支持该软件的开发者，[Bookstack].

## 安装

该附加组件的安装非常简单，与安装任何其他 Home Assistant 附加组件没有不同。

1. 在附加组件商店中搜索 "bookstack" 附加组件并安装它。
1. 启动 "bookstack" 附加组件
1. 检查 "bookstack" 附加组件的日志，以查看一切是否顺利。
1. 默认登录信息是 admin@admin.com/password。

## 配置

**注意**：_在更改配置时，请记得重启附加组件。_

附加组件配置示例：

```yaml
log_level: info
ssl: false
certfile: fullchain.pem
keyfile: privkey.pem
envvars:
  - name: SESSION_COOKIE_NAME
    value: bookstack_session
```

**注意**：_这只是一个示例，不要复制粘贴！请创建您自己的！_

### 选项： `log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会有用。可能的值包括：

- `trace`: 显示每一个细节，比如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 运行时错误，不需要立即采取措施。
- `fatal`: 出现严重错误，附加组件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项： `ssl`

在 Bookstack 面板的 Web 界面上启用/禁用 SSL（HTTPS）。设置为 `true` 以启用，设置为 `false` 则禁用。

### 选项： `certfile`

用于 SSL 的证书文件。

**注意**：_该文件必须存储在 `/ssl/`，这是默认位置_

### 选项： `keyfile`

用于 SSL 的私钥文件。

**注意**：_该文件必须存储在 `/ssl/`，这是默认位置_

### 选项： `remote_mysql_host`

如果使用外部数据库，MYSQL/MariaDB 数据库的主机名/地址。

### 选项： `remote_mysql_database`

仅在使用远程 MYSQL 数据库时适用，数据库的名称。

### 选项： `remote_mysql_username`

仅在使用远程 MYSQL 数据库时适用，具有权限的用户名。

### 选项： `remote_mysql_password`

仅在使用远程 MYSQL 数据库时适用，上述用户的密码。

### 选项： `remote_mysql_port`

仅在使用远程 MYSQL 数据库时适用，数据库服务器监听的端口。

### 选项： `show_appkey`

如果设置为 `true`，将在附加组件日志中显示当前配置的 appkey。这应该在还原时记录下来。

### 选项： `appkey`

允许用户定义 appkey，以便于从其他系统还原。如果设置，将在第一次运行时自动从配置中删除。

### 选项： `envvars`

这允许设置环境变量以控制 Bookstack 配置，具体文档请见：

<https://www.bookstackapp.com/docs/>

**注意**：_更改这些选项可能会对您的实例造成问题。请自行承担风险！_

这些选项对大小写敏感，特定配置设置的任何项将优先于其他。

#### 子选项： `name`

要设置的环境变量的名称。

#### 子选项： `value`

要设置的环境变量的值。

## 数据库使用

默认情况下，Bookstack 会自动使用和配置 Home Assistant 的 MariaDB 附加组件，该附加组件应在启动前安装，您可以在配置中更改，以使用外部 MySql/MariaDB 数据库。请注意，两种选项之间没有简单的升级路径。

## 已知问题和限制

- 由于应用程序存储图像文件的方式，Ingress 将无法正常工作。

## 更新日志与发布

该仓库使用 [GitHub 的发布][releases] 功能保留变更日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强功能。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- Home Assistant 社区附加组件 Discord 聊天服务器 [discord] 用于附加组件支持和功能请求。
- Home Assistant Discord 聊天服务器 [discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 的 [/r/homeassistant][reddit]

您还可以在 [这里打开问题][issue] GitHub。

## 作者与贡献者

该仓库的原始设置由 [Paul Sinclair][sinclairpaul] 创建。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2019-2025 Paul Sinclair

特此免费授予获得此软件及相关文档文件（“软件”）副本的任何人，无限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售软件的副本，并允许提供软件的人员这样做，遵循以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质性部分中。

该软件是“按原样”提供的，不提供任何形式的担保，明示或暗示，包括但不限于适销性、适合特定目的和非侵权的担保。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面，均由于、因或与软件或使用或其他交易的关系而引起。

[bookstack]: https://www.bookstackapp.com/
[contributors]: https://github.com/hassio-addons/addon-bookstack/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/community-hass-io-xxxxx/xxxxx
[sinclairpaul]: https://github.com/sinclairpaul
[issue]: https://github.com/hassio-addons/addon-bookstack/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-bookstack/releases
[semver]: http://semver.org/spec/v2.0.0