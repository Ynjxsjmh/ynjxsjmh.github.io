---
layout:     post
title:      Python3 中 bytes 和 string 之间的互相转换
subtitle:   
date:       2019-06-21 21:33
author:     在到处之间找我
header-img: 
catalog: true
category: Python
tags: []
---

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [前言](#前言)
- [创建 bytes 型数据](#创建-bytes-型数据)
- [创建字符串](#创建字符串)
- [相互转换](#相互转换)
    - [string to bytes](#string-to-bytes)
        - [按 utf-8 的方式编码，转成 bytes](#按-utf-8-的方式编码转成-bytes)
        - [按 gb2312 的方式编码，转成 bytes](#按-gb2312-的方式编码转成-bytes)
    - [bytes to string](#bytes-to-string)
        - [解码成 string，默认不填](#解码成-string 默认不填)
        - [解码成 string，使用 gb2312 的方式](#解码成-string 使用-gb2312-的方式)
- [参考资料](#参考资料)

<!-- markdown-toc end -->


# 前言
Python3 最重要的新特性大概要算是对文本（text）和二进制数据（binary data）作了更为清晰的区分。[^1]

- 文本总是 Unicode，由 str 类型表示。
- 二进制数据则由 bytes 类型表示。


那么什么是 bytes、什么是 Unicode 呢？[^2] [^3]

- 首先计算机能存储的唯一东西就是 bytes。所以为了在计算机中存储东西，我们首先得将其编码（encode），例如将其转化为 bytes。比如：
  - 要想保存音乐，我们首先得用 MP3, WAV 等将其编码
  - 要想保存图片，我们首先得用 PNG, JPEG 等将其编码
  - 要想保存文本，我们首先得用 ASCII, UTF-8 等将其编码
- Unicode 是字符集，不是字符编码。Unicode 把全世界的字符都搜集并且编号了，但是没有规定具体的编码规则。编码规则有 UTF-8、GBK 之类的。


Python3 不会以任意隐式的方式混用 str 和 bytes。正是这使得两者的区分特别清晰，你不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然），也不能将字符串传入参数为字节包的函数（反之亦然）。


# 创建 bytes 型数据
使用 Python3 的内置函数 bytes 函数。

```python
class bytes([source[, encoding[, errors]]])
```


```python
>>> bytes([1,2,3,4,5,6,7,8,9])
b'\x01\x02\x03\x04\x05\x06\x07\x08\t'

>>> bytes("python", 'ascii') # 字符串，编码
b'python'
```


# 创建字符串
```python
>>> website = 'http://www.jb51.net/'
>>> type(website)
<class 'str'>
>>> website
'http://www.jb51.net/'
```


# 相互转换
如果你仔细看给的 SO 链接那个有 bounties 的回答的话，就应该知道将 string 转化成 bytes 首先需要进行编码（encode），而 encode 是可以使用许多不同的 encodings 的[^4]。而将 bytes 转化成 string 需要进行解码（decode），解码的 encodings 往往需要根据数据的实际编码情况来设定。

## string to bytes
### 按 utf-8 的方式编码，转成 bytes
```python
>>> website_bytes_utf8 = website.encode(encoding="utf-8")
>>> type(website_bytes_utf8)
<class 'bytes'>
>>> website_bytes_utf8
b'http://www.jb51.net/'
```


### 按 gb2312 的方式编码，转成 bytes
```python
>>> website_bytes_gb2312 = website.encode(encoding="gb2312")
>>> type(website_bytes_gb2312)
<class 'bytes'>
>>> website_bytes_gb2312
b'http://www.jb51.net/'
```

## bytes to string
### 解码成 string，默认不填
```python
>>> website_string = website_bytes_utf8.decode()
>>> type(website_string)
<class 'str'>
>>> website_string
'http://www.jb51.net/'
```


### 解码成 string，使用 gb2312 的方式
```python
>>> website_string_gb2312 = website_bytes_gb2312.decode("gb2312")
>>> type(website_string_gb2312)
<class 'str'>
>>> website_string_gb2312
'http://www.jb51.net/'
```


# 参考资料
[Python3 中 bytes 和 string 之间的互相转换](http://www.jb51.net/article/105064.html)（原来的文章是转这个的，但是一年后的我看这篇文章觉得是真的水的不能再水，连个外链都没，不知道当时为啥转那篇文章，因此本文又重新改了下）

[^1]: [Text Vs. Data Instead Of Unicode Vs. 8-bit](https://docs.python.org/3/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit)

[^2]: [Unicode 和 UTF-8 有什么区别？](https://www.zhihu.com/question/23374078)

[^3]: [What is the difference between a string and a byte string?](https://stackoverflow.com/questions/6224052/what-is-the-difference-between-a-string-and-a-byte-string)

[^4]: [Standard Encodings](https://docs.python.org/2.4/lib/standard-encodings.html)

