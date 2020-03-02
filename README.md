# Introduction

Fork from [qiubaiying.github.io](https://github.com/qiubaiying/qiubaiying.github.io)

# Further work

- [x] Archive, Categories, Tags: https://brucezhaor.github.io/
- [x] Support math using MathJax: https://pkuwwt.github.io/linux/2013-12-03-jekyll-using-mathjax/ && https://segmentfault.com/a/1190000008317350 
- [x] Support math using KaTeX: https://xuc.me/blog/katex-and-jekyll/ && https://karas.io/blog/math-support-with-katex-on-github-pages/ && https://stackoverflow.com/a/45301641/10315163
- [ ] Show random old saying in page header: https://program-think.blogspot.com/
- [x] Accurate post time to minute: https://learn.cloudcannon.com/jekyll/date-formatting/
- [ ] Show access number
- [ ] Show read time: http://lsfalimis.github.io/customise-hpstr-jekyll-theme/#decimal
- [x] Show total pages
- [x] Show tag cloud: https://www.oukohou.wang/ || https://jovandeginste.github.io/2016/05/04/add-a-tag-cloud-to-my-jekyll-site.html
- [x] Add article info: https://macplay.github.io/
- [ ] Picture changes when clicked
- [ ] Render HTML exported from Org and AsciiDoc
- [ ] Playing mp4
- [ ] Video link preview
- [ ] Make URL clickable
- [ ] Header and ToC mutual back: https://macplay.github.io/ -> toc-backref


**Plugins**

[Jekyll without plugins](https://jekyllcodex.org/without-plugins/)

[Jekyll Plugins | Find Plugins for Jekyll Blogs](http://www.jekyll-plugins.com/)

[planetjekyll/awesome-jekyll-plugins](https://github.com/planetjekyll/awesome-jekyll-plugins) - https://planetjekyll.github.io/plugins/top

- [x] Back to top: https://brucezhaor.github.io/
- [ ] Toc
  - [x] Multi-level toc: https://github.com/ghiculescu/jekyll-table-of-contents
  - [ ] Word wrap/overflow on too long toc item
  - [ ] Toc hover/float left
- [x] Add header collapse: https://github.com/szhielelp/md-post-header-collapse
- [x] Picture preview: https://lucienhsu.github.io
- [x] Search: https://lucienhsu.github.io -> https://github.com/androiddevelop/jekyll-search && https://www.oukohou.wang/
- [ ] Highlight search keywords in result
- [x] Add donation page: https://awang0608.github.io/ -> https://github.com/greedying/tctip
- [x] Show reading progress bar: https://github.com/szhielelp/JekyllTheme-ProjectGaia
- [ ] Fancy Box: http://fancyapps.com/fancybox/
- [ ] Share: https://github.com/overtrue/share.js/
- [x] anchorjs: https://github.com/bryanbraun/anchorjs


# More themes

Here lists some blog themes I admire

- [ashfinal](https://macplay.github.io/)
- [Tianyun's Blog](https://doowzs.com/blog/)
- [oukohou](https://www.oukohou.wang/)
- [mmistakes](https://github.com/mmistakes)

# Post [front matter](https://jekyllrb.com/docs/front-matter/)

```
---
layout:     post
title:      
subtitle:
date:       2020-02-29 13:26
author:     
header-img: img/post-default-bg.jpg
category:   []
tags:       []
link:       转载连接
type:       markdown(default) | asciidoc | readtheorg
toc:        Designed for asciidoc. If you use `toc:left` in asciidoc, fill it with `left`. Otherwise, you don't need to define this value.
---
```


# Tips for customization

[Liquid Introduction](https://shopify.github.io/liquid/basics/introduction/)

- [Jekyll cheatsheet](https://devhints.io/jekyll)
- [Directory Structure](https://jekyllrb.com/docs/structure/)

 ├── _config.yml: [Variables](https://jekyllrb.com/docs/variables/)

 ├── _layouts: https://www.jekyll.com.cn/tutorials/convert-site-to-jekyll/#how-layouts-work

 │   └── default.html

 └── index.html: https://jekyllrb.com/docs/pagination/

# Possible Error

```
Liquid Exception: Liquid syntax error (line **): Variable '{{1,2,3}' was not
 properly terminated with regexp: /\}\}/ in ...
```

https://github.com/imathis/octopress/issues/466

Replace `{{` with `{ {` and `}}` with `} }`




# Tips for myself

Under blog sourcecode folder, run `jekyll serve` or `jekyll s` in cmd then browse `http://127.0.0.1:4000/` to preview the changes.

