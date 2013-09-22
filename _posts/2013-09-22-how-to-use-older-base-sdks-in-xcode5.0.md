---
layout: post
category : blog
title : 怎样在xcode5中使用低版本sdk，解决兼容ios7ui问题
tagline: how to use older base sdks in xcode5.0
tags : [xcode5,base sdk,older,ios7]
---
{% include JB/setup %}

### 问题

令人头疼的是，xcode每次升级都会使用最新版本的sdk，而且只有最新版本的sdk，对之前老版本的sdk都没有默认安装，这搞的最近我很头疼，
最近我升级到Xcode5.0版本，编译后运行后，在ios7.0上显示ui非常乱，我不可能自己重新换一套正对ios7.0的ui，即使换也需要时间，这个版本不可能换，需要设计师重新设计一套，汗，只能自己折腾，果然Google是好帮手，可以在新版本Xcode中添加老版本的sdk：
### 解决方法

首先得有老版本的sdk，如果你已经安装了Xcode5.0，那么老版本的sdk `iPhoneOS6.1.sdk`已经被删除了，你可以从同事电脑里拷贝一份，路径是：`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs`，我从同事电脑考了一份，汗，又编译出错，找不到头文件，只好重写下载Xcode4.6.3，打开dmg镜像文件，从路径`/Volumes/Xcode/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer`拷贝`iPhoneOS6.1.sdk`到路径
`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs`目录即可

### 提示

对于还没有安装Xcode5.0的童鞋，在安装之前最好备份一下`iPhoneOS6.1.sdk`目录，在安装Xcode5.0之后拷贝到相关目录`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs`即可以使用sdk6.1了，在项目中设置，如下图：

![ScreenShot](/attachments/2013-09-22-base-sdk.png)

附iPhoneOS6.1.sdk下载链接：[iPhoneOS6.1.sdk](http://pan.baidu.com/share/link?shareid=3844278108&uk=3675764550)