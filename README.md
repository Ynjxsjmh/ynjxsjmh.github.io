
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Introduction](#introduction)
- [Further work](#further-work)
- [More themes](#more-themes)
- [Post [front matter](https://jekyllrb.com/docs/front-matter/)](#post-front-matterhttpsjekyllrbcomdocsfront-matter)
- [Tips for customization](#tips-for-customization)
- [Possible Error](#possible-error)
- [Tips for myself](#tips-for-myself)

<!-- markdown-toc end -->


# Introduction

Fork from [qiubaiying.github.io](https://github.com/qiubaiying/qiubaiying.github.io)

# Further work

- [x] Archive, Categories, Tags: https://brucezhaor.github.io/
- [x] Support math using MathJax: https://pkuwwt.github.io/linux/2013-12-03-jekyll-using-mathjax/ && https://segmentfault.com/a/1190000008317350 
- [x] Support math using KaTeX: https://xuc.me/blog/katex-and-jekyll/ && https://karas.io/blog/math-support-with-katex-on-github-pages/ && https://stackoverflow.com/a/45301641/10315163
- [x] Show random old saying in page header: https://program-think.blogspot.com/ -> https://program-think.blogspot.com/2014/08/maxim.html?q=%E7%8C%AA%E6%A0%8F%E7%9A%84%E7%90%86%E6%83%B3 && https://jekyllcodex.org/without-plugin/randomize/
- [x] Show random poetry in page footer: https://github.com/chinese-poetry/huajianji && https://github.com/chinese-poetry/chinese-poetry
- [x] Accurate post time to minute: https://learn.cloudcannon.com/jekyll/date-formatting/
- [ ] Show access number
- [x] Show total pages
- [x] Show tag cloud: https://www.oukohou.wang/ || https://jovandeginste.github.io/2016/05/04/add-a-tag-cloud-to-my-jekyll-site.html
- [x] Add article info: https://macplay.github.io/ || http://moxfive.xyz/
- [ ] Picture changes when clicked
- [ ] Render HTML exported from Org and AsciiDoc
- [ ] Make URL clickable
- [x] Change navbar content color according to background image color: https://stackoverflow.com/questions/32928517 -> https://github.com/kennethcachia/Background-Check
- [ ] Hide timestamp in image
- [x] Article preview: http://moxfive.xyz/
- [ ] Render preview content: http://moxfive.xyz/
- [x] Pin an article: https://github.com/ibrado/jekyll-stickyposts
- [x] Clickable right side menu: https://github.com/poole/lanyon || https://github.com/cloudflare-apps/SideNav
- [ ] Icon
  - [ ] Brand icon:
    - Font awesome: https://fontawesome.com/icons
    - https://github.com/olOwOlo/hugo-theme-even
    - https://github.com/MOxFIVE/hexo-theme-yelee

-----

- [ ] Stop targeting tags: https://frontstuff.io/you-need-to-stop-targeting-tags-in-css
- [ ] Use External CSS/JS
- [x] Upgrade to Bootstrap v4
- [ ] Upgrade to less/sass: https://frontstuff.io/ -> https://github.com/sarahdayan/frontstuff


**Plugins**

[Jekyll without plugins](https://jekyllcodex.org/without-plugins/)

[Jekyll Plugins | Find Plugins for Jekyll Blogs](http://www.jekyll-plugins.com/)

[planetjekyll/awesome-jekyll-plugins](https://github.com/planetjekyll/awesome-jekyll-plugins) - https://planetjekyll.github.io/plugins/top


- [x] Back to top: https://brucezhaor.github.io/
- [ ] Toc: https://talk.jekyllrb.com/t/any-tutorials-for-styling-table-of-content/4052
  - [x] Multi-level toc: https://github.com/ghiculescu/jekyll-table-of-contents || https://github.com/Huxpro/huxpro.github.io/issues/116#issuecomment-306086066
  - [ ] Word wrap/Overflow on too long toc item
  - [ ] Toc hover/float left
  - [ ] Keep toc in article container: https://github.com/olOwOlo/hugo-theme-even
  - [x] Header and ToC mutual back: https://github.com/Ynjxsjmh/toc-backref
- [x] Add header collapse: https://github.com/szhielelp/md-post-header-collapse
- [x] Picture preview: https://lucienhsu.github.io
- [x] Search: https://lucienhsu.github.io -> https://github.com/androiddevelop/jekyll-search && https://www.oukohou.wang/
- [ ] Highlight search keywords in result
- [x] Add donation page: https://awang0608.github.io/ -> https://github.com/greedying/tctip
- [x] Non aggresive donation link: https://www.oukohou.wang/ 
- [x] Show reading progress bar: https://github.com/szhielelp/JekyllTheme-ProjectGaia
- [ ] Fancy Box: http://fancyapps.com/fancybox/
- [ ] Share: https://github.com/overtrue/share.js/ || https://jekyllcodex.org/without-plugin/share-buttons/
- [x] anchorjs: https://github.com/bryanbraun/anchorjs
- [ ] Show read time: https://jekyllcodex.org/without-plugin/reading-time-indicator/ || http://lsfalimis.github.io/customise-hpstr-jekyll-theme/#decimal
- [x] Media
  - [x] Embed web mp4
    1. Use iframe: https://stackoverflow.com/questions/10529859
    2. Use https://jekyllcodex.org/without-plugin/open-embed/ -> Synatx: Just paste `path-to-video-file.mp4` in your markdown file. eg: `https://youtu.be/iMvdG4guQf4`.
    3. Search `Jekyll Embed mp4` in Google
  - [x] Embed local vedio: Maybe [html audio/video elements example](https://github.com/mmistakes/minimal-mistakes/issues/1827)
  - [x] Embed mp3
    1. Use https://jekyllcodex.org/without-plugin/open-embed/ -> Synatx: Just paste `path-to-audio-file.mp3` in your markdown file, either relative or absolute path is ok. eg: `https://www.web3.wang/assets/audio/napianhai.mp3`.
    2. Search `jekyll embed mp3` in Google



# More themes

Except Jekyll. there exist a bunch of blog frameworks for you to choose:

- [Hugo](https://github.com/gohugoio/hugo)
- [Hexo](https://github.com/hexojs/hexo)
- [Nikola](https://github.com/getnikola/nikola)
  - https://github.com/macplay/macplay.github.io
- [pelican](https://github.com/getpelican/pelican)
  - https://github.com/honmaple/honmaple.github.io
  
Want more?  [![](./images/20200327_190259_SlIkSt.png)](https://www.google.com/search?q=blog+framework)

Here list some blog themes I admire

- [Org Mode 生成静态站点 Site](https://emacs-china.org/t/org-mode-site-v0-0-3/11409)
- [ashfinal](https://macplay.github.io/)
- [Tianyun's Blog](https://doowzs.com/blog/)
- [oukohou](https://www.oukohou.wang/)
- [Frank Lin](https://frankindev.com/)
- [mmistakes](https://github.com/mmistakes) -> https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/

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
pin:        true/false
---
```


# Tips for customization

Some files have a minified version, which is used by default. If you modify something in non-minified file and find it is not working as you expect, please check if you modify the corresponding minified file.

https://jekyllrb.com/docs/ruby-101/

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

