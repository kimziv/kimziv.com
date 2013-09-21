---
layout: post
category : blog
title: "怎样分析苹果Crash日志文件"
tagline: "怎样分析苹果Crash日志文件"
tags : [crash,reports,dSYM,symbolicatecrash,symbolicate]
---
{% include JB/setup %}

### 问题

最近在修复项目bug过程中，需要分析ios device里crash日志文件，但是日志文件中只有函数的地址，不能看到函数名称，查资料才知道苹果这样做起到了一定的加密作用，程序真机上崩溃以后通常会留下一个.crash的日志文件，可以通过这个crash文件迅速查找到哪里崩溃了，但是这个文件中没有平时调试时候那样可以看到的函数名和函数具体调用行数，因为这里的这些信息都被转换成了16进制的地址，即使别人拿到你程序的crash日志文件也不知道哪个函数崩溃了，如下面的crash日志：

	Thread 0 Crashed:
	0 libobjc.A.dylib 0×300c87ec 0×300bb000 + 55276
	1 MobileLines 0×00006434 0×1000 + 21556
	2 MobileLines 0×000064c2 0×1000 + 21698
	3 UIKit 0×30a740ac 0×30a54000 + 131244

### 解决办法

在xcode build项目之后，在.app文件旁边看见一个同名的dSYM文件，这个文件有debug和函数和函数地址等相关信息，在发不到App Store之前一定要保留这个文件，以便后面的crash日志的分析，xcode里有一个叫symbolicatecrash的工具，Xcode4.3之后的路径是：
/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKit.framework/Versions/A/Resources/symbolicatecrash，你可以拷贝到/usr/local/bin/目录独立执行:

	sudo cp /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKit.framework/Versions/A/Resources/symbolicatecrash /usr/local/bin/

然后执行symbolicatecrash命论，可以得到完整崩溃日志记录，可以根据改日志找到crash发生在那个函数中：

 	symbolicatecrash MyApp.crash MyApp.app.dSYM > MyApp.log

解析后的崩溃日志如下：

	Thread 0 Crashed:
	0 libobjc.A.dylib 0×300c87ec objc_msgSend + 20
	1 MobileLines 0×00006434 -[CustomView setSelectedPiece:] (CustomView.m:321)
	2 MobileLines 0×000064c2 -[CustomView touchesBegan:withEvent:] (CustomView.m:349)
	3 UIKit 0×30a740ac -[UIWindow sendEvent:] + 264


注意每个.dSYM文件与产生crash日志app版本要一致的,所以如果每次编译后的dsym文件都要手动保存一次,就很麻烦，有好心人写了一个脚本,自动在编译后保存该文件.请参考:[http://www.cimgf.com/2009/12/23/automatically-save-the-dsym-files/](http://www.cimgf.com/2009/12/23/automatically-save-the-dsym-files/)

### 参考文献
* [http://developer.apple.com/tools/xcode/symbolizingcrashdumps.html](http://developer.apple.com/tools/xcode/symbolizingcrashdumps.html)
* [http://www.anoshkin.net/blog/2008/09/09/iphone-crash-logs/](http://www.anoshkin.net/blog/2008/09/09/iphone-crash-logs/)
