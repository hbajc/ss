# Home Assistant Community Add-on: motionEye

motionEye 是一个流行的相机软件 motion 的前端。此附加组件提供了两者，允许您将相机添加到您的 Hass.io 设置中。

motionEye 是开源的 CCTV 和 NVR，优雅且易于使用。它可以用作婴儿监视器、施工现场 Montage 观察员、商店相机 DVR、花园安全以及更多功能。

motionEye 的一些酷功能：

- 支持数量庞大的相机，包括 IP 摄像头。
- 通过连接多个 motionEye 实例来添加多个相机。例如，在您的网络中使用 Pi Zero + Pi 摄像头上的 MotionEyeOS。
- 支持将录制上传到 Google Drive 和 Dropbox。
- 运动检测，包括电子邮件通知和调度。
- 可以连续录制、运动录制或延时录制，并具有保留设置。
- 支持配置中的 "[action buttons][motioneye-wiki-action-buttons]"。

## 安装

此附加组件的安装非常简单，与安装任何其他 Home Assistant 附加组件没有不同。

1. 点击下方的 Home Assistant My 按钮以在您的 Home Assistant 实例中打开此附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装附加组件。
1. 启动“motionEye”附加组件
1. 检查“motionEye”附加组件的日志以查看是否一切正常。
1. 点击“打开 Web UI”按钮以打开网页界面。
1. 使用用户名“admin”登录，无需输入密码。
1. 用安全密码编辑您的管理员账户！

默认情况下，Home Assistant 附带社区附加组件商店安装。然而，如果缺失（出于任何原因），您可以通过点击下面的 My 按钮添加它。

[![将存储库添加到您的 Home Assistant 实例。][repository-badge]][repository]

## 配置

**注意**：_在更改配置时请记得重新启动附加组件。_

示例附加组件配置：

```yaml
log_level: info
ssl: true
certfile: mycertfile.pem
keyfile: mykeyfile.pem
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`: 显示所有细节，例如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 出现严重错误，附加组件变得不可用。

请注意，每个级别自动包含来自更高级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，除非您在排除故障，否则建议使用该设置。

### 选项: `motion_webcontrol`

启用在端口 `7999` 上运行的运动 webcontrol 端点。

:warning: MotionEye HTTP webcontrol **不支持** 身份验证，并且 **不支持** SSL！仅在您知道自己在做什么时启用此选项！**绝对不要**将此端口暴露给外部世界！

### 选项: `ssl`

启用/禁用 motionEye 的网页界面上的 SSL（HTTPS）。设置为 `true` 以启用，设置为 `false` 以禁用。

### 选项: `certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认值_

### 选项: `keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认值_

### 选项: `action_buttons`

如果配置，则会创建一个脚本来实现 [action button][motioneye-wiki-action-buttons]。

示例 action buttons 配置：

```yaml
action_buttons:
  - type: light_on
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=ON > /dev/null"
  - type: light_off
    camera: 1
    command: "curl -s 192.168.1.1/index.html?light=OFF > /dev/null"
```

#### 子选项: `action_buttons.type`

操作按钮的类型。可接受的类型包括：

- `lock` 和 `unlock`。
- `light_on` 和 `light_off`。
- `alarm_on` 和 `alarm_off`。
- `up`、`right`、`down` 和 `left`。
- `zoom_in` 和 `zoom_out`。
- `preset1` 到 `preset9`。

#### 子选项: `action_buttons.camera`

摄像头识别号码。对应于在 motionEye UI 中设置的摄像头号码。

#### 子选项: `action_buttons.command`

按下按钮时要执行的 bash shell 命令。

## 更新日志与发布

此存储库使用 [GitHub 的 releases][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，使用格式 `MAJOR.MINOR.PATCH`。简而言之，版本将根据以下内容递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和软件包更新。

## 支持

有问题？

您有几种选项可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获取附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以获取一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit subreddit][reddit]，在 [/r/homeassistant][reddit] 中。

您也可以在这里 [打开问题][issue] GitHub。

## 作者与贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授予任何获取本软件及相关文档文件（“软件”）副本的人，无限制地使用、复制、修改、合并、发布、分发、再授权和/或出售软件副本的权利，并允许提供给他人使用软件的人这样做，前提是满足以下条件：

上述版权声明和本许可声明应包含在所有软件副本或实质部分中。

该软件是按“原样”提供的，不提供任何种类的担保，无论是明示或暗示，包括但不限于适销性、特定用途的适用性和不侵权。在任何情况下，作者或版权持有人均不对因使用该软件或其他交易而产生的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面。

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