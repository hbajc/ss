# ESPHome 开发附加组件

这是 **开发** 版本的 ESPHome 附加组件。

要部署生产节点，请使用主流发布附加组件。

该附加组件使用的版本是每天在 UTC 02:00 自动构建的 ESPHome，用于测试开发中的组件。请查看下面的 `esphome_fork` 配置以正确配置附加组件。一旦您更新了配置，请确保重新构建镜像。

## 配置

**注意**：_在更改配置时，请记得重启附加组件。_

### 选项：`esphome_fork`

从分支或分叉安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分叉所有者的用户名和分支 `username:branch`，这假设仓库仍然命名为 `esphome`。

如果您需要在镜像更新之前测试开发分支上的最新提交，可以在这里输入 `dev`。

请注意，您使用的分叉或分支 **必须** 与 ESPHome 开发版保持最新，
否则附加组件 **将无法启动**。

## 通用 ESPHome 附加组件配置

通用选项在其他版本中也可用。

### 选项：`ssl`

启用或禁用该附加组件的 web 服务器的加密 SSL/TLS（HTTPS）连接。
将其设置为 `true` 以加密通信，否则设置为 `false`。
请注意，如果您将其设置为 `true`，还必须为加密生成密钥和证书文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果此文件不存在，附加组件将启动失败。

**注意**：该文件必须存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果此文件不存在，附加组件将启动失败。

**注意**：该文件必须存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`leave_front_door_open`

将此选项添加到附加组件配置中可以通过将其设置为 `true` 来禁用
身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 控制面板，以便它可以集成到现有的 Web 代理中，例如在相对 URL 下的 NGINX。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，控制面板使用 mDNS 检查节点是否在线。这在不同子网之间不会工作，除非您的路由器支持 mDNS 转发或 avahi。

将其设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点在连接时始终显示离线状态，请使用此设置。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防在编辑和验证时这些信息也被显示。