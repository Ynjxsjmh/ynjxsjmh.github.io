---
layout:     post
title:      自动机描述被 3 乘除的数
subtitle:   
date:       2019-06-21 11:29
author:     在到处之间找我
header-img: 
catalog: true
category: 编译原理
tags: [自动机]
---

- [设计 DFA 以识别所有能被 3 整除的无符号十进制数](#orgedbdf41)
- [设计 DFA 以识别所有能被 3 整除的二进制数](#org3df3758)


<a id="orgedbdf41"></a>

# 设计 DFA 以识别所有能被 3 整除的无符号十进制数

能被 3 整除的数的特征是：各位数字之和能被三整除。

所以我们可以通过记录十进制数每位数与三相除的余数，如果最后的余数之和能被三整除那该数就可以被三整除；否则不能被三整除。（除三余一的数和除三余二的数组合一定能被三整除，除三余一的数和除三余一的数除三组合一定余二）

因此我们不妨假设有三种状态：

1.  S0：余 0 状态（能被三整除）
2.  S1：余 1 状态
3.  S2：余 2 状态

三种标识符

1.  `D0 = 0|3|6|9`
2.  `D1 = 1|4|7`
3.  `D2 = 2|5|8`

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2019/2019-03-19-01-01.png)


<a id="org3df3758"></a>

# 设计 DFA 以识别所有能被 3 整除的二进制数

思路和构造十进制数类似，也是通过余数来判断。

-   每当多加一个 0 时，就相当于十进制数乘以 2（左移一位），即余数乘以 2。
-   每当多加一个 1 时，就相当于十进制数乘以 2 再加 1，即余数乘以 2 再加 1。

状态的 0、1、2 分别代表余 0、余 1、余 2 状态。

![img](https://raw.githubusercontent.com/Ynjxsjmh/ynjxsjmh.github.io/master/img/2019/2019-03-19-01-02.png)