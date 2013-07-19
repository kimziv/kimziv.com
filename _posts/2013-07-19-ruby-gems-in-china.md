---
layout: post
title: "如何解决国内安装gem的问题"
tagline: "how to install gem in China"
description: ""
tags: ["gem", "翻墙", "ruby"]
---
{% include JB/setup %}

几次在bash里执行`gem install bundler` 都会出现以下问题

	ERROR:  Could not find a valid gem 'bundler' (>= 0), here is why:
          Unable to download data from https://rubygems.org/ - Errno::ETIMEDOUT: Operation timed out - connect(2) (https://rubygems.org/latest_specs.4.8.gz)
	ERROR:  Possible alternatives: bundler

之前买的VPN又用完了，太让我失望了，国内的GFW，于是自己动手，丰衣足食，偶然发现国内还有一个淘宝gems mirror，废话少说，接下来告诉你怎么解决问题吧：
	$ gem sources --remove https://rubygems.org/
	$ gem sources -a http://ruby.taobao.org/
	$ gem sources -l
	*** CURRENT SOURCES ***

	http://ruby.taobao.org
	# 请确保只有 ruby.taobao.org
	$ gem install rails

### 如果你是用 Bundle (Rails 项目)
	source 'http://ruby.taobao.org/'
	gem 'rails', '3.2.12'
	...

### Ruby 源代码下载

 *	[ruby-2.0.0-p247.tar.gz](http://ruby.taobao.org/mirrors/ruby/2.0/ruby-2.0.0-p247.tar.gz)
 *	[ruby-1.9.3-p448.tar.gz](http://ruby.taobao.org/mirrors/ruby/1.9/ruby-1.9.3-p448.tar.gz)
 *	[ruby-1.9.2-p320.tar.gz](http://ruby.taobao.org/mirrors/ruby/1.9/ruby-1.9.2-p320.tar.gz)
 *	[ruby-1.8.7-p358.tar.gz](http://ruby.taobao.org/mirrors/ruby/1.8/ruby-1.8.7-p358.tar.gz)

 ### RVM 改用本站作为下载源, 提高 Ruby 安装速度

 *	For Mac

 	$ sed -i .bak 's!ftp.ruby-lang.org/pub/ruby!ruby.taobao.org/mirrors/ruby!' $rvm_path/config/db

 *	For Linux

 	$ sed -i 's!ftp.ruby-lang.org/pub/ruby!ruby.taobao.org/mirrors/ruby!' $rvm_path/config/db

附：[淘宝 Ruby官方FTP镜像](http://ruby.taobao.org/mirrors/ruby)

经查明，由于国内网络原因（你懂的），导致 [rubygems.org](http://rubygems.org/) 存放在 Amazon S3 上面的资源文件间歇性连接失败。所以你会与遇到 `gem install rack` 或 `bundle install` 的时候半天没有响应，具体可以用 `gem install rails -V` 来查看执行过程。
