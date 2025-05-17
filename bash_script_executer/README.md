# Home Assistant Community Add-on: Bash 脚本执行器
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

Homeassistant OS 的 Bash 脚本执行器

## 关于

这是一个简单的 Docker 镜像，用于执行个人脚本。我需要这个的原因是，HA OS 安装的功能有限（例如没有 curl、sed 等），这个插件解决了这个问题。<br />
您可以使用此插件运行多达三个不同的脚本。<br />
这个 Docker 镜像包含：busybox-extras curl grep coreutils sed xmlstarlet

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
这个插件的安装相当简单，与安装任何其他自定义 Home Assistant 插件没有不同。<br />
只需点击上面的链接或将我的仓库添加到 hassio 附加组件库中： <https://github.com/FaserF/hassio-addons>

将您的脚本放在 /share/ 文件夹中的某个地方。其他文件夹对该插件不可见。<br />
您的脚本示例文件可能在： /share/scripts/script.sh

## 配置

**我建议禁用此插件的“开机启动”和 HA 的看门狗选项！**<br />

**注意**：_更改配置时，请记得重新启动该插件。_

示例插件配置：

```yaml
script_path: /share/scripts/script.sh
script_argument1: myFirstArgument
script_argument2: AnotherVariable
script_argument3: AnotherVariable
script_path2: false
script2_argument1:
script2_argument2:
script2_argument3:
script_path3: false
script3_argument2:
script3_argument2:
script3_argument3:
```

**注意**：_这只是一个示例，不要直接复制粘贴！请创建您自己的！_

### 选项： `script_path`

此选项是必需的。根据您的脚本所在位置更改它，或更改为“false”以留空。

### 选项： `scriptX_argumentX`

此选项是可选的。您可以通过此选项向您的脚本提交多达三个参数。

### 选项： `script_path2`

此选项是必需的。根据您的脚本所在位置更改它，或更改为“false”以留空。

### 选项： `script_path3`

此选项是必需的。根据您的脚本所在位置更改它，或更改为“false”以留空。

## Cron 支持 - 按时间运行脚本

我没有在此插件中实现 Cron，因为您可以通过 Homeassistant 自动化定期运行您的脚本。
示例自动化：<br />

```yaml
  - alias: "使用插件 Bash 脚本执行器运行 Bash 脚本"
    trigger:
      - platform: time
        at: '00:02:00'
      - platform: time_pattern
        minutes: '/90'
        seconds: 0
    action:
      - service: hassio.addon_start
        data:
          addon: 605cee21_bashscriptexecuter
```

## 支持

有问题或疑问吗？

您可以 [在这里打开一个问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 上的 armv7 上经过测试。我为我的个人脚本制作了这个插件。

## 作者与贡献者

该 hassio 插件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权所有 (c) 2025 FaserF

特此授予任何获得本软件及相关文档文件（“软件”）副本的人免费使用该软件的权利，处理该软件而不受限制，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售该软件副本的权利，并允许向其提供该软件的人这样做，遵循以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质部分中。

本软件是按“原样”提供的，不附有任何形式的担保，明示或暗示，包括但不限于对适销性、特定用途的适用性和非侵权的担保。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件或其他交易相关的使用产生的任何索赔、损害或其他责任负责，无论是合同、侵权或其他行为。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues