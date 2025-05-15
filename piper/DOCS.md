# Home Assistant 插件：Piper

## 安装

按照以下步骤在您的系统上安装该插件：

1. 在您的 Home Assistant 前端中导航至 **设置** -> **插件** -> **插件商店**。
2. 找到 "Piper" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

该插件安装并运行后，Home Assistant 中的 Wyoming 集成将自动发现它。要完成设置，请点击以下我的按钮：

[![打开您的 Home Assistant 实例并开始设置新的集成。](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=wyoming)

或者，您可以手动安装 Wyoming 集成，更多信息请参见 [Wyoming 集成文档](https://www.home-assistant.io/integrations/wyoming/)。

## 配置

### 选项：`voice`

[收听语音样本](https://rhasspy.github.io/piper-samples/)

要使用的 Piper 语音名称，例如 `en_US-lessac-medium`（默认值）。
语音模型将自动从 https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0 下载。

语音的命名遵循以下方案：`<language>_<REGION>-<name>-<quality>`
`<name>` 部分来自用于训练语音的数据集或提供的发言者名称。

语音的质量分为 4 个不同级别：

- `x_low` - 16Khz，最小/最快
- `low` - 16Khz，快速
- `medium` - 22.05Khz，更慢但音质更好
- `high` - 22.05Khz，最慢但音质最好

在 Raspberry Pi 4 上，最多可以使用 `medium` 模型以可用速度运行。如果音频质量不是优先考虑的，优先选择 `low` 或 `x-low` 语音，因为它们的速度明显快于 `medium`。

### 选项：`speaker`

如果语音支持多个扬声器，则使用的扬声器编号，例如 [`en-us-libritts-high`](https://rhasspy.github.io/piper-samples/#en-us-libritts-high)。

默认情况下，将使用第一个扬声器（扬声器 0）。

### 选项：`length_scale`

加速或减缓声音。值为 1.0 表示使用语音的默认说话速率，< 1.0 为更快，> 1.0 为更慢。

### 选项：`noise_scale`

通过在音频生成过程中添加噪声来控制音频的变化性。该效果高度依赖于语音本身，但一般来说，值为 0 将消除变异，值大于 1 将开始降低音频质量。

### 选项：`noise_w`

控制说话节奏的变化性（音素宽度）。该效果高度依赖于语音本身，但一般来说，值为 0 将消除变异，值大于 1 会产生极端的口吃和停顿。

### 选项：`max_piper_procs`

同时运行的 Piper 进程数量（默认值为 1）。每个 Piper 进程将一个语音模型加载到内存中，因此同时使用多个语音需要：

- 在使用语音时启动/停止 Piper 进程，或
- 运行更多的 Piper 进程

该插件将为每个请求的语音启动一个 Piper 进程，最多到 `max_piper_procs`。之后，将停止使用时间最久的语音。
如果需要快速切换多个语音，请增加 `max_piper_procs`，但请注意，这会增加插件的内存使用量。

### 选项：`update_voices`

每次插件启动时自动下载新语音的列表。您还必须重新加载 Home Assistant 中的 Wyoming 集成以查看新语音。

### 选项：`debug_logging`

将 DEBUG 级别的消息打印到插件的日志中。

## 自定义语音

将自定义语音文件添加到 `/share/piper` 目录。每个自定义语音必须包含一个模型文件（`<voice>.onnx`）和一个配置文件（`<voice>.onnx.json`）。
有关如何训练和导出自定义语音的详细信息，请参阅 [训练指南](https://github.com/rhasspy/piper/blob/master/TRAINING.md)。

## 支持

有问题吗？

您有几种方式可以获得答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了一个 bug，请 [在我们的 GitHub 上提交问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant
[repository]: https://github.com/hassio-addons/repository