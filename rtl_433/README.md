# rtl_433 Home Assistant 插件

## 关于

这个插件是一个简单的包装器，围绕着优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，该项目通过 [支持的 SDR 加密狗之一](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式（包括 JSON 和 MQTT）输出。 rtl_433 理解的无线传感器主要在 433.92 MHz、868 MHz、315 MHz、345 MHz 和 915 MHz ISM 频段上发送数据。

[查看 rtl_433 文档](https://triq.org/rtl_433)

## 工作原理

这个插件唯一的作用是通过 Home Assistant OS 主管运行 rtl_433。您需要做的就是提供一个配置文件。

默认情况下，rtl_433 将接收到的数据打印到终端-您可以配置它将数据发布到 MQTT，以便 Home Assistant 能够访问，这可以通过配置文件中的一行实现。

一旦您将 rtl_433 传感器数据放入 MQTT，您需要帮助 Home Assistant 发现并理解它。您可以通过多种方式做到这一点：

  * 手动配置 HA 中的 `sensors` 和 `binary_sensors`，并 [将它们链接到从 rtl_433 输出的适当 MQTT 主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动或定期运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本以自动完成大部分配置，或者
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，它为您运行 rtl_433_mqtt_hass.py。

## 先决条件

要使用此插件，您需要以下内容：

 1. [一个由 rtl_433 支持的 SDR 加密狗](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在安装了 SDR 加密狗的机器上运行 Home Assistant OS。

 3. 一些由 rtl_433 支持的无线传感器。完整的支持协议和设备列表可以在 [rtl_433 的 README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的 "支持设备协议" 部分找到。

## 安装

 1. 创建一个满足您需求的 rtl_433 配置文件。如果您在运行 Home Assistant OS 以外的计算机上执行此操作，它可能会更顺利，以便您可以自由实验并迭代，直到得出一个好的配置。有关更多详细信息，请参见下文。

 2. 使用适合您的任何方法（通过 Samba 插件、ssh/scp、文件编辑器插件等）将配置文件上传到 Home Assistant 的 "/config" 目录中。

 3. 安装插件。

 5. 将 SDR 加密狗插入运行插件的机器。

 5. 启动插件。默认配置将创建在 `/config/rtl_433/` 中。要添加或编辑额外的配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于 "零配置" 设置，请安装 [Mosquitto 代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。虽然其他代理可能有效，但它们未经测试并且需要手动设置。一旦插件安装完成，启动或重新启动 rtl_433 和 rtl_433_mqtt_autodiscovery 插件以开始捕获已知的 433 MHz 协议。

有关更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含 bash 变量，**美元符号和其他特殊 shell 字符需要转义**。例如，若要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志默认是否启用。可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来逐个无线电进行覆盖。

在手动配置时，假设您希望将 rtl_433 数据导入到 Home Assistant，您在配置文件中需要指定的绝对最小值是 [MQTT 连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认收听 433.92MHz，但即使这就是您需要的，明确指定频率也许是个好主意，以避免混淆：

```
frequency   433.92M
```

您可能还希望缩小 rtl_433 应该尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的 "支持设备协议" 部分找到。假设您希望收听 Acurite 592TXR 温湿度传感器：

```
protocol    40
```

最后但并非最不重要的是，如果您决定使用 MQTT 自动发现脚本或插件，其文档建议将 rtl_433 输出的所有数据转换为 SI 单位：

```
convert     si
```

假设您只有一个 USB 加密狗连接，并且 rtl_433 能够自动找到它，我们得到了一个最小的 rtl_433 配置文件，如下所示：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查阅 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf) 以获取更多信息。

## 鸣谢

此插件基于 James Fry 的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，该插件又基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而该项目又基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。