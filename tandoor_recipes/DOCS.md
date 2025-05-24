## 配置

请查看 Tandoor Recipes 文档: https://docs.tandoor.dev/install/docker/

```yaml
必需项：
    "ALLOWED_HOSTS": "您的系统网址", # 您需要输入您的 homeassistant URL（逗号分隔，无空格），以允许流量进入
    "DB_TYPE": "list(sqlite|postgresql_external)" # 使用的数据库类型。
    "SECRET_KEY": "str", # 您的密钥
    "PORT": 9928 # 默认情况下，webui 可通过 http://HAurl:9928 访问。如果您需要更改端口，应该仅通过此选项更改，而不是在应用程序中更改
    "Environment": 0|1 # 1 为调试模式，0 为正常模式。除非主动开发，您应该在正常模式下运行。
    "GUNICORN_MEDIA": 0|1 # 1 启用 gunicorn 媒体托管。这不推荐。您应该使用 nginx 服务器来托管媒体 - 请参阅文档。
可选项：
    "POSTGRES_HOST": "str?", # 对于 postgresql_external 是必需的
    "POSTGRES_PORT": "str?", # 对于 postgresql_external 是必需的
    "POSTGRES_USER": "str?", # 对于 postgresql_external 是必需的
    "POSTGRES_PASSWORD": "str?", # 对于 postgresql_external 是必需的
    "POSTGRES_DB": "str?" # 对于 postgresql_external 是必需的
    "externalfiles_folder": "str?" # 您希望在 tandoor 中映射的文件夹。由于 /share/ 和 /media/ 已经映射，因此不需要此文件夹。如果它不存在，将自动创建这个文件夹。
```
### Mariadb
Mariadb 是 Home Assistant 社区中的一个热门插件，然而它不被 Tandoor Recipes 应用程序支持。

### 调试模式
这是 "Environment" 设置。
0 为正常模式  
1 为调试模式。

### 认证
使用外部认证。Tandoor Recipes 支持此功能，但尚未实现。

### Gunicorn 媒体
禁用 gunicorn 媒体是个好主意，但需要一个运行中的 web 服务器来托管媒体文件。web 服务器应该映射 `/media/`。  
有关更多信息，请参见 https://docs.tandoor.dev/install/docker/#nginx-vs-gunicorn。  
0 为 gunicorn 禁用 - 没有 nginx web 服务器，媒体将无法工作。  
1 为 gunicorn 启用 - 媒体将在 gunicorn 中托管，这不是推荐的做法。

### 外部食谱文件

目录 `/config/addons_config/tandoor_recipes/externalfiles` 可用于将外部文件导入到 Tandoor。您可以在 Docker 中将其映射到 /opt/recipes/externalfiles。根据此处的说明：https://docs.tandoor.dev/features/external_recipes/
目录 `/config`、`/media/` 和 `/share/` 已映射到插件中。您可以在这些位置中的任何一个手动创建一个文件夹，并将其映射到 tandoor：
- 在您想要的位置创建一个目录，例如 `/share/tandoor/recipebook/`
- 在 tandoor 中创建一个外部存储位置 - `/share/tandoor/`
- 监视特定文件夹 - `/share/tandoor/recipebook/`
- 现在同步
- 导入。