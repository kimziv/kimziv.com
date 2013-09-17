---
layout: post
category : blog
tagline: "PinYin4Objc is a popular objective-c library supporting convertion between Chinese"
tags : [pinyin,chinese,hanzi,objc,convert]
---
{% include JB/setup %}

### 特性

之前做android开发时，感觉`pinyin4j`这个库用作汉字转拼音很不错，最近就写了一个objc版本的，有以下特性：

* 效率高，使用数据缓存，第一次初始化以后，拼音数据存入文件缓存和内存缓存，后面转换效率大大提高；
* 支持自定义格式化，拼音大小写等等；
* 拼音数据完整，支持中文简体和繁体，与网络上流行的相关项目比，数据很全，几乎没有出现转换错误的问题。

	PinYin4Objc is a popular objective-c library supporting convertion between Chinese(both Simplified and Tranditional) characters and most popular Pinyin systems， it's performance is very efficient, data cached at first time. The output format of pinyin could be customized.

### 性能比较：

与之前的pinyin，POAPinyin和PYMethod等项目比较，PinYin4Objc的速度是非常快的，差不多为：0.20145秒/1000字， 如下图


### 使用 
	
	NSString *sourceText=@"我爱中文";
	HanyuPinyinOutputFormat *outputFormat=[[HanyuPinyinOutputFormat alloc] init];
	[outputFormat setToneType:ToneTypeWithoutTone];
	[outputFormat setVCharType:VCharTypeWithV];
	[outputFormat setCaseType:CaseTypeLowercase];
	NSString *outputPinyin=[PinyinHelper toHanyuPinyinStringWithNSString:sourceText withHanyuPinyinOutputFormat:outputFormat withNSString:@" "];
    	
    	
    	
### 接图

![ScreenShot](https://github.com/kimziv/PinYin4Objc/blob/master/ScreenShot.PNG)

### [项目地址](https://github.com/kimziv/PinYin4Objc)
   