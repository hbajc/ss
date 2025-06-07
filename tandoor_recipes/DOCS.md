## 配置

请查看 Tandoor Recipes 文档 : https://docs.tandoor.dev/install/docker/

```yaml
必需：
    "ALLOWED_HOSTS": "你的系统URL", # 你需要输入你的 homeassistant URL（用逗号分隔，不要有空格）以允许访问
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 你的密钥
    "PORT": 9928 # 默认情况下，Web 界面可在 http://HAurl:9928 上访问。如果你需要更改端口，则不应在应用程序中进行更改，只能通过此选项。
    "Environment": 0|1 # 1 是调试模式，0 是正常模式。除非积极开发，否则应在正常模式下运行。
    "GUNICORN_MEDIA": 0|1 # 1 启用 gunicorn 媒体托管。这个不推荐。你应该使用 nginx 服务器来托管你的媒体 - 请查看文档。
可选：
    "POSTGRES_HOST": "str?", # postgresql_external 所需
    "POSTGRES_PORT": "str?", # postgresql_external 所需
    "POSTGRES_USER": "str?", # postgresql_external 所需
    "POSTGRES_PASSWORD": "str?", # postgresql_external 所需
    "POSTGRES_DB": "str?" # postgresql_external 所需
    "externalfiles_folder": "str?" # 你想要映射到 Tandoor 的文件夹。不是必要的，因为 /share/ 和 /media/ 已被映射。如果该文件夹不存在，将会创建。
```

### Mariadb
Mariadb 是家居助手社区中的一个流行附加组件，然而它不被 Tandoor Recipes 应用程序支持。

### 调试模式
这是 "Environment" 设置。
0 是正常模式  
1 是调试模式。

### 身份验证
使用外部身份验证。Tandoor Recipes 支持这一点，但尚未实施。

### Gunicorn 媒体
禁用 gunicorn 媒体是个好主意，但需要运行一个 Web 服务器来托管媒体文件。Web 服务器应映射 `/media/`。  
有关更多信息，请查看 https://docs.tandoor.dev/install/docker/#nginx-vs-gunicorn。  
0 是禁用 gunicorn - 媒体在没有 nginx Web 服务器的情况下无法工作。  
1 是启用 gunicorn - 媒体将通过 gunicorn 托管，但这并不推荐。

### 外部食谱文件

目录 `/config/addons_config/tandoor_recipes/externalfiles` 可用于将外部文件导入到 Tandoor。你可以在 Docker 中将其映射到 /opt/recipes/externalfiles。根据此处的说明：https://docs.tandoor.dev/features/external_recipes/
目录 `/config`、`/media/` 和 `/share/` 已映射到附加组件。你可以在这些位置中的任何一个手动创建文件夹并将其映射到 Tandoor：
- 在你想要的地点创建一个目录，例如 `/share/tandoor/recipebook/`
- 在 Tandoor 中创建一个外部存储位置 - `/share/tandoor/`
- 监视特定文件夹 - `/share/tandoor/recipebook/`
- 立即同步
- 导入。