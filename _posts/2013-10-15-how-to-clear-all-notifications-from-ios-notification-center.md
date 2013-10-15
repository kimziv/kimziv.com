---
layout: post
category : blog
title : 如何清除ios消息中心的消息[翻译]？
tagline:  how to clear all notifications from ios notification center?
tags : [clear, cancel , notification, center, ios]
---
{% include JB/setup %}

&nbsp;&nbsp;在做ios项目过程中，ios通知中心有很多通知，我想点击其中一条，其他通知从消息中心消失掉，但是很多应用程序都不这么做。
我用Google搜索，发现了一些线索，但是都不奏效，我也做了一些研究，其实很简单。

1.如果你的app使用了applicationIconBadgeNumber，你可以把它设置为0

	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];

2.如果你的badge已经是0，你可以先把它设置为非零整数，然后再设置为0既可

	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:1];
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];

3.若上面两个方法都不奏效，可以设置一个本地通知列表，并且对这些本地通知列表不做任何操作，然后删除本地通知就行

	UIApplication* application = [UIApplication sharedApplication];
	NSArray* scheduledNotifications = [NSArray arrayWithArray:application.scheduledLocalNotifications];
	application.scheduledLocalNotifications = scheduledNotifications;
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:1];
	[[UIApplication sharedApplication] setApplicationIconBadgeNumber:0];


> [iOS Development: Remove Old Notifications From Notification Center](http://josh-asch.net/2012/02/29/ios-development-remove-old-notifications-from-notification-center/)
