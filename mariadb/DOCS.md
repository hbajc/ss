# Home Assistant 附加组件：MariaDB

## 安装

按照以下步骤在您的系统上安装附加组件：

1. 在 Home Assistant 前端导航到 **设置** -> **附加组件** -> **附加组件商店**。
2. 找到 "MariaDB" 附加组件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

1. 将 `logins` -> `password` 字段设置为安全且唯一的密码。
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

### 选项：`databases`（必需）

数据库名称，例如 `homeassistant`。允许多个。

### 选项：`logins`（必需）

本节定义了在 MariaDB 中创建用户的设置。 [创建用户][createuser] 文档。

### 选项：`logins.username`（必需）

数据库用户登录名，例如 `homeassistant`。 [用户名][username] 文档。

### 选项：`logins.password`（必需）

用户登录的密码。应为安全且独特的密码。

### 选项：`rights`（必需）

本节授予用户在 MariaDB 中的权限。 [授予][grant] 文档。

### 选项：`rights.username`（必需）

这应该是 `logins` -> `username` 中定义的相同用户名。

### 选项：`rights.database`（必需）

这应该是 `databases` 中定义的相同数据库。

### 选项：`rights.privileges`（可选）

要授予此用户的权限列表，如 [授予][grant] 中的 `SELECT` 和 `CREATE`。
如果省略，则授予用户 `ALL PRIVILEGES`。限制 Home Assistant 使用的用户权限是不推荐的，但如果您希望允许其他应用程序查看录制数据，应该创建一个限制为只读访问数据库的用户。

### 选项：`mariadb_server_args`（可选）

一些用户在 Home Assistant 对大型数据库进行架构更新时遇到了 [错误][migration-issues]。
定义推荐的参数可以在有足够 RAM 的情况下有所帮助。

示例：`--innodb_buffer_pool_size=512M`

## Home Assistant 配置

MariaDB 将由 Home Assistant 中的 `recorder` 和 `history` 组件使用。有关如何设置此功能的更多信息，请参见 Home Assistant 的 [recorder 集成][mariadb-ha-recorder] 文档。

示例 Home Assistant 配置：

```yaml
recorder:
  db_url: mysql://homeassistant:password@core-mariadb/homeassistant?charset=utf8mb4
```

## 支持

有问题？

您有几种选项可以获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

如果您发现了错误，请 [在我们的 GitHub 上打开一个问题][issue]。

[createuser]: https://mariadb.com/kb/en/create-user/
[username]: https://mariadb.com/kb/en/create-user/#user-name-component
[hostname]: https://mariadb.com/kb/en/create-user/#host-name-component
[grant]: https://mariadb.com/kb/en/grant/
[migration-issues]: https://github.com/home-assistant/core/issues/125339
[mariadb-ha-recorder]: https://www.home-assistant.io/integrations/recorder/
[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository