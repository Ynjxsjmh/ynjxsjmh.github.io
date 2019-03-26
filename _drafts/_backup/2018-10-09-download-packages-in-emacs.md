---
layout:     post
title:      emacs 下载安装插件
subtitle:   
date:       2019-02-16 21:13
author:     在到处之间找我
header-img: 
catalog: true
tags:
- emacs
---

  - [寻找并下载插件](#寻找并下载插件)
  - [配置插件](#配置插件)
    - [新建 `init-org-download.el`](#新建-init-org-download.el)
    - [打开 `~\.emacs.d\lisp\init-elpa.el` （可省略）](#打开-.emacs.dlispinit-elpa.el-可省略)
    - [加载配置文件](#加载配置文件)
  - [个人理解](#个人理解)
  - [参考文献](#参考文献)

毫无疑问，使用 emacs 自带的 elpa 包管理器下载和管理插件是最便捷的方法

emacs 24之后的版本内置了 elpa 包管理功能，下面我来介绍如何使用 elpa 的包管理功能来方便的安装插件。 有一点得提前说明：我使用的基本上是 [陈斌的配置](https://github.com/redguardtoo/emacs.d.git)，所以以下也是在其原有结构上实现的。


<a id="寻找并下载插件"></a>

# 寻找并下载插件

我们打开 emacs 后使用 `M-x list-packages` 函数就可以列出所有可以安装的第三方包了。

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-10-09-01-01.png "在这里插入图片描述")

然后我们可以使用 `C-s` 来搜索我们想要的插件。这里我以 `org-download` 为例，该插件是一个方便 `org-mode` 插入图片的插件，有了它我们就可以很方便的在编辑过程中将图片加入到我们的 org 文件中了。

如果没有找到我们想要的插件，可以在 `init-elpa.el` 中的 `melpa-include-packages` 变量中添加。

具体下载过程不是本文重点，不再赘述。


<a id="配置插件"></a>

# 配置插件

下载完插件后，我们可以在 `~\.emacs.d\elpa` 目录下找到我们刚刚下载好的插件 `org-download` 。当然，只是这样还是不够的，我们还要继续做一些更加具体的配置才能让 emacs 启动时加载该插件。

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-10-09-01-02.png "在这里插入图片描述")


<a id="新建-init-org-download.el"></a>

## 新建 `init-org-download.el`

新建的 init-\*\*.el 根据下载插件的名字决定，这里我下载的是 org-download，因此叫 init-org-download.el 我们需要在 `~\.emacs.d\lisp` 下新建一个叫做 `init-org-download.el` 的文件，然后在里面写上：

    (require 'org-download)
    
    (provide 'init-org-download)

至于第一句 `(require 'org-download)` 这句是要根据插件本身提供的接口来写：

1.  打开我们刚刚下载到 `~\.emacs.d\elpa\org-download-0.1.0` 目录。

2.  我是在 Windows 下使的，但是安装了 `Cygwin` 来提供 Unxi/Linux 的命令。所以我在该文件夹下打开命令窗口使用 `grep -nr "provide"` 看看有提供什么接口。

3.  这里看到 `org-download.el` 这个文件给我们提供了一个叫做 `org-download` 的接口，所以我们才写了那个第一句。

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-10-09-01-03.png "在这里插入图片描述")


<a id="打开-.emacs.dlispinit-elpa.el-可省略"></a>

## 打开 `~\.emacs.d\lisp\init-elpa.el` （可省略）

然后，我们需要在打开的 `init-elpa.el` 中的 `(provide 'init-elpa)` 前面加上 `(require-package 'org-download)`

这里 `require-package` 的作用是 `Ask elpa to install given PACKAGE.` （是个自定义函数，功能可以自己去查看）

为什么要这样做呢？

我们看 [陈斌在 github 上的配置](https://github.com/redguardtoo/emacs.d) 可以发现他 github 上的配置是没有 `~\elpa` 这个文件夹的，因此我们 git clone 后在这个配置下第一次打开 emacs 的时候， `init-elpa.el` 里的一大堆 `require-package` 就负责下载这些指定的 package 到我们本地的 elpa 目录下。


<a id="加载配置文件"></a>

## 加载配置文件

最后，我们还需要在 `~\.emacs.d\init.el` 文件中添加一行 `(require 'init-org-download)` 。

这里是根据我们刚才 `(provide 'init-org-download)` 这里写的。个人感觉类似 provide 定义了一个函数，require 来调用这个函数。


<a id="个人理解"></a>

# 个人理解

对于为什么这么样划分，我在 [EmacsWiki](https://www.emacswiki.org/emacs/InitFile) 上看到的解释是： > It's often better to break up a lengthy init file into a number of EmacsLisp libraries and a small, top-level init file that loads those libraries, especially if you define commands and other functions. Some of the init files posted on EmacsWiki are organized in this way, as a set of library files.

子龙山人在其 21 天里也给出了解释：[第三天：配置文件模块化（上）](http://book.emacs-china.org/#orgheadline13)

由于自己对 git 还不是太了解，我现在有个问题是如何保证能同步更新陈斌的配置的同时保留自己的配置，希望有热心网友能指点一下。

上面那个同步问题可以参考 [issue 737](https://github.com/redguardtoo/emacs.d/issues/737)


<a id="参考文献"></a>

# 参考文献

本文对 <https://blog.csdn.net/vv_vv_vv/article/details/52992985> 这篇文章进行了补充和改进。