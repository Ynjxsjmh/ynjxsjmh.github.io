---
layout:     post
title:      Python 的两个魔法方法：__repr__ 和 __str__
subtitle:   
date:       2019-02-09 11:29
author:     在到处之间找我
header-img: 
catalog: true
tags:
- python
---

  - [例子](#orgc1a2726)
  - [关系](#org9889df6)
  - [使用](#org2de4cac)
  - [官方文档](#org4561c71)
  - [参考](#orge8107a0)



<a id="orgc1a2726"></a>

# 例子

```python
>>> class A:
    pass

>>> a1 = A()
>>> a1
<__main__.A object at 0x000000000302C358>

>>> print(a1)
<__main__.A object at 0x000000000302C358>
```

```python
>>> class A:
    def __str__(self):        #__str__使用：被打印的时候需要以字符串的形式输出的时候，就会找到这个方法，并将返回值打印出来
        return "我是一个字符串"                                                                      
#要想显示对象的属性，有两种方法
#（1）return 后加上你想要格式化输出的属性,比如： return "%d %s" % (int("123"), str(123))                                                                   
#（2）利用字符串的format方法，比如："{},{}".format(1,2)	
>>> a1 = A()
>>> a1
<__main__.A object at 0x00000000033712E8>

>>> print(a1)
我是一个字符串
```

```python
>>> class A:
    def __repr__(self):   #返回一个可以用来表示对象的可打印字符串
        return "我是一个字符串"


>>> a1 = A()
>>> a1
我是一个字符串

>>> print(a1)
我是一个字符串
```

```python
>>> class A:
    def __str__(self):
        return "__str__"
    def __repr__(self):   
        return "__repr__"


>>> a1 = A()
>>> a1
__repr__
>>> print(a1)
__str__
```

此例表明：同时定义 **\_\_repr\_\_** 方法和 **\_\_str\_\_** 方法时，print() 方法会调用 **\_\_str\_\_** 方法。


<a id="org9889df6"></a>

# 关系

**\_\_str\_\_** 方法其实调用了 **\_\_repr\_\_** 方法。

> Other crucial tidbits to know: **\_\_str\_\_** on a built-on container uses the **\_\_repr\_\_**, NOT the **\_\_str\_\_**, for the items it contains.

来自 [Alex Martelli](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr/1436756#1436756)


<a id="org2de4cac"></a>

# 使用

在 [Difference between <span class="underline"><span class="underline">str</span></span> and <span class="underline"><span class="underline">repr</span></span>?](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr) 上的解释是：

-   **\_\_repr\_\_** 目的是为了表示清楚，是为开发者准备的。

-   **\_\_str\_\_** 目的是可读性好，是为使用者准备的。

我的理解是

-   **\_\_str\_\_** 就简单的表示对象，而不要让不懂编程的以为输出的是 bug。

-   **\_\_repr\_\_** 应该尽可能的表示出一个对象来源的类以及继承关系，方便程序员们了解这个对象。

```python
>>> import datetime
>>> today = datetime.datetime.now()
>>> str(today)
'2012-03-14 09:21:58.130922'
>>> repr(today)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'
```

上段程序是来自 [bitoffdev](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr/19597196#19597196) 的回答。

我们可以看到 str(today) 输出的很正常，哪个都看得懂。但是 repr(today) 的输出对不懂编程的就来说有点奇怪了，只懂一丢丢的还可能会以为自己搞出了啥幺蛾子呢。但是这对于有点经验的人来说这个就表示 today 对象是由 datetime 类实例化出来的。


<a id="org4561c71"></a>

# 官方文档

> repr(object)
> 
> Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a \_\_repr\_\_() method.

> str(object='')
> 
> Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string. If no argument is given, returns the empty string, ''.


<a id="orge8107a0"></a>

# 参考

<http://blog.csdn.net/luckytanggu/article/details/53649156>

<https://www.cnblogs.com/superxuezhazha/p/5746922.html>

<http://blog.csdn.net/DucklikeJAVA/article/details/73478307>