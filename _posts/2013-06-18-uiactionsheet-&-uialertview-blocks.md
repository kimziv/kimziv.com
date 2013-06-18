---
layout: post
title: Blocks 取代 Delegates
tagling:
description:
category : ios & osx
tags : [UIActionSheet,UIAlertView, Blocks, Delegate ]
---
{% include JB/setup %}


### Objective  C里Block介绍

Block和一个函数很像， 产生于一个叫做GCD的新功能，GCD用于同步处理环境下有更好的运行效率，Block把一个task封装好交给GCD,GCD在宏观上对其进行CPU和Memory等资源进行分配，Block一般长成这样：

	^(args...)
	{
		//代码
		...
	}

常用与方法回调和异步响应，在此之前使用Delegate和Protocal组合实现，编写代码的时候比较分散，比较麻烦。

### UIActionSheet & UIAlertView Blocks的实现

对于我们常用的UIActionSheet和UIAlertView等控件都的Delegate方法可以改写成Block方式来实现，现在新建一个实现UIAlertSheet的Delegate Category：

* 声明文件：`UIActionSheet+Blocks.h`

		#import <UIKit/UIKit.h>
		/*
		* Completion handler invoked when user taps a button.
		*
		* @param actionSheet The action sheet being shown.
		* @param buttonIndex The index of the button tapped.
		*/
		typedef void(^UIActionSheetHandler)(UIActionSheet *actionSheet, NSInteger buttonIndex);

		/**
		* Category of `UIActionSheet` that offers a completion handler to listen to interaction. This avoids the need of the implementation of the delegate pattern.
		*
		* @warning Completion handler: Invoked when user taps a button.
		*
		* typedef void(^UIActionSheetHandler)(UIActionSheet *actionSheet, NSInteger buttonIndex);
		*
		* - *actionSheet* The action sheet view being shown.
		* - *buttonIndex* The index of the button tapped.
		*/
		@interface UIActionSheet (Blocks) <UIActionSheetDelegate>

		/**
		* Shows the sheet from a view.
		*
		* @param view The view from which the action sheet originates.
		* @param handler The handler that will be invoked in user interaction.
		*/
		- (void)showInView:(UIView *)view handler:(UIActionSheetHandler)handler;
		@end

* 实现文件：`UIActionSheet+Blocks.m`

		#import "UIActionSheet+Blocks.h"
		#import <objc/runtime.h>
		/*
		* Runtime association key.
		*/
		static NSString *kHandlerAssociatedKey = @"kHandlerAssociatedKey";

		@implementation UIActionSheet (Blocks)

		#pragma mark - Showing

		/*
		* Shows the sheet from a view.
		*/
		- (void)showInView:(UIView *)view handler:(UIActionSheetHandler)handler {
		    
		    objc_setAssociatedObject(self, (__bridge const void *)(kHandlerAssociatedKey), handler, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
		    
		    [self setDelegate:self];
		    [self showInView:view];
		}
		@end

### 如何使用？

UIActionSheet+Blocks 是UIActionSheet的子类，提供了完整的交互式侦听处理，避免使用委派设计模式实现。使用方法如下：

1. 首先在你的类中引入UIActionSheet+Blocks.h ;
2. 按照一下方式创建UIActionSheet;

	    UIActionSheet *sheet = [[UIActionSheet alloc] initWithTitle:@"Test"
	    // Can be another value but will be overridden when showing with handler.
	             										   delegate:nil 
	                                              cancelButtonTitle:@"Cancel"
	                                         destructiveButtonTitle:@"Delete"
	                                              otherButtonTitles:@"Option 1", @"Option 2", nil];


3. 用一下方法显示UIActionSheet,在名为handler的block中编写事件响应代码;
    
		[sheet showInView:view 
		          handler:^(UIActionSheet *actionSheet, NSInteger buttonIndex) {
	                  if (buttonIndex == [actionSheet cancelButtonIndex]) {
	                      NSLog(@"Cancel button index tapped");
	                  } else if (buttonIndex == [actionSheet destructiveButtonIndex]) {
	                      NSLog(@"Destructive button index tapped");
	                  } else  {
	                      NSLog(@"Button %i tapped", buttonIndex);
	                  }                      
	    }];


  4. 对于其他show...方法，你也可以按照上面的方法进行改写：

	    - (void)showInView:(UIView *)view handler:(UIActionSheetHandler)handler;
	    - (void)showFromBarButtonItem:(UIBarButtonItem *)item animated:(BOOL)animated handler:(UIActionSheetHandler)handler;
	    - (void)showFromRect:(CGRect)rect inView:(UIView *)view animated:(BOOL)animated handler:(UIActionSheetHandler)handler;
	    - (void)showFromTabBar:(UITabBar *)view handler:(UIActionSheetHandler)handler;
	    - (void)showFromToolbar:(UIToolbar *)view handler:(UIActionSheetHandler)handler;

