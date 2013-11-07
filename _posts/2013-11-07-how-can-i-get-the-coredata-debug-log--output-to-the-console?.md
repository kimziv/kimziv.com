---
layout: post
category : blog
title : 怎么在Xcode获取Core Data的调试日志？
tagline:  怎么在Xcode获取Core Data的调试日志?
tags : [Core Data, Debug , log, 日志]
---
{% include JB/setup %}

不多说了，mark一下，按照一下步骤：

	1.在Xcode左上角找到Product-> Edit Scheme;
	2.选择左边的`Run...`菜单项；
	3.选择右边的`Arguments`选项卡;
	4.在下边的`Arguments Passed On Launch`处添加参数`-com.apple.CoreData.SQLDebug 1`;
	5.运行工程，即可在xcode的Consle里看到Core Data的查询日志等。

如下图:

![ScreenShot](/attachments/2013-11-07-1.png)
![ScreenShot](/attachments/2013-11-07-2.png)
![ScreenShot](/attachments/2013-11-07-3.png)