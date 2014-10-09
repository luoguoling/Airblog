Airblog+
========
博客地址: [http://airblog.net](http://airblog.net)

#概述
- **Airblog+**是一个给予**Django**开发的博客系统，项目初衷是希望构建一套由最基本功能组建而成的博客系统，做到“**极简**”为目标，让使用者尽情书写回归博客本质，重拾文字的力量。

- 项目名称的由来，其实有些小山寨，由于项目**“极简”**的核心思想，因此联想到**MACBOOKAIR**的命名，**AIR**正是形容了产品的轻薄、简单，于是**Airblog+**诞生了。**“+”**则代表了项目在极简的基础上拥有增量、可扩展的特性。

#功能

1. 文章、分类、标记

2. 图片、附件上传，支持自动生成缩略图

3. 文章评论

4. 基于**Django admin**的文章管理（增删改查）

5. **Markdown**编辑文章

#技术实现

1. 服务器端使用 Python2.7+Django1.4

2. 前端使用 bootstrap3+flat-ui

3. 分页使用了django-pagination第三方库（[项目主页](https://github.com/ericflo/django-pagination/)）

4. markdown解析使用django.contrib.markup ([参考Django官方文档](https://docs.djangoproject.com/en/1.4/ref/contrib/markup/))
5. 评论系统直接集成多说实现（[参考官方文档](http://dev.duoshuo.com/python-sdk)）

#项目截图

文章列表页

![airblog_demo_screenshot1](https://github.com/chenxc86/Airblog/blob/master/Airblog%2B/Airblog/media/demo_screenshot/airblog_demo_screenshot1.jpg)

文章详细页

![airblog_demo_screenshot2](https://github.com/chenxc86/Airblog/blob/master/Airblog%2B/Airblog/media/demo_screenshot/airblog_demo_screenshot2.jpg)
