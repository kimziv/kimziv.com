---
layout: post
title: "为什么objc里用脱字符作为block标志符"
tagline: "why objcuse ^ as block opertator"
description: ""
tags: ["objective c", "^", "block"]
---
{% include JB/setup %}

### 问题如题。

#### 答案：脱字符是c++里唯一一个没有被重载的运算符，所以苹果选择了这个定义Block，有一期wwdc里苹果的工程师讲的：[wwdc2010 session 206](http://leinax.com/s3/WWDC%202010%20Session%20Videos%20-%20HD/Session%20206%20-%20Introducing%20Blocks%20and.mov)

![it's the only unary operator we knew of that could not be operator overloaded in C++, so ...](/atachments/wwdc_2010_session_206.jpg)
