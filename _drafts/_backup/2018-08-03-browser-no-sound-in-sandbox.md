---
layout:     post
title:      浏览器在 sandbox 中没声音
subtitle:   
date:       2019-02-09 20:17
author:     在到处之间找我
header-img: 
catalog: true
category: Sandbox
tags:
- Sandbox
---


- [方法一：降低安全等级](#org65fb5b2)
- [方法二](#orgea633f8)

今天随便冲浪的时候找到了这个东西的解决方法（方法一没试过，方法二亲测有效）

方法来自：<https://forums.sandboxie.com/phpBB3/viewtopic.php?f=11&t=24937#p130456>

总结一下里面别人提到的解决方法：


<a id="org65fb5b2"></a>

# 方法一：降低安全等级

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-08-03-01-01.png)

第一步：在火狐地址栏键入 about:config 来到下图这样的页面

第二步：在搜索中键入 **security.sandbox.content.level** ，双击更改其值为 2（如果改为 2 还不行的话可以逐渐改小至 0，不建议）

更详细的可以看那个链接：<https://www.ghacks.net/2017/01/23/how-to-change-firefoxs-sandbox-security-level/>

值得注意的是，有人将其降为 0 都没有用：

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-08-03-01-02.png)


<a id="orgea633f8"></a>

# 方法二

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-08-03-01-03.png)

第一步：进入 about:config 页面

第二步：在搜索栏键入 **browser.tabs.remote.autostart** ，更改其值为 false

如果上述方法都不行的话，可以参考一下这个：

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-08-03-01-04.png)

主要的就是将 **browser.tabs.remote.autostart.2** 这一项人为设为 false

ps. 5.26 版的 sandbox 应该修复了此问题

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2018/2018-08-03-01-05.png)