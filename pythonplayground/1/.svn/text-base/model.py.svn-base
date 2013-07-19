# -*- coding: utf-8 -*-
import re
from time import time
from datetime import time
from setting import *
import sae
try:
	from tornado import database
except Exception, e:
	raise
else:
	pass
finally:
	pass

# if debug:
# 	#已经在setting里设置了
# 	pass
# else:
# 	import sae.const
MYSQL_DB = sae.const.MYSQL_DB
MYSQL_USER = sae.const.MYSQL_USER
MYSQL_PASS = sae.const.MYSQL_PASS
MYSQL_HOST_M = sae.const.MYSQL_HOST
MYSQL_HOST_S = sae.const.MYSQL_HOST_S
MYSQL_PORT = sae.const.MYSQL_PORT

#主数据库 进行Create,Update,Delete 操作
#从数据库 读取

mdb = database.Connection("%s:%s"%(MYSQL_HOST_M,str(MYSQL_PORT)), MYSQL_DB,MYSQL_USER, MYSQL_PASS, max_idle_time = MAX_IDLE_TIME)
sdb = database.Connection("%s:%s"%(MYSQL_HOST_S,str(MYSQL_PORT)), MYSQL_DB,MYSQL_USER, MYSQL_PASS, max_idle_time = MAX_IDLE_TIME)


class Article():

	def add_new_article(self, params):
		# query = "INSERT INTO `sp_posts` (`author`,`text`,`image_url`,`create_at`,`source`,`weibo_id`,`site_id`) VALUES(%s,%s,%s,%s,%s,%s,%s)"
		query = "INSERT IGNORE INTO `sp_posts` SET `author`=%s,`text`=%s,`image_url`=%s,`create_at`=%s,`source`=%s,`weibo_id`=%s,`site_id`=%s"
		mdb._ensure_connected()
		return mdb.execute(query, params['author'], params['text'], params['image_url'], params['create_at'], params['source'], params['weibo_id'], params['site_id'])

	def get_article_by_id(self, id,last_id):
		# if last_id <= 0:
		# 	query = 'SELECT * FROM `sp_posts` ORDER BY `create_at` DESC LIMIT 1'
		# else:
		# 	pick_id=last_id - id+1
		# 	query = 'SELECT * FROM `sp_posts` WHERE `id` = %s  ORDER BY `create_at` DESC LIMIT 1' % str(pick_id)
		if last_id <= 0:
			query = 'SELECT * FROM `sp_posts` ORDER BY `id` DESC LIMIT 1'
		else:
			pick_id=last_id - id+1
			query = 'SELECT * FROM `sp_posts` WHERE `id` = %s' % str(pick_id)
		return sdb.get(query)

	def get_the_latest_id():
		query = 'SELECT * FROM `sp_posts` WHERE `id` = %s  ORDER BY `create_at` DESC LIMIT 1' % str(id)
		res = sdb.get(query)
		data = eval(res);
		return data[0].id
	
Article = Article()

		
class MyData(object):
	def  flush_all_data(self):
		 sql = """
		 TRUNCATE TABLE `sp_posts`;
		 """
		 mdb._ensure_connected()
		 mdb.execute(sql)

	def create_tables(self):
		sql="""
DROP TABLE IF EXISTS `sp_posts`;
CREATE TABLE IF NOT EXISTS `sp_posts` (
 `id` mediumint(10) unsigned NOT NULL AUTO_INCREMENT,
 `author` varchar(50) NOT NULL DEFAULT '',
 `text` varchar(500) NOT NULL,
 `image_url` varchar(255),
 `create_at` int(10) unsigned NOT NULL,
 `source` varchar(50),
 `weibo_id` varchar(30),
 `site_id` varchar(30),
 PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
"""
		mdb._ensure_connected()
		mdb.execute(sql)



myData = MyData()



