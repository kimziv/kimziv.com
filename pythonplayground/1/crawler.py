# -*- coding: utf-8 -*-

__author__ = 'kimziv'
import time, json, base64, logging, hashlib, string, re
from datetime import datetime, tzinfo, timedelta
from transwarp.web import ctx, get, post, route, seeother, forbidden, jsonresult, Template
from weibo import APIError, APIClient
from setting import *
from model import Article, myData

_TD_ZERO = timedelta(0)
_TD_8 = timedelta(hours=8)

class UTC8(tzinfo):
    def utcoffset(self, dt):
        return _TD_8

    def tzname(self, dt):
        return "UTC+8:00"

    def dst(self, dt):
        return _TD_ZERO

_UTC8 = UTC8()

def _format_datetime(dt):
    t = datetime.strptime(dt, '%a %b %d %H:%M:%S +0800 %Y').replace(tzinfo=_UTC8)
    return time.mktime(t.timetuple())

def _format_user(u):
    return dict(id=str(u.id), screen_name=u.screen_name, profile_url=u.profile_url, verified=u.verified, verified_type=u.verified_type, profile_image_url=u.profile_image_url)

# def _format_weibo(st):
#     user = st.user
#     r = dict(
#         user = _format_user(st.user),
#         text = st.text,
#         created_at = _format_datetime(st.created_at),
#         reposts_count = st.reposts_count,
#         comments_count = st.comments_count,
#     )
#     if 'original_pic' in st:
#         r['original_pic'] = st.original_pic
#     if 'thumbnail_pic' in st:
#         r['thumbnail_pic'] = st.thumbnail_pic
#     if 'retweeted_status' in st:
#         r['retweeted_status'] = _format_weibo(st.retweeted_status)
#     `author`,`text`,`image_url`,`create_at`,`source`,`weibo_id`,`site_id`
#     aid = Article.add_new_article(r)
#     return r

def _format_weibo(st):
    user = st.user
    r = dict(
        author = st.user.name,
        text = st.text,
        image_url = st.bmiddle_pic,
        create_at = _format_datetime(st.created_at),
        source = 'weibo',
        weibo_id = st.mid,
        site_id = st.user.id
    )
    aid = Article.add_new_article(r)
    return r



# @route('/load')
# @jsonresult
# def load():
#     client = _create_client()
#     client.set_access_token(SINA_APP_ACCESS_TOKEN, 6300.0)
#     sites = ['1713053037', '1341267693', '1273034312', '1610362247', '1624763627', '1644225642', '1573047053', '1495037557', '1919131861', '1222135407', '1653460650', '1191965271', '2109300743', '1891422510', '1918182630', '2195315124', '1640516504', '1920061532', '1893786465', '2093879035', '2377059260', '1947267610', '1848155523', '2720880354', '2141100877', '1708242827', '2267520473', '2272568451', '1733950851', '2124580897']
#     sts = []
#     pattern=re.compile(r'预订|粉丝|微博|屏蔽|有奖|奖品|大奖|转发|转让|微信')
#     pattern2=re.compile(r'美丽说|蘑菇街')
#     for site in sites:
#         try:
#             r = client.statuses.home_timeline.get(uid=site,feature=1,count=5)
#             sts.extend(r.statuses)
#         except APIError, e:
#             return dict(error=e)
#     sts_tmp=[]
#     sts_tmp=sts[:]
#     for st in sts:
#         if ('bmiddle_pic' in st) and not pattern.search(st.text) and not pattern2.search(st.author):
#             pass
#         else:
#             sts_tmp.remove(st)
#     return [_format_weibo(s) for s in sts_tmp]

@route('/load')
@jsonresult
def load():
    client = _create_client()
    client.set_access_token(SINA_APP_ACCESS_TOKEN, 6300.0)
    sites = ['1713053037', '1341267693', '1273034312', '1610362247', '1624763627', '1644225642', '1573047053', '1495037557', '1919131861', '1222135407', '1653460650', '1191965271', '2109300743', '1891422510', '1918182630', '2195315124', '1640516504', '1920061532', '1893786465', '2093879035', '2377059260', '1947267610', '1848155523', '2720880354', '2141100877', '1708242827', '2267520473', '2272568451', '1733950851', '2124580897']
    #sts = []
    pattern=re.compile(r'预订|粉丝|微博|屏蔽|有奖|奖品|大奖|转发|转让|微信')
    pattern2=re.compile(r'美丽说|蘑菇街')
    for site in sites:
        try:
            r = client.statuses.user_timeline.get(uid=site,feature=1,count=5)
            for st in r.statuses:
                if ('bmiddle_pic' in st) and (not pattern.search(st.text)) and (not pattern2.search(st.user.name)):
                    _format_weibo(st)
            #sts.extend(r.statuses)
        except APIError, e:
            return dict(error=e)
    #sts_tmp=[]
    # for st in sts:
    #     if ('bmiddle_pic' in st) and (not pattern.search(st.text)) and (not pattern2.search(st.user.name)):
    #         _format_weibo(s)
    #         #sts_tmp.append(st)      
    #[_format_weibo(s) for s in sts_tmp]
    #return [_format_weibo(s) for s in sts_tmp]
    return {'status':0}


@route('/pick')
@jsonresult
def pick():
    id=ctx.request['id']
    last_id=ctx.request['last_id']
    # if id=='':
    #     id=Article.get_the_latest_id()
    return [Article.get_article_by_id(string.atoi(id),string.atoi(last_id))]


@route('/install')
def install():
    myData.create_tables()
    return '已经成功安装~'


@route('/')
def index_page():
    output= """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>闲读</title>
        <link rel="stylesheet" href="/static/stylesheets/main.css"/>
        <script src="/static/javascripts/jquery-1.7.2.min.js"></script>
        <script src="/static/javascripts/main.js"></script>
        <script src="/static/javascripts/moment.js"></script>
        <script src="/static/javascripts/jquery.fullscreen.min.js"></script>
    </head>
    <body onload="autoloading('next',100)">
        <div id="backTop" onclick="scrollToTop()">回顶部</div>
        <div id="main">
            <div id="top">
                <p><a href="#" onclick="autoloading('home',500)">闲读(一首歌.一点文字.一幅画)</a></p><a href="images/yuewei.apk"><!--img(src='images/android.png')--><!--img(src='images/iphone.png')--></a></div><div id="content"><div id="item"><!--#waiting 图片加载中--><img style="display: block;" src="http://ww4.sinaimg.cn/bmiddle/6e289d83jw1e4rmprxur1j20dz0973z1.jpg" id="image_url">
            <div class="right">
                <div style="display: block;" id="text"></div>
                <div style="display: block;" id="author">
                 <a href="http://weibo.com/1848155523" target="_blank">微杂志</a>
                 <span> (a day ago)</span>
                 </div>
                <div class="radio">
            <iframe src="http://douban.fm/partner/baidu/doubanradio">
            </iframe>
            </div>
            <div class="share"><a id="sinashare" href="#" itemid="519792cfe1f0ce086a00101f" onclick="share()">分享到weibo</a></div>
            <div class="share"><a href="#" title="也可以按方向键→" onclick="autoloading('next',500)">下一个</a></div>
            <div id="goPre" class="share">
                <a id="goPre" title="也可以按方向键←" href="#" onclick="autoloading('pre',500)">上一个</a><!--button(onclick='windowopen()')全屏显示-->
            </div>
        </div>
    </div>
</div>
<div id="bottom">
    <p>A man should hear a little music, read a little poetry, and see a fine picture every day of his life, in order that worldly cares may not obliterate the sense of the beautiful which God has implanted in the human soul. (Johann Wolfgang von Goethe)</p>
    <p>一个人在他的生活中应该每天听一首歌，读一点诗歌，看一幅美丽的画，以致世俗的关心不会磨灭上帝植入人类灵魂的审美能力。（歌德）</p>
    <p>@copyright2013 <a href="http://weibo.com/kimziv" target="_blank">kimziv</a></p>
</div>
<div id="tongji">

<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fbd816fc6427fc505edf33e2e7f7e6841' type='text/javascript'%3E%3C/script%3E"));
</script>

<script src="http://s19.cnzz.com/stat.php?id=5450117&web_id=5450117&show=pic" language="JavaScript"></script>
   <!-- <script src="http://s95.cnzz.com/stat.php?id=4232991&amp;web_id=1953193211">
    </script>
    <script src="http://c.cnzz.com/cnzz_core.php?web_id=4232991&amp;l=none" charset="utf-8" type="text/javascript"></script><a href="http://www.cnzz.com/stat/website.php?web_id=4232991" target="_blank" title="站长统计">站长统计</a></div></div>
    <div id="xunlei_com_thunder_helper_plugin_d462f475-c18e-46be-bd10-327458d045bd"></div>
    -->
</body>
</html>
    """
    return output;
    # @pagecache('post_list_index', PAGE_CACHE_TIME, lambda self,direction,page,base_id: page)
    # def get(self, direction = 'next', page = '2', base_id = '1'):
    #     if page == '1':
    #         self.redirect(BASE_URL)
    #         return
    #     objs = Article.get_page_posts(direction, page, base_id)
    #     if objs:
    #         if direction == 'prev':
    #             objs.reverse()            
    #         fromid = objs[0].id
    #         endid = objs[-1].id
    #     else:
    #         fromid = endid = ''
        
    #     allpost =  Article.count_all_post()
    #     allpage = allpost/EACH_PAGE_POST_NUM
    #     if allpost%EACH_PAGE_POST_NUM:
    #         allpage += 1
    #     output = self.render('index.html', {
    #         'title': "%s - %s | Part %s"%(SITE_TITLE,SITE_SUB_TITLE, page),
    #         'keywords':KEYWORDS,
    #         'description':SITE_DECR,
    #         'objs': objs,
    #         'cats': Category.get_all_cat_name(),
    #         'tags': Tag.get_hot_tag_name(),
    #         'page': int(page),
    #         'allpage': allpage,
    #         'listtype': 'index',
    #         'fromid': fromid,
    #         'endid': endid,
    #         'comments': Comment.get_recent_comments(),
    #         'links':Link.get_all_links(),
    #     },layout='_layout.html')
    #     self.write(output)
    #     return output

@get('/signin')
def signin():
    client = _create_client()
    raise seeother(client.get_authorize_url())

@get('/signout')
def signout():
    ctx.response.set_cookie(_COOKIE, 'deleted', max_age=0)
    raise seeother('/')

@get('/callback')
def callback():
    i = ctx.request.input(code='')
    code = i.code
    client = _create_client()
    r = client.request_access_token(code)
    logging.info('access token: %s' % json.dumps(r))
    access_token, expires_in, uid = r.access_token, r.expires_in, r.uid
    client.set_access_token(access_token, expires_in)
    u = client.users.show.get(uid=uid)
    logging.info('got user: %s' % uid)
    users = db.select('select * from users where id=?', uid)
    user = dict(name=u.screen_name, \
            image_url=u.avatar_large or u.profile_image_url, \
            statuses_count=u.statuses_count, \
            friends_count=u.friends_count, \
            followers_count=u.followers_count, \
            verified=u.verified, \
            verified_type=u.verified_type, \
            auth_token=access_token, \
            expired_time=expires_in)
    if users:
        db.update_kw('users', 'id=?', uid, **user)
    else:
        user['id'] = uid
        db.insert('users', **user)
    _make_cookie(uid, access_token, expires_in)
    raise seeother('/')

_COOKIE = 'authuser'
_SALT = 'A random string'

def _make_cookie(uid, token, expires_in):
    expires = str(int(expires_in))
    s = '%s:%s:%s:%s' % (str(uid), str(token), expires, _SALT)
    md5 = hashlib.md5(s).hexdigest()
    cookie = '%s:%s:%s' % (str(uid), expires, md5)
    ctx.response.set_cookie(_COOKIE, base64.b64encode(cookie).replace('=', '_'), expires=expires_in)

def _check_cookie():
    try:
        b64cookie = ctx.request.cookies[_COOKIE]
        cookie = base64.b64decode(b64cookie.replace('_', '='))
        uid, expires, md5 = cookie.split(':', 2)
        if int(expires) < time.time():
            return
        L = db.select('select * from users where id=?', uid)
        if not L:
            return
        u = L[0]
        s = '%s:%s:%s:%s' % (uid, str(u.auth_token), expires, _SALT)
        if md5 != hashlib.md5(s).hexdigest():
            return
        return u
    except BaseException:
        pass

def _create_client():
	return APIClient(SINA_APP_KEY, SINA_APP_SECRET, SINA_APP_CALLBACK_URL)