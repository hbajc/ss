# Ollama 插件 for Home Assistant

请注意，此插件在 CPU 加速或实验性的 Nvidia GPU 支持下运行（请反馈是否对您有效！）。ROCm 的支持仍在待定中。

## 模型目录

所有下载的模型默认存储在 `/share/ollama`。出于历史原因，您也可以将其配置为 `/config/ollama`。请确保您有足够的可用空间。

## Ollama 集成

要下载任何模型，可以使用 Ollama 的 API，或与 Home Assistant 集成 [Ollama](https://www.home-assistant.io/integrations/ollama/)：

[![添加 Ollama 集成](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ollama)

使用以下数据：

- URL: `http://76e18fb5-ollama:11434`

如果您想更改模型，请删除集成（而不是插件！）并重新启动集成的配置过程。

## 关于 UI 链接的说明

UI 链接仅用于检查 Ollama 的 API 是否可用。官方版本的 Ollama 中不包含聊天功能。