---
layout:     post
title:      Python 递归求解汉诺塔
subtitle:   
date:       2019-02-08 23:47
author:     在到处之间找我
header-img: 
catalog: true
category: Python
tags:
- Python
- recursive
- FishCNote
---

想象有三根柱子 x, y, z，我们要将 x 上的 64 个盘子移动到 z 上。

对于游戏的解决思路，我们可以简单的分解为三个步骤：

1.  将前 63 个盘子从 x 移动到 y 上

2.  将最底下的第 64 个盘子从 x 移动到 z 上

3.  将 y 上的 63 个盘子移动到 z 上

在实现上面三个问题过程中，我们会遇到下面两个问题

1.  问题一：如何将 x 上的 63 个盘子借助 z 移动到 y 上

2.  问题二：如何将 y 上的 63 个盘子借助 x 移动到 z 上

我们可以将以上两个问题做出如下拆解：

**问题一** ：“如何将 x 上的 63 个盘子借助 z 移动到 y 上” 拆解为：

1.  将前 62 个盘子从 x 移动到 z 上

2.  将最底下的第 63 个盘子移动到 y 上

3.  将 z 上的 62 个盘子移动到 y 上

**问题二** ：“如何将 y 上的 63 个盘子借助 x 移动到 z 上” 拆解为：

1.  将前 62 个盘子从 y 移动到 x 上

2.  将最底下的第 63 个盘子移动到 z 上

3.  将 x 上的 62 个盘子移动到 y 上

运用递归的思想可以很容易的写出汉诺塔的代码：

```python
def hanoi(n, x, y, z):      #将x上的n个盘子借助y移动到z上
    'n为输入盘子的数目，xyz为三根柱子的名字'
    if n == 1:             #x上只有一个盘子的时候，直接将其移动到z上
        print(x, "->", z)
    else:
        hanoi(n-1, x, z, y) #将x上的前n-1个盘子借助z移动到y上
        print(x, "->", z)   #将x上的第n个盘子移动到z上
        hanoi(n-1, y, x, z) #将y上的n-1个盘子借助x移动到z上


n = int(input('请输入汉诺塔的盘子数'))
hanoi(n, 'x', 'y', 'z')
```