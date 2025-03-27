# Home Assistant 插件：yarr

又一个 RSS 阅读器！

## 安装

将此库添加到您的 [Hass.io](https://home-assistant.io/hassio/) 实例中：

`https://github.com/einschmidt/hassio-addons`

如果遇到问题，您可以参考 [官方文档](https://home-assistant.io/hassio/installing_third_party_addons/)。

然后安装 "yarr!" 插件。

## 配置

**注意**：_当配置更改时，请记得重启插件。_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁的输出，这在处理未知问题时可能会很有用。可能的值有：

- `trace`：显示每一个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常事件，但不是错误。
- `error`：运行时错误，通常无需立即处理。
- `fatal`：出现严重错误，插件变得无法使用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

### 选项：`login.username`

设置 yarr 的登录用户名。不能为空。

### 选项：`login.password`

设置 yarr 的登录密码。不能为空。

### 选项：`ssl`

启用/禁用 yarr 的 Web 界面的 SSL（HTTPS）！
设置为 `true` 以启用，其他情况设为 `false`。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项：`db_path`

此选项允许您覆盖默认的数据库文件存储路径。例如，使用不同的配置，如 `/share/yarr/yarr.db`，而不是 `/data/yarr.db`。

如果未配置，该插件将自动使用默认路径：`/data/yarr.db`。