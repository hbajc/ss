# Home Assistant 插件：Authelia

## 描述

Authelia 是一个开源的身份验证和授权服务器，旨在为您的服务提供安全的访问控制。此插件允许您在 Home Assistant 内部运行 Authelia。

## 支持的架构

此插件支持以下架构：

- `amd64`
- `aarch64`

## 安装

1. 在 Home Assistant 中导航到 **设置** > **插件**。
2. 点击 **插件商店** 并搜索 **Authelia**。
3. 如有必要，添加 `https://github.com/einschmidt/hassio-addons` 仓库。
4. 安装插件并使用以下设置进行配置。
5. 启动插件并打开日志以检查任何问题。

## 配置

在首次启动插件之前，您 **必须编辑 `domain`** 选项中的配置。这是一个关键步骤，因为它确保 Authelia 与您的特定域设置正确，以确保正常功能。

### 配置步骤

1. **编辑域**  
   `domain` 选项必须在第一次启动之前设置。此选项对正确路由请求和配置会话 cookie 至关重要。

   - 示例：
     ```yaml
     domain: yourdomain.com
     ```

2. **首次启动**  
   在首次启动时，插件将自动在 `addon_config` 文件夹中创建 `config.yml` 文件。此文件将填充默认设置，包括配置的域和其他所需设置。

3. **编辑生成的 `config.yml`**  
   首次启动后，您将在 `/addon_config` 文件夹中找到 `config.yml` 文件。 **您必须编辑此文件以匹配您的个人环境**。确保所有必要的设置，如域、用户身份验证路径和其他相关选项都已正确配置。

4. **重新启动插件**  
   对 `config.yml` 文件进行任何编辑后， **您必须重新启动插件** 以使更改生效。此步骤对于确保更新配置的正确应用至关重要。

### 重要说明

- **`domain`** 设置仅在初始配置创建时为必需。
- 初始启动后对 `config.yml` 的任何更改都需要 **重新启动插件** 才能应用新设置。

请确保仔细审查并自定义 `config.yml`，以确保最佳操作。

## 更多信息

有关更多详细信息，请访问官方 Authelia 资源：

- **网站:** [Authelia](https://www.authelia.com//)
- **文档:** [入门指南](https://www.authelia.com/integration/prologue/get-started/)