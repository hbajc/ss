# 家庭助手插件: Trillium Next Notes
Trilium Next Notes 是一款层次化笔记应用，专注于构建大型个人知识库。

_感谢每一个给我的仓库加星的朋友！要给它加星，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 特性

* 笔记可以被安排成任意深度的树形结构。单个笔记可以在树中放置于多个位置（参见[克隆](https://triliumnext.github.io/Docs/Wiki/cloning-notes)）
* 丰富的所见即所得笔记编辑，包括例如表格、图片和[数学](https://triliumnext.github.io/Docs/Wiki/text-notes)支持，及markdown [自动格式化](https://triliumnext.github.io/Docs/Wiki/text-notes#autoformat)
* 支持编辑带有源代码的[笔记](https://triliumnext.github.io/Docs/Wiki/code-notes)，包括语法高亮
* 快速而简便的[笔记导航](https://triliumnext.github.io/Docs/Wiki/note-navigation)，全文本搜索和[笔记提升](https://triliumnext.github.io/Docs/Wiki/note-hoisting)
* 无缝的[笔记版本控制](https://triliumnext.github.io/Docs/Wiki/note-revisions)
* 笔记[属性](https://triliumnext.github.io/Docs/Wiki/attributes)可用于笔记组织、查询和高级[脚本](https://triliumnext.github.io/Docs/Wiki/scripts)
* 与自托管的同步服务器[同步](https://triliumnext.github.io/Docs/Wiki/synchronization)
  * 还有一个[第三方服务用于托管同步服务器](https://trilium.cc/paid-hosting)
* 将笔记[共享](https://triliumnext.github.io/Docs/Wiki/sharing)（发布）到公共互联网
* 强大的[笔记加密](https://triliumnext.github.io/Docs/Wiki/protected-notes)，按笔记粒度进行加密
* 用内置的 Excalidraw 绘制图表（笔记类型为 "canvas"）
* [关系图](https://triliumnext.github.io/Docs/Wiki/relation-map)和[链接图](https://triliumnext.github.io/Docs/Wiki/link-map)用于可视化笔记及其关系
* [脚本](https://triliumnext.github.io/Docs/Wiki/scripts) - 参见[高级展示](https://triliumnext.github.io/Docs/Wiki/advanced-showcases)
* 用于自动化的[REST API](https://triliumnext.github.io/Docs/Wiki/etapi)
* 可承载超过 100,000 个笔记，具备良好的可用性和性能
* 针对智能手机和平板电脑优化的[移动前端](https://triliumnext.github.io/Docs/Wiki/mobile-frontend)
* [夜间主题](https://triliumnext.github.io/Docs/Wiki/themes)
* 支持[Evernote](https://triliumnext.github.io/Docs/Wiki/evernote-import)和[Markdown 导入与导出](https://triliumnext.github.io/Docs/Wiki/markdown)
* [网页剪辑器](https://triliumnext.github.io/Docs/Wiki/web-clipper)，方便保存网页内容

## 安装

1. [将我的 Hass.io 插件库][repository]添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `Save` 按钮保存你的配置。
1. 启动插件。它会失败，这没关系。
1. SSH 进入你的家庭助手并运行 `chmod 2777 /2effc9b9/trilliumnext`
1. 启动插件。
1. 检查插件的日志，看看一切是否正常。
1. 进入本地家庭助手 IP:port 管理端口或入口。
1. 按照指示操作。

```
port : 8000 #你想要运行管理界面的端口。
```

Webui 可以在 `<your-ip>:port` 或入口找到。

[repository]: https://github.com/jdeath/homeassistant-addons