# Ollama 附加组件用于 Home Assistant

请注意，这个附加组件使用 CPU 加速或实验性的 Nvidia GPU 支持（如果适用于您，请报告！）。对于 ROCm 的支持仍在等待中。

## 模型目录

所有下载的模型默认存储在 `/share/ollama`。出于历史原因，您也可以将其配置为 `/config/ollama`。请确保您有足够的可用空间。

## Ollama 集成

要下载任何模型，可以使用 Ollama 的 API 或与 Home Assistant 集成 [Ollama](https://www.home-assistant.io/integrations/ollama/)：

[![添加 Ollama 集成](https://my.home-assistant.io/badges/brand.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=ollama)

使用以下数据：

- URL: `http://76e18fb5-ollama:11434`

如果您想更改模型，请删除集成（而不是附加组件！）并重新启动配置集成的过程。

## 关于 UI 链接的说明

UI 链接仅用于检查 ollama 的 API 是否可用。官方的 ollama 镜像中不包含聊天功能。