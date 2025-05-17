## &#9888; 已打开的问题 : [🐛 [Birdnet-go] 音频设置在重启时被覆盖 (打开于 2025-02-21)](https://github.com/alexbelgium/hassio-addons/issues/1781) 由 [@Lotwook](https://github.com/Lotwook)
## &#9888; 已打开的问题 : [🐛 [Birdnet-go] USB 麦克风在 UI 中可选择，但无法工作 (打开于 2025-03-12)](https://github.com/alexbelgium/hassio-addons/issues/1808) 由 [@melor](https://github.com/melor)
## &#9888; 已打开的问题 : [🐛 [BirdNET-Go] HA 入口网址无法重定向到带日期的网址 (打开于 2025-04-02)](https://github.com/alexbelgium/hassio-addons/issues/1830) 由 [@phobiac](https://github.com/phobiac)
# Home Assistant 插件：Birdnet-Go

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有关注我的仓库的人！要关注它，请点击下面的图像，然后它将位于右上角。谢谢！_

[![关注者名单](https://reporoster.com/stars/alexbelgium/hassio-addons)](https://github.com/alexbelgium/hassio-addons/stargazers)


![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/birdnet-go/stats.png)

## 关于

[BirdNET-Go](https://github.com/tphakala/birdnet-go/tree/main) 是由 @tphakala 开发的一种持续鸟类监测和识别的 AI 解决方案。

此插件基于他们的 Docker 镜像。

## 配置

首次安装后启动插件。WebUI 可在 <http://homeassistant:8080> 找到。
你需要一个麦克风：可以使用连接到 HA 的麦克风或 RTSP 摄像头的音频流。

音频片段文件夹可以通过从插件选项挂载外部或 SMB 驱动器来存储，然后指定路径而不是 "clips/"。例如，"/mnt/NAS/Birdnet/"

选项可以通过三种方式进行配置：

- 插件选项

```yaml
ALSA_CARD : 卡的编号（通常为 0 或 1），请参见 https://github.com/tphakala/birdnet-go/blob/main/doc/installation.md#deciding-alsa_card-value
TZ: Etc/UTC 指定要使用的时区，请参见 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
COMMAND : realtime --rtsp url # 允许为 birdnet-go 提供参数
```

- Config.yaml
可以使用在 /config/db21ed7f_birdnet-go/config.yaml 中找到的 config.yaml 文件配置其他变量，通过 Filebrowser 插件进行访问。

- Config_env.yaml
可以在此处配置其他环境变量。

## 安装

此插件的安装非常简单，与安装其他任何插件没有区别。

1. 将我的插件库添加到你的 Home Assistant 实例（在监视器插件商店的右上方，或如果你已经配置了我的 HA，单击下面的按钮）

   [![打开你的 Home Assistant 实例并显示添加插件库对话框，特定的库 URL 预填充。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以存储你的配置。
4. 根据你的喜好设置插件选项。
5. 启动插件。
6. 检查插件的日志以确定一切是否正常。
7. 打开 WebUI 并调整软件选项。

## 与 HA 的集成

Home Assistant 集成说明在此处找到，[Birdnet-Go 插件：Home Assistant 集成](./HAINTEGRATION.md)

## 使用 VLC 设置 RTSP 源

VLC 打开一个 TCP 端口，但流是 udp。为此需要配置 Birdnet-Go 使用 udp。调整 config.yaml 文件为 udp，或使用 birdnet-go 命令行选项：

`--rtsptransport udp --rtsp rtsp://192.168.1.21:8080/stream.sdp`

### Linux 指令

使用以下命令之一无界面地运行 vlc：

```bash
# 这应该适用于大多数设备
/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --no-sout-all --sout-keep --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'

# 如果第一个命令不工作，请尝试这个
/usr/bin/vlc -I dummy -vvv alsa://hw:4,0 --no-sout-all --sout-keep --sout '#rtp{sdp=rtsp://:8080/stream.sdp}'
```

运行 `arecord -l` 获取麦克风硬件信息

```text
**** 捕获硬件设备列表 ****
卡 0: PCH [HDA Intel PCH], 设备 0: ALC3220 模拟 [ALC3220 Analog]
  子设备: 1/1
  子设备 #0: 子设备 #0
卡 2: S7 [SteelSeries Arctis 7], 设备 0: USB 音频 [USB Audio]
  子设备: 1/1
  子设备 #0: 子设备 #0
卡 3: Nano [Yeti Nano], 设备 0: USB 音频 [USB Audio]
  子设备: 1/1
  子设备 #0: 子设备 #0
卡 4: 设备 [USB PnP 音频设备], 设备 0: USB 音频 [USB Audio]
  子设备: 0/1
  子设备 #0: 子设备 #0
```

hw:4,0 = **卡 4**: 设备 [USB PnP 音频设备], **设备 0**: USB 音频 [USB Audio]

Systemd 服务文件示例。根据需要调整用户：组。如果你想以 root 身份运行，可能需要运行 vlc-wrapper 而不是 vlc。

```text
[Unit]
Description=VLC Birdnet RTSP Server
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
StandardOutput=journal
ExecStart=/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'
User=someone
Group=somegroup

[Install]
WantedBy=multi-user.target
```

## 常见问题

尚未提供。

## 支持

在 GitHub 上创建一个问题。

---

![插图](https://raw.githubusercontent.com/tphakala/birdnet-go/main/doc/BirdNET-Go-dashboard.webp)