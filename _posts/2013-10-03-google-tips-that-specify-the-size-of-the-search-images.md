---
layout: post
category : blog
title : Google图片搜索如何指定大小搜索图片？
tagline:  google image search tips that specify the size of the search images
tags : [google,image,size]
---
{% include JB/setup %}

### 问题

之前Google的图片搜索还可以自己定义尺寸，比起一般的搜索引擎只能选择小，中和大等选择可要高级多了，不知道最近怎么去掉了，这么好的更能竟然去掉了，不知道Google是如何考量的。

### 解决方法

经过仔细研究，发现Google并没有去掉这个功能，只是隐藏掉了，在输入搜索内容的同时加入imagesize:xxy即可，其中x, y为横纵像素值。
比如搜索`壁纸`1280×800像素的图片，使用：壁纸 imagesize:1280x800 即可。

(PS：imagesize之间不能有空格。1280x800，不能是1280*800。中间的乘号是字母x)

这样便方便搜索桌面背景等资源了，当然写blog时插入的图片也可以按自己模板的大小来指定搜索选择。

![ScreenShot](/attachments/2013-10-03T14-39-31.090Z.png)

点击`切换到标准版`，之前隐藏的功能又出来了

![ScreenShot](/attachments/2013-10-03T14-48-16.400Z.png)