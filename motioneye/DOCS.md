# Home Assistant Community Add-on: motionEye

motionEye 是一个流行的摄像头软件 motion 的前端。这个插件提供了两者的功能，让您可以将摄像头添加到您的 Hass.io 设置中。

motionEye 是开源的 CCTV 和 NVR，既优雅又易于使用。
它可以用作婴儿监视器、建筑工地监控查看器、
商店摄像头 DVR、花园安保等更多用途。

motionEye 的一些酷功能：

- 支持大量摄像头，包括 IP 摄像头。
- 通过将多个 motionEye 实例连接在一起，可以添加多个摄像头。
  例如，通过在您的网络中使用带有 Pi 摄像头的 Pi Zero 上运行 MotionEyeOS。
- 支持将录制内容上传到 Google Drive 和 Dropbox。
- 支持运动检测，包括电子邮件通知和调度。
- 可以连续录制、运动或延时拍摄，具有保留设置。
- 支持在配置中使用 “[action buttons][motioneye-wiki-action-buttons]”。

## 安装

安装这个插件非常简单，与安装其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 我的按钮以在您的 Home
   Assistant 实例中打开插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 启动“motionEye”插件。
1. 检查“motionEye”插件的日志以查看是否一切顺利。
1. 点击“打开网页界面”按钮以打开网页界面。
1. 使用用户名“admin”登录，密码为空。
1. 使用安全密码编辑您的管理员帐户！

Home Assistant 默认情况下安装了社区插件商店。
但是，如果缺失（出于任何原因），您可以通过点击下面的我的按钮来添加它。

[![将存储库添加到您的 Home Assistant 实例。][repository-badge]][repository]

## 配置

**注意**：_更改配置时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
ssl: true
certfile: mycertfile.pem
keyfile: mykeyfile.pem
```

**注意**：_这只是一个示例，不能直接复制粘贴！请创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以改变为更详细或更简略，在处理未知问题时可能会很有用。可以的值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常事件。
- `error`：不需要立即处理的运行时错误。
- `fatal`：出现严重错误，插件变得不可用。

请注意，每个级别自动包含来自更高严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是一种推荐设置，除非您在排错。

### 选项：`motion_webcontrol`

启用在端口 `7999` 上运行的运动网页控制端点。

:warning: MotionEye HTTP 网页控制 **不支持** 认证
并且 **不支持** SSL！仅当您知道自己在做什么时才能启用此功能！**绝不要** 将此端口暴露给外部世界！

### 选项：`ssl`

启用/禁用 motionEye 网页界面的 SSL (HTTPS)。设置为 `true`
以启用，`false` 则禁用。

### 选项：`certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 目录中，这是默认设置_

### 选项：`keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 目录中，这是默认设置_

### 选项：`action_buttons`

如果配置，则将创建一个脚本以实现 [action button][motioneye-wiki-action-buttons]。

示例动作按钮配置：

```yaml
action_buttons:
  - type: light_on
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=ON > /dev/null"
  - type: light_off
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=OFF > /dev/null"
```

#### 子选项：`action_buttons.type`

动作按钮的类型。可接受的类型有：

- `lock` 和 `unlock`。
- `light_on` 和 `light_off`。
- `alarm_on` 和 `alarm_off`。
- `up`、`right`、`down` 和 `left`。
- `zoom_in` 和 `zoom_out`。
- `preset1` 到 `preset9`。

#### 子选项：`action_buttons.camera`

摄像头识别号码。对应于在 motionEye 用户界面中设置的摄像头编号。

#### 子选项：`action_buttons.command`

按下按钮时要执行的 bash shell 命令。

## 更新日志与版本

该存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

版本基于 [语义版本控制][semver]，使用格式 `MAJOR.MINOR.PATCH`。简单来说，版本将根据以下内容进行增量更新：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强功能。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几种选择可以得到答案：

- [Home Assistant Community Add-ons Discord 服务器][discord]，用于插件
  支持和功能请求。
- [Home Assistant Discord 服务器][discord-ha]，用于一般 Home
  Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以在这里 [打开问题][issue] GitHub。

## 作者与贡献者

该存储库的初始设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，随意处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售软件的副本，并允许向其提供软件的人这样做，具体条件如下：

上述版权声明和本许可声明应包含在所有副本或实质性部分的软件中。

该软件是“按原样”提供的，不作任何种类的担保，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有者对于因使用软件或与软件的使用或其他交易有关的任何索赔、损害或其他责任均不承担责任。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_motioneye
[contributors]: https://github.com/hassio-addons/addon-motioneye/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[dockerhub]: https://hub.docker.com/r/hassioaddons/motioneye
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-motioneye/71826?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-motioneye/issues
[motioneye-wiki-action-buttons]: https://github.com/motioneye-project/motioneye/wiki/Action-Buttons
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-motioneye/releases
[repository-badge]: https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg
[repository]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[semver]: https://semver.org/spec/v2.0.0.html