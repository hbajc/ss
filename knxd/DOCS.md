# Home Assistant Community Add-on: KNXD

## 安装

按照以下步骤在您的系统上安装该插件：

1. 在您的 Home Assistant 前端中导航至 **Supervisor** -> **Add-on Store**。
2. 如果您尚未将此插件库添加到您的 supervisor，点击右上角的菜单图标，选择 **Repositories**，添加 `https://github.com/da-anda/hass-io-addons` 作为新库，然后关闭对话框。
3. 找到 "KNXD" 插件并点击它。
4. 点击 "INSTALL" 按钮。

## 配置

插件配置：

```yaml
    "address": "0.0.1",
    "client_address": "0.0.2:8",
    "interface": "tpuart",
    "device": "/dev/ttyACM0",
    "usb_filters": "",
    "custom_config": ""
```

### 选项
这些选项的描述部分复制自 `knxd` [文档](https://github.com/knxd/knxd/blob/master/doc/inifile.rst)。您可以在这里找到更多示例和详细信息。

#### 选项 `address`

knxd 守护进程本身的 KNX 地址。用于例如来自组缓存的请求。

#### 选项 `client_address`

要分配给客户端连接的地址范围。请注意，长度参数表示要分配的地址数量。

示例：1.2.3:5（这为 knxd 的客户端分配地址 1.2.3 到 1.2.7。）

#### 选项 `interface`

`knxd` 应该使用的与 KNX 总线进行通信的接口驱动程序。对于该插件的典型用例，最常见的是：

- `tpuart`（用于基于 UART 的 KNX 接口，如来自 Busware.de 的接口）
- `usb`（用于商业 USB KNX 接口）

有关所有可能选项的完整列表，请参见 `knxd` 文档的 [drivers section](https://github.com/knxd/knxd/blob/master/doc/inifile.rst#drivers)。

#### 选项：`device`（某些接口可选）

您适配器在 Linux 中的物理设备地址。示例：

- **TPUART 接口**：`/dev/ttyACM0`
- **USB 接口**：您可以尝试将此留空，以便 `knxd` 自动检测您的设备。如果留空时无法正常工作，请尝试指定设备地址，例如 `/dev/ttyAMA0`。

请注意，这些地址是示例，可能与您的设备不同。要查找设备地址，您必须 SSH 进入主机操作系统（**NOT** supervisor！）并检查连接的设备。

#### 选项：`usb_filters`（可选）

使用 USB 接口时，您可以指定要使用的其他过滤器。有关更多信息，请参见官方 `knxd` 文档的 [filters section](https://github.com/knxd/knxd/blob/master/doc/inifile.rst#filters)。

#### 选项：`custom_config`（已废弃）

允许您编写自己的自定义 `knxd` ini 配置，而不是使用来自此插件的预制模板，该模板使用了上述所有其他配置选项。

您的自定义配置将替换此插件提供的默认配置，因此上述所有其他配置选项将被忽略。有关所有可能的配置选项，请参阅 [knxd 文档](https://github.com/knxd/knxd/blob/master/doc/inifile.rst)。

请注意，此配置选项在此插件的 0.6.0 版本中已废弃，并将在未来的更新中删除。您现在可以在此插件的相应 `addon_config` 目录中提供自定义 ini 配置文件。如果您还安装了此插件的相应插件，您可以通过网络共享（SMB）访问该目录。

## 支持

如果您有任何问题，请随时加入 HomeAssistant 社区并在 [add-on thread](https://community.home-assistant.io/t/knxd-add-on-covert-your-knx-usb-interface-into-an-ip-interface-that-can-be-used-by-ha/38108/38) 中提问。

如果您发现了错误，请随时在 [Github](https://github.com/da-anda/hass-io-addons/issues) 上创建一个问题单。