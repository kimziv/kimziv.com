# -*- coding: utf-8 -*-
from os import environ

APP_NAME = environ.get("APP_NAME","")
debug = not APP_NAME

# 新浪微博 app key & secret & callback url
SINA_APP_KEY ="966056985" #"1886100128"
SINA_APP_SECRET ="618742871f656e46ec33a0046631fa72"  #"7279911ed0782e5277167d24da4082cb" 89cff151907c00f5e1ec96c759880527
SINA_APP_CALLBACK_URL ="http://www.sina.com"# "http://apps.weibo.com/baicaigo/callback"
SINA_APP_ACCESS_TOKEN = "2.00_m5LIConsdDC972626a7e8xdo9jC"

#数据库配置信息
if debug:
	MYSQL_DB=''
	MYSQL_USER=''
	MYSQL_PASS=''
	MYSQL_HOST_M=''
	MYSQL_HOST_S=''
	MYSQL_PORT='3306'

MAX_IDLE_TIME = 5 #数据库最大空闲时间 SAE文档说是30 其实更小，设为5，没问题就不要改了