
# -*- coding: utf-8 -*-
#import logging
import re
import os.path
from traceback import format_exc
from urllib import unquote, quote, urlencode
from urlparse import urljoin, urlunsplit

from datetime import datetime, timedelta

import tenjin
from tenjin.helpers import *

from setting import *

import tornado.web

###
engine = tenjin.Engine(path=[os.path.join('templates', theme) for theme in [THEME,'admin']] + ['templates'], cache=tenjin.MemoryCacheStorage(), preprocess=True)
class BaseHandler(tornado.web.RequestHandler):
    
    def render(self, template, context=None, globals=None, layout=False):
        if context is None:
            context = {}
        context.update({
            'request':self.request,
        })
        return engine.render(template, context, globals, layout)

    def echo(self, template, context=None, globals=None, layout=False):
        self.write(self.render(template, context, globals, layout))
    
    def set_cache(self, seconds, is_privacy=None):
        if seconds <= 0:
            self.set_header('Cache-Control', 'no-cache')
            #self.set_header('Expires', 'Fri, 01 Jan 1990 00:00:00 GMT')
        else:
            if is_privacy:
                privacy = 'public, '
            elif is_privacy is None:
                privacy = ''
            else:
                privacy = 'private, '
            self.set_header('Cache-Control', '%smax-age=%s' % (privacy, seconds))
    

def client_cache(seconds, privacy=None):
    def wrap(handler):
        def cache_handler(self, *args, **kw):
            self.set_cache(seconds, privacy)
            return handler(self, *args, **kw)
        return cache_handler
    return wrap