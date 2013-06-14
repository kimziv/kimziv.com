---
layout: post
title: "Objective C Method Swizzling剖析"
description: ""
category: objective c
tags: [method swizzling, objective c, 方法混合]
---
{% include JB/setup %}


### 一个例子

一个类SwizzlingDemo中两个方法method1和method2:

	-(void)method1
	{
		NSLog("method1 called");
	}

	-(void)method2
	{
		NSLog("method2 called");
		[self method2];//注意，这里是递归调用method2
	}

我在另一个方法test中使用SwizzlingDemo类中的方法：
	
	-(void)test
	{
		SwizzlingDemo sd=[[SwizzlingDemo alloc] init];
		[sd method1];
		MethodSwizzle([SwizzlingDemo class],
						@selector(method1),
						@selector(method2));
		[sd method1];
	}

  则输出：

  	method1 called
	method2 called
	method1 called

### 剖析

你是不是感觉很奇怪，当使用[MethodSwizzle](#ref1)方法交换两个方法之后，本来以为会出现死循环的，结果却没有发生，
这是因为在Objc中，方法分为两部分：SEL和IMP两部分,Objc runtime会根据SEL去找它指向的实现代码，在使用MethodSwizzle方法之前

* SEL(method1)->IMP(method1)
* SEL(method2)->IMP(method2)

此时若依次调用method1和method2的话，则会陷入死循环；在使用MethodSwizzle方法之后

* SEL(method1)->IMP(method2)
* SEL(method2)->IMP(method1)

此时调用[sd method1]则实际上是执行method2实现中的代码：

	NSLog("method2 called");
	[self method2];//注意，这里是递归调用method2

而`[sd method2]`则执行的是method1中代码：

	NSLog("method1 called");

所以会输出以上结果，而且不会出现死循环了。

<p id="ref1"></p>
<br/>
<br/>

<font size="1">
 [1] MethodSwizzle是一种在运行时修改方法名与方法实现映射关系的技术,常用于在系统内部方法的基础上增加新的处理流程，`method_exchangeImplementations`是runtime中常用的方法。
</font>
