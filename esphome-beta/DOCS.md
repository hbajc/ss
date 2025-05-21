# ESPHome 附加组件
## 安装

这个附加组件的安装相当简单，与安装其他 Home Assistant 附加组件没有区别。

1. 在 Supervisor 附加组件商店中搜索 “ESPHome” 附加组件。
2. 按下安装以下载附加组件并将其解压到您的机器上。这可能需要一些时间。
3. 可选：如果您使用 SSL/TLS 证书并希望加密与该附加组件的通信，请在 `ssl` 字段中输入 `true`，并相应地设置 `fullchain` 和 `certfile` 选项。
4. 启动附加组件，检查附加组件的日志以查看一切是否正常。
5. 点击 “打开网页界面” 以打开 ESPHome 仪表板。你将需要输入你的 Home Assistant 凭据 - ESPHome 使用 Home Assistant 的认证系统来登录。

您可以访问 ESPHome 文档，网址为 https://esphome.io/

## 配置

**注意**：_请记住在更改配置时重启附加组件。_

附加组件配置示例：

```json
{
  "ssl": false,
  "certfile": "fullchain.pem",
  "keyfile": "privkey.pem"
}
```

### 选项： `ssl`

启用或禁用与该附加组件的网络服务器之间的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，`false` 则不加密。
请注意，如果您将其设置为 `true`，您还必须生成加密所需的密钥和证书文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于 SSL 的证书文件。如果该文件不存在，附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项： `keyfile`

用于 SSL 的私钥文件。如果该文件不存在，附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项： `leave_front_door_open`

将此选项添加到附加组件配置中，允许您通过将其设置为 `true` 来禁用身份验证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成到现有的 Web 代理（如 NGINX）下的相对 URL。 默认为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则此方法在子网之间无法工作。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使连接时也始终显示离线状态，则使用此选项。

### 选项： `streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有潜在的私密信息。例如 WiFi (B)SSIDs（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防止在编辑和验证时这些信息显示出来。