# rtl_433 Home Assistant 插件

## 关于

这个插件是对优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目的一个简单封装，它通过 [一个支持的SDR接收器](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，并将其解码并以多种格式输出，包括JSON和MQTT。rtl_433理解的无线传感器主要在433.92 MHz、868 MHz、315 MHz、345 MHz和915 MHz ISM频段传输数据。

[查看rtl_433文档](https://triq.org/rtl_433)

## 工作原理

这个插件唯一的功能是在Home Assistant OS管理器下运行rtl_433。你只需提供一个配置文件。

默认情况下，rtl_433将接收到的数据打印到终端 - 你需要配置它将数据发布到MQTT，以便Home Assistant可以访问，这可以通过在配置文件中添加一行来完成。

一旦你将rtl_433传感器数据导入MQTT，你需要帮助Home Assistant发现并理解它。你可以通过多种方式做到这一点：

  * 在HA中手动配置`sensors`和`binary_sensors`，并 [将它们链接到从rtl_433发出的适当MQTT主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本或定时运行以自动进行大部分配置，或者
  * 安装 [rtl_433 MQTT自动发现Home Assistant插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，该插件为你运行rtl_433_mqtt_hass.py。

## 先决条件

要使用此插件，你需要以下内容：

 1. [一个支持rtl_433的SDR接收器](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在插入SDR接收器的机器上运行Home Assistant OS。

 3. 一些由rtl_433支持的无线传感器。支持的协议和设备的完整列表可以在[rtl_433的README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持设备协议”部分找到。

## 安装

 1. 创建一个rtl_433配置文件，满足你的需求。如果在运行Home Assistant OS的计算机以外的计算机上做这件事，可能会更好，这样你可以自由实验并反复修改，直到得到一个好的配置。详细信息见下文。

 2. 使用适合你的任何方法将配置文件上传到Home Assistant的"/config"目录（通过Samba插件、ssh/scp、文件编辑器插件等）。

 3. 安装插件。

 5. 将你的SDR接收器插入运行插件的机器。

 5. 启动插件。默认配置将创建在`/config/rtl_433/`中。要添加或编辑额外的配置，请在该目录中创建多个`.conf.template`文件。

 6. 启动插件并检查日志。

## 配置

对于“零配置”设置，安装 [Mosquitto代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。虽然其他代理可能有效，但未经测试，且需要手动设置。一旦安装了插件，请启动或重启rtl_433和rtl_433_mqtt_autodiscovery插件，以开始捕获已知的433 MHz协议。

对于更高级的配置，可以查看rtl_433源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中有bash变量， **美元符号和其他特殊Shell字符需要转义**。例如，若要在配置文件中使用字面字符串`$GPRMC`，请使用`\$GPRMC`。

`retain`选项控制MQTT的`retain`标志默认是启用还是禁用。可以通过在`output`设置中将`retain`设置为`true`或`false`来在每个无线电基础上覆盖。

在手动配置时，假设你打算将rtl_433数据导入Home Assistant，配置文件中需要指定的最低要求是[MQTT连接和认证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433默认监听在433.92MHz，但即使这是你所需要的，明确指定频率也是个好主意，以避免混淆：

```
frequency   433.92M
```

你可能还想缩小rtl_433应尝试解码的协议列表。完整列表可以在[README](https://github.com/merbanan/rtl_433/blob/master/README.md)的“支持设备协议”部分找到。假设你想监听Acurite 592TXR温湿度传感器：

```
protocol    40
```

最后但同样重要的是，如果你决定使用MQTT自动发现脚本或插件，其文档建议将来自rtl_433的所有数据中的单位转换为SI：

```
convert     si
```

假设你只有一个USB接收器连接，并且rtl_433能够自动找到它，那么我们得到一个最小的rtl_433配置文件如下：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

有关更多信息，请查看 [官方rtl_433文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf)。

## 贡献

这个插件基于James Fry的 [rtl4332mqtt Hass.IO插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，后者又基于Chris Kacerguis的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而后者又基于Marco Verleun的rtl2mqtt镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。