# ESPHome 插件
## 安装

此插件的安装非常简单，与安装其他 Home Assistant 插件没有区别。

1. 在 Supervisor 插件商店中搜索 “ESPHome” 插件。
2. 按下安装以下载并解压插件到您的机器上。这可能需要一些时间。
3. 可选：如果您使用 SSL/TLS 证书，并希望加密与此插件的通信，请在 `ssl` 字段中输入 `true`，并相应地设置 `fullchain` 和 `certfile` 选项。
4. 启动插件，检查插件的日志以确保一切都正常。
5. 点击 "OPEN WEB UI" 打开 ESPHome 仪表板。系统会要求您输入您的 Home Assistant 凭据 - ESPHome 使用 Home Assistant 的认证系统进行登录。

您可以在 https://esphome.io/ 查看 ESPHome 文档。

## 配置

**注意**：_记得在更改配置时重启插件。_

示例插件配置：

```json
{
  "ssl": false,
  "certfile": "fullchain.pem",
  "keyfile": "privkey.pem"
}
```

### 选项： `ssl`

启用或禁用加密的 SSL/TLS (HTTPS) 连接到该插件的网络服务器。
将其设置为 `true` 以加密通信，反之则设置为 `false`。
请注意，如果您将其设置为 `true`，您还必须生成加密所需的密钥和证书文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于 SSL 的证书文件。如果此文件不存在，插件启动将会失败。

**注意**：该文件必须存储在 `/ssl/` 目录中，这是 Home Assistant 的默认位置。

### 选项： `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，插件启动将会失败。

**注意**：该文件必须存储在 `/ssl/` 目录中，这是 Home Assistant 的默认位置。

### 选项： `leave_front_door_open`

将此选项添加到插件配置中，可以通过将其设置为 `true` 来禁用认证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在 NGINX 之类的现有 Web 代理下集成相对 URL。默认值为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则这在子网之间是无效的。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使在连接时总是显示离线状态，请使用此选项。

### 选项： `streamer_mode`

如果设置为 `true`，将启用流媒体模式，使 ESPHome 隐藏所有潜在的私密信息。因此，例如 WiFi (B)SSIDs（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防止这些信息在编辑和验证过程中显示。