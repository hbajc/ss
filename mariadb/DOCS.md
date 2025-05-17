# Home Assistant 扩展：MariaDB

## 安装

按照以下步骤在您的系统上安装扩展：

1. 在 Home Assistant 前端导航到 **设置** -> **附加组件** -> **附加组件商店**。
2. 找到 "MariaDB" 扩展并点击它。
3. 点击 "安装" 按钮。

## 如何使用

1. 将 `logins` -> `password` 字段设置为一个强而唯一的密码。
2. 启动扩展。
3. 检查扩展日志输出以查看结果。
4. 将 `recorder` 集成添加到您的 Home Assistant 配置中。

## 扩展配置

可以根据自己的喜好调整 MariaDB 服务器扩展。此部分描述了每个扩展配置选项。

示例扩展配置：

```yaml
databases:
  - homeassistant
logins:
  - username: homeassistant
    password: 密码
  - username: read_only_user
    password: 密码
rights:
  - username: homeassistant
    database: homeassistant
  - username: read_only_user
    database: homeassistant
    privileges:
      - SELECT
```

### 选项：`databases`（必填）

数据库名称，例如 `homeassistant`。允许多个。

### 选项：`logins`（必填）

此部分定义在 MariaDB 中创建用户的定义。 [创建用户][createuser] 文档。

### 选项：`logins.username`（必填）

数据库用户登录名，例如 `homeassistant`。 [用户名][username] 文档。

### 选项：`logins.password`（必填）

用户登录的密码。应当是强而唯一的。

### 选项：`rights`（必填）

此部分授予 MariaDB 中用户的特权。 [授权][grant] 文档。

### 选项：`rights.username`（必填）

这应该与 `logins` -> `username` 中定义的用户名相同。

### 选项：`rights.database`（必填）

这应该与 `databases` 中定义的数据库相同。

### 选项：`rights.privileges`（可选）

授予此用户的特权列表，来自 [grant][grant]，如 `SELECT` 和 `CREATE`。
如果省略，将授予用户 `ALL PRIVILEGES`。限制 Home Assistant 使用的用户的特权
并不推荐，但如果您想允许其他应用程序
查看记录器数据，应该创建一个仅限于只读访问该数据库的用户。

### 选项：`mariadb_server_args`（可选）

一些用户在大型数据库上进行 Home Assistant 模式更新时遇到 [错误][migration-issues]。
定义推荐的参数可以在有可用 RAM 时提供帮助。

示例：`--innodb_buffer_pool_size=512M`

## Home Assistant 配置

MariaDB 将被 Home Assistant 中的 `recorder` 和 `history` 组件使用。有关设置的更多信息，请参阅 [recorder 集成][mariadb-ha-recorder] 文档。

示例 Home Assistant 配置：

```yaml
recorder:
  db_url: mysql://homeassistant:password@core-mariadb/homeassistant?charset=utf8mb4
```

## 支持

有问题吗？

您有几种方式可以得到答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

如果您发现了一个错误，请 [在我们的 GitHub 上打开一个问题][issue]。

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