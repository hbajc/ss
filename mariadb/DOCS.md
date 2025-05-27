# Home Assistant 附加组件: MariaDB

## 安装

按照以下步骤在您的系统上安装附加组件：

1. 在您的 Home Assistant 前端导航到 **设置** -> **附加组件** -> **附加组件商店**。
2. 找到 "MariaDB" 附加组件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

1. 将 `logins` -> `password` 字段设置为强且独特的密码。
2. 启动附加组件。
3. 检查附加组件日志输出以查看结果。
4. 将 `recorder` 集成添加到您的 Home Assistant 配置中。

## 附加组件配置

MariaDB 服务器附加组件可以根据您的喜好进行调整。本节描述了每个附加组件配置选项。

示例附加组件配置：

```yaml
databases:
  - homeassistant
logins:
  - username: homeassistant
    password: PASSWORD
  - username: read_only_user
    password: PASSWORD
rights:
  - username: homeassistant
    database: homeassistant
  - username: read_only_user
    database: homeassistant
    privileges:
      - SELECT
```

### 选项: `databases` (必需)

数据库名称，例如 `homeassistant`。可以指定多个数据库。

### 选项: `logins` (必需)

本节定义了在 MariaDB 中创建用户的定义。[创建用户][createuser] 文档。

### 选项: `logins.username` (必需)

数据库用户登录，例如 `homeassistant`。[用户名][username] 文档。

### 选项: `logins.password` (必需)

用户登录的密码。应为强且独特的密码。

### 选项: `rights` (必需)

本节为 MariaDB 中的用户授予权限。[授权][grant] 文档。

### 选项: `rights.username` (必需)

应与 `logins` -> `username` 中定义的用户名相同。

### 选项: `rights.database` (必需)

应与 `databases` 中定义的数据库相同。

### 选项: `rights.privileges` (可选)

授予该用户的权限列表，如 `[grant][grant]` 中的 `SELECT` 和 `CREATE`。
如果省略，则授予用户 `ALL PRIVILEGES`。不建议限制 Home Assistant 使用的用户的权限，但如果您希望其他应用程序查看记录器数据，则应创建一个用户以限制对数据库的只读访问。

### 选项: `mariadb_server_args` (可选)

一些用户在大型数据库的 Home Assistant 模式更新中遇到了 [错误][migration-issues]。
定义推荐参数可以帮助，但需确保有可用的 RAM。

示例: `--innodb_buffer_pool_size=512M`

## Home Assistant 配置

MariaDB 将用于 Home Assistant 中的 `recorder` 和 `history` 组件。有关设置的更多信息，请参阅 Home Assistant 的 [recorder 集成][mariadb-ha-recorder] 文档。

示例 Home Assistant 配置：

```yaml
recorder:
  db_url: mysql://homeassistant:password@core-mariadb/homeassistant?charset=utf8mb4
```

## 支持

有问题吗？

您有多个选项来获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子论坛][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了错误，请 [在我们的 GitHub 上提出问题][issue]。

[createuser]: https://mariadb.com/kb/zh/create-user/
[username]: https://mariadb.com/kb/zh/create-user/#user-name-component
[hostname]: https://mariadb.com/kb/zh/create-user/#host-name-component
[grant]: https://mariadb.com/kb/zh/grant/
[migration-issues]: https://github.com/home-assistant/core/issues/125339
[mariadb-ha-recorder]: https://www.home-assistant.io/integrations/recorder/
[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository