# Home Assistant 社区附加组件：Studio Code Server

该附加组件运行 [code-server](https://github.com/coder/code-server)，
它可以让您从浏览器直接获得 Visual Studio Code 的体验。它允许您
直接从网页浏览器编辑您的 Home Assistant 配置，直接在 Home Assistant 前端中。

该附加组件预先安装和配置了 Home Assistant、MDI 图标和 YAML 扩展。
这意味着自动补全可以立即工作，而无需配置任何内容。

## 安装

安装此附加组件非常简单，与安装任何其他 Home Assistant 附加组件没有什么不同。

1. 点击下面的 Home Assistant 我的按钮以在您的 Home Assistant 实例中打开该附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

2. 点击“安装”按钮安装该附加组件。
3. 启动“Studio Code Server”附加组件。
4. 检查“Studio Code Server”附加组件的日志，以查看一切是否顺利。
5. 点击“打开 Web 界面”按钮以打开 Studio Code Server。

## 配置

**注意**：_在更改配置时，请记得重启附加组件。_

附加组件配置示例：

```yaml
log_level: info
config_path: /share/my_path
packages:
  - mariadb-client
init_commands:
  - ls -la
```

**注意**：_这只是一个示例，请不要直接复制粘贴！ 创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制附加组件输出的日志级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能值有：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不错误的异常情况。
- `error`：不需要立即行动的运行时错误。
- `fatal`：出现严重错误，附加组件无法使用。

请注意，每个级别自动包含更高级别的日志消息，例如 `debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这也是推荐的设置，除非您正在进行故障排除。

### 选项：`config_path`

此选项允许您覆盖附加组件在访问网页界面时将打开的默认路径。例如，使用不同的配置目录，如 `/share/myconfig`，而不是 `/config`。如果设置为 `/root`，则 Home Assistant 的所有常见文件夹（如下 `/config`、`/ssl`、`/share` 等）将作为子文件夹出现。

在未配置的情况下，附加组件将自动使用默认路径：`/config`

### 选项：`packages`

允许您指定额外的 [Ubuntu 包][ubuntu-packages]，以便在您的 shell 环境中安装（例如，Python、PHP、Go）。

**注意**：_添加多个包会导致附加组件启动时间更长。_

### 选项：`init_commands`

使用 `init_commands` 选项进一步自定义您的 VSCode 环境。将一个或多个 shell 命令添加到列表中，每次启动此附加组件时都会执行这些命令。

## 将您的 VSCode 设置重置为附加组件默认值

该附加组件会更新您的设置，以优化与 Home Assistant 的使用。一旦您更改设置，附加组件将停止执行该操作，因为这可能会破坏。然而，如果您更改了一些内容，但希望恢复到该附加组件提供的默认值，请执行以下操作：

1. 打开 Visual Studio Code 编辑器。
2. 点击顶部菜单栏中的 `终端`，然后点击 `新终端`。
3. 在终端窗口中执行以下命令：`reset-settings`。
4. 完成！

## 已知问题和限制

- 此附加组件可以在 Raspberry Pi 上运行吗？是的，但仅在您运行 64 位操作系统的情况下。另见下面的要点。
- 此附加组件当前仅支持 AMD64 和 aarch64/ARM64 机器。
  尽管我们支持 ARM 设备，但请注意，此附加组件运行起来相当耗费资源，并且需要相当多的 RAM。我们不建议在内存少于 4Gb 的设备上运行它。
- “Visual Studio Code 无法监视此大型工作区中的文件更改”（错误 ENOSPC）

  此问题是由于您的系统没有足够的文件句柄，导致 VSCode 无法监视所有文件。对于 HassOS，目前唯一的选项是在通知出现时点击小齿轮并告诉它不再显示。如果您有通用的 Linux 设置（例如，Ubuntu），请按照 Microsoft 的指南操作：

  <https://code.visualstudio.com/docs/setup/linux#_visual-studio-code-is-unable-to-watch-for-file-changes-in-this-large-workspace-error-enospc>

## 更新日志与发布

该存储库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，采用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有多种选项可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit subreddit][reddit] 在 [/r/homeassistant][reddit]

您也可以在这里 [提交问题][issue] 到 GitHub。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，
请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2019-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，处理该软件的权利，未经限制地，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售该软件的副本，以及允许向其提供该软件的人这样做，受以下条件的限制：

上述版权声明和本许可声明应包含在所有副本或重要部分的该软件中。

该软件是“按原样”提供的，未提供任何种类的保证，无论是明示还是暗示，包括但不限于对适销性、特定目的适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因本软件或其使用或其他交易而产生的任何索赔、损害或其他责任（无论是在合同、侵权或其他方面）承担责任。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-vscode/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-visual-studio-code/107863?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-vscode/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-vscode/releases
[semver]: https://semver.org/spec/v2.0.0
[ubuntu-packages]: https://packages.ubuntu.com