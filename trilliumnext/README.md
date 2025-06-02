# 家庭助手插件：Trillium Next Notes
Trilium Next Notes 是一款层次化的笔记应用程序，专注于构建大型个人知识库。

_感谢所有给我的仓库星标的人！要给它加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 特点

* 笔记可以被安排成任意深度的树形结构。单个笔记可以放置在树的多个位置（请参见 [克隆](https://triliumnext.github.io/Docs/Wiki/cloning-notes)）
* 丰富的所见即所得（WYSIWYG）笔记编辑功能，包括例如表格、图片和 [数学](https://triliumnext.github.io/Docs/Wiki/text-notes)，支持markdown [自动格式化](https://triliumnext.github.io/Docs/Wiki/text-notes#autoformat)
* 支持编辑带有源代码的 [笔记](https://triliumnext.github.io/Docs/Wiki/code-notes)，包括语法高亮
* 快速简便的 [笔记导航](https://triliumnext.github.io/Docs/Wiki/note-navigation)、全文搜索和 [笔记提升](https://triliumnext.github.io/Docs/Wiki/note-hoisting)
* 无缝的 [笔记版本控制](https://triliumnext.github.io/Docs/Wiki/note-revisions)
* 笔记 [属性](https://triliumnext.github.io/Docs/Wiki/attributes) 可用于笔记组织、查询和高级 [脚本](https://triliumnext.github.io/Docs/Wiki/scripts)
* 与自托管同步服务器的 [同步](https://triliumnext.github.io/Docs/Wiki/synchronization)
  * 有一个 [第三方服务用于托管同步服务器](https://trilium.cc/paid-hosting)
* 将笔记 [分享](https://triliumnext.github.io/Docs/Wiki/sharing)（发布）到公共互联网
* 强大的 [笔记加密](https://triliumnext.github.io/Docs/Wiki/protected-notes)，支持逐笔记的粒度
* 使用内置的 Excalidraw 绘制图表（笔记类型为 "canvas"）
* [关系图](https://triliumnext.github.io/Docs/Wiki/relation-map) 和 [链接图](https://triliumnext.github.io/Docs/Wiki/link-map) 用于可视化笔记及其关系
* [脚本](https://triliumnext.github.io/Docs/Wiki/scripts) - 参见 [高级展示](https://triliumnext.github.io/Docs/Wiki/advanced-showcases)
* 用于自动化的 [REST API](https://triliumnext.github.io/Docs/Wiki/etapi)
* 在可用性和性能上能良好扩展至超过 100,000 条笔记
* 针对智能手机和平板电脑优化的 [移动前端](https://triliumnext.github.io/Docs/Wiki/mobile-frontend)
* [夜间主题](https://triliumnext.github.io/Docs/Wiki/themes)
* 支持 [Evernote](https://triliumnext.github.io/Docs/Wiki/evernote-import) 和 [Markdown 的导入与导出](https://triliumnext.github.io/Docs/Wiki/markdown)
* [网页剪辑工具](https://triliumnext.github.io/Docs/Wiki/web-clipper)，便于保存网页内容

## 安装

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
2. 安装此插件。
3. 点击 `保存` 按钮以保存您的配置。
4. 启动插件。它会失败，没关系
5. 使用 ssh 登录到您的家庭助手并运行 `chmod 2777 /2effc9b9/trilliumnext`
6. 启动插件。
7. 检查插件的日志以查看是否一切正常。
8. 转到您的本地家庭助手 IP:端口管理端口或入口。
9. 按照说明进行操作

```
port : 8000 # 您想要运行管理界面的端口。
```

Webui 可以在 `<your-ip>:port` 或入口访问。

[repository]: https://github.com/jdeath/homeassistant-addons