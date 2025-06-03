# Home Assistant 插件: battybirdnet-pi

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要加星，请点击下面的图像，然后它会在右上角出现。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/BirdNET-Pi/stats.png)

## 关于

---

[battybirdnet-pi](https://github.com/rdz-oss/BattyBirdNET-Pi) 是一个基于 Raspberry Pi 4/5 的实时声学蝙蝠和鸟类分类系统，构建于 BattyBirdNET-Analyzer 之上。

插件的特点：
- 由 [linuxserver](https://github.com/linuxserver/docker-baseimage-debian) 提供的强大基础镜像
- 多亏于 https://github.com/gdraheim/docker-systemctl-replacement 的工作 docker 系统
- 使用 HA 的 pulseaudio 服务器
- 使用 HA tmpfs 在 RAM 中存储临时文件，避免磁盘磨损
- 将所有配置文件暴露到 /config，以允许持久性和便捷访问
- 允许修改存储鸟类歌曲的位置（最好是外接硬盘）
- 支持入口，以允许安全的远程访问而不暴露端口

## 配置

---

首先安装，然后首次启动插件
Webui 可以通过两种方式找到：
- 从 HA 的入口访问（没有密码，但某些功能不工作）
- 使用 <http://homeassistant:port> 直接访问，端口为在 birdnet.conf 中定义的端口。当请求密码时，用户名为 `birdnet`，密码为您可以在 birdnet.con 中定义的密码（默认为空）。这与插件选项中的密码不同，后者是必须用于访问 Web 终端的密码。

Web 终端访问：用户名 `pi`，密码：如插件选项中所定义。

您需要一个麦克风：可以使用连接到 HA 的麦克风或 rstp 摄像头的音频流。

可以通过三种方式配置选项：

- 插件选项

```yaml
BIRDSONGS_FOLDER: 存储鸟类歌曲文件的文件夹 # 如果您想避免分析时堵塞，它应该是 SSD
MQTT_DISABLED: 如果为 true，则禁用自动 MQTT 发布。仅在已有本地代理时有效
LIVESTREAM_BOOT_ENABLED: 从启动或设置中启动直播
PROCESSED_FOLDER_ENABLED: 如果启用，您需要在 birdnet.conf（或 birdnet 的设置）中设置将保存在 tmpfs 中的临时文件夹 "/tmp/Processed" 中的最后 WAV 文件的数量（避免磁盘磨损）以便您想要检索它们。这个数量可以通过插件选项调整
TZ: Etc/UTC 指定要使用的时区，见 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
pi_password: 设置用户密码以访问 Web 终端
localdisks: sda1 # 输入硬盘的硬件名称，以逗号分隔，或其标签。例如：sda1，sdb1，MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smb 服务器列表，以逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "密码" # 可选，smb 密码
cifsdomain: "域" # 可选，允许设置 smb 共享的域
```

- Config.yaml
可以使用在 /config/db21ed7f_battybirdnet-pi/config.yaml 中找到的 config.yaml 文件配置其他变量，通过 Filebrowser 插件访问

- Config_env.yaml
可以在此配置额外的环境变量

## 安装

---

安装此插件相当简单，与安装其他任何插件并无不同。

1. 将我的插件存储库添加到您的 Home Assistant 实例（在 supervisor 插件商店右上方，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件存储库对话框，带有特定的存储库 URL 预填充](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 单击 `保存` 按钮以保存您的配置。
1. 根据您的喜好设置插件选项
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 打开 WebUI 并调整软件选项

## 与 HA 的集成

---
### Apprise

您可以使用 apprise 通过 mqtt 发送通知，然后使用 HomeAssistant 对其进行处理
更多信息： https://wander.ingstar.com/projects/birdnetpi.html

### 自动 mqtt

如果已安装 mqtt，插件将自动更新每个检测物种的 birdnet 主题

## 使用 ssl

---

选项 1：安装 let's encrypt 插件，生成证书。它们默认是 certfile.pem 和 keyfile.pem，存储在 /ssl 中。只需从插件选项中启用 ssl，它就会正常工作。

选项 2：启用 80 端口，将您的 battybirdnet-pi URL 定义为 https。证书将由 caddy 自动生成。

## 改善检测

---

### 卡的增益

在终端选项卡中使用 alsamixer，确保音量适中，但不太高（不要进入红色部分）
https://github.com/mcguirepr89/BirdNET-Pi/wiki/Adjusting-your-sound-card

### 铁氧体

在我的情况下，添加铁氧体珠导致更糟的噪声。

### Aux to usb 适配器

根据我的测试，仅使用 KT0210 的适配器（例如 Ugreen 的）有效。我无法检测到基于 ALC 的适配器。

### 麦克风对比

推荐的麦克风（[完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/39)）：
- Clippy EM272 (https://www.veldshop.nl/en/smart-clippy-em272z1-mono-omni-microphone.html) + ugreen aux to usb 连接器：最好的灵敏度，使用领夹技术
- Boya By-LM40：最佳性价比
- Hyperx Quadcast：最好的灵敏度，使用心形技术

结论，使用 Dahua 的麦克风已足够好，EM272 是最佳的，但 Boya By-LM40 是一个很好的折中，因为 birndet 模型分析 0-15000Hz 范围

![图片](https://github.com/alexbelgium/hassio-addons/assets/44178713/df992b79-7171-4f73-b0c0-55eb4256cd5b)

### 降噪 ([完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/597))

降噪受到严肃研究者的质疑。然而，它确实似乎显著提高检测质量！以下是在 HA 中执行此操作的方法：
- 使用 Portainer 插件，进入 hassio_audio 容器，并修改文件 /etc/pulse/system.pa，添加行 `load-module module-echo-cancel`
- 进入终端插件并输入 `ha audio restart`
- 在插件选项中选择回声取消设备作为输入设备

### 高通滤波

应避免使用，因为模型使用整个 0-15kHz 范围

## 常见问题

尚未提供

## 支持

在 GitHub 上创建一个问题

---