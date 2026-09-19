# Xiaodong Yang — Academic Homepage

英文默认、支持中文切换的静态个人主页。无需安装前端框架或 Hugo。

## 预览与维护

直接打开 `site/index.html` 即可预览。修改内容后运行 `python3 build.py`。

- `templates/layout.html`：三个页面共用的导航、页脚与元信息。
- `templates/index.html`：首页个人介绍、近期成果、代表成果、科研经历与项目、联系方式。
- `templates/research.html`：研究框架、四个方向的核心问题与方法、相关成果及长期研究目标。
- `templates/publications.html`：成果搜索和筛选页面。
- `data/publications.json`：成果书目。`featured` 控制精选，`rank` 控制展示顺序。
- `site/styles.css`：布局与样式。
- `site/app.js`：语言切换、成果搜索与筛选。
- `site/assets/portrait.png`：原仓库中的本人照片。

页面默认英文；切换语言后，在当前浏览器中保留偏好。论文题目与作者保持原始书目语言。

## GitHub Pages

目标仓库：Yang-ICTCAS/Yang-ICTCAS.github.io。
在 GitHub 仓库 Settings → Pages → Build and deployment 中选择 GitHub Actions。
审核后提交并推送 main，即由配置好的工作流生成并发布 `site/`。
目标网址：https://yang-ictcas.github.io/

发布状态与历史记录可在 GitHub 仓库的 Actions 页面查看。
此版本替代原 Hugo 构建流程；未恢复或撤销原工作区中已有的删除。

## 内容与风格

参见 `docs/design-and-sources.md`。只发布公开履历和成果；研究愿景与已完成论文分开表述。
