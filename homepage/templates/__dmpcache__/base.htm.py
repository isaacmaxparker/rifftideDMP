# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1589771325.9779203
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_links', 'page_content', 'page_scripts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def page_content():
            return render_page_content(context._locals(__M_locals))
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_links():
            return render_page_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n    <head>\r\n        <meta charset="utf-8">\r\n        <meta name="author" content="Isaac McDougal">\r\n        <meta name="viewport" content="width=device-width,initial-scale=1.0">\r\n\r\n\r\n\r\n        <title>Rifftide')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/global.css">\r\n\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/global.js"></script>\r\n        <link rel="stylesheet" media="(max-width:1275px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/global-mobile.css">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_links'):
            context['self'].page_links(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        \r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/favicon.ico">\r\n        <script>\r\n            function checks(passed){\r\n                document.getElementById(\'navCheck\').checked = !passed\r\n                document.getElementById(\'navCheck2\').checked = !passed\r\n            }\r\n        </script>\r\n    </head>\r\n    <body>\r\n        <div id="header">\r\n            <div id="nav" class="bigMenu">\r\n                <div class="navHead">\r\n                    <a href="/"><img class="navLogo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/thick logo - darker.png" alt="Rifftide Logo"></a>\r\n                </div>\r\n                <ul>\r\n                    <li>\r\n                        <a href="/about/">About</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/cards/">Card Gallery</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/resources/">Resources</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/resources/music/">Discography</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="/resources/videos/">Music Videos</a>\r\n                    </li>\r\n                    <li>\r\n                        <a href="https://patreon.com/rifftide" target="_blank">Patreon</a>\r\n                    </li>\r\n                </ul>\r\n            </div>\r\n            <div class="lilMenu">\r\n\r\n                <div id="menuToggle">\r\n                    <div class="navHead">\r\n                        <a href="/"><img class="navLogo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/thick logo - darker.png" alt="Rifftide Logo"></a>\r\n                    </div>\r\n                    <!--\r\n                    A fake / hidden checkbox is used as click reciever,\r\n                    so you can use the :checked selector on it.\r\n                    -->\r\n                   \r\n                    \r\n                    <!--\r\n                    Some spans to act as a hamburger.\r\n                    \r\n                    They are acting like a real hamburger,\r\n                    not that McDonalds stuff.\r\n                    -->\r\n                    <input id="navCheck" type="checkbox"/>\r\n        \r\n                    <div class="spans" onclick="checks(document.getElementById(\'navCheck\').checked)">\r\n                        <input id="navCheck2" type="checkbox"/>\r\n                    <span></span>\r\n                    <span></span>\r\n                    <span></span>\r\n                    </div>\r\n                    <!--\r\n                    Too bad the menu has to be inside of the button\r\n                    but hey, it\'s pure CSS magic.\r\n                    -->\r\n                    <ul id="menu">\r\n                      <a href="/"><li>Home</li></a>\r\n                      <a href="/about/"><li>About</li></a>\r\n                      <a href="/cards/"><li>Card Gallery</li></a>\r\n                      <a href="/resources/"><li>Resources</li></a>\r\n                      <a href="/resources/music/"><li>Discography</li></a>\r\n                      <a href="/resources/videos/"><li>Music Videos</li></a>\r\n                    </ul>\r\n                  </div>\r\n            </div>\r\n        </div>\r\n        <div id="content" class="content-wrap">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_content'):
            context['self'].page_content(**pageargs)
        

        __M_writer('\r\n        </div>\r\n        <div class="footer centerRow">\r\n\r\n                <p class=icon><a href="https://instagram.com/rifftidemusic" target="_blank">d</a></p>\r\n                <p class=icon><a href="https://facebook.com/rifftideacappella" target="_blank">b</a></p>\r\n                <p>&copy; Isaac McDougal 2020</p>\r\n                <p class=icon><a href="https://Youtube.com/rifftide" target="_blank">w</a></p>\r\n                <p class=icon><a href="https://twitter.com/rifftidemusic" target="_blank">n</a></p>\r\n\r\n        </div>\r\n    </body>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_scripts'):
            context['self'].page_scripts(**pageargs)
        

        __M_writer('\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_links():
            return render_page_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/home.css">\r\n        <link rel="stylesheet" media="(max-width:1375px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/home-mobile.css">\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/home.js"></script>\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_scripts():
            return render_page_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <script type="text/javascript">\r\n            //let showLocation;\r\n            function ready(fn) {\r\n                if (document.readyState != \'loading\') {\r\n                    fn();\r\n                } else {\r\n                    document.addEventListener(\'DOMContentLoaded\', fn);\r\n                }\r\n            }\r\n\r\n            ready(function () {\r\n                Global.init();\r\n                hoverOn = Global.hoverOn\r\n                hoverOff = Global.hoverOff\r\n            });\r\n        </script>\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "34": 2, "39": 12, "40": 15, "41": 15, "42": 15, "43": 18, "44": 18, "45": 19, "46": 19, "51": 24, "52": 28, "53": 30, "54": 30, "55": 42, "56": 42, "57": 69, "58": 69, "63": 108, "68": 137, "74": 12, "85": 20, "93": 20, "94": 21, "95": 21, "96": 22, "97": 22, "98": 23, "99": 23, "105": 107, "111": 107, "117": 120, "123": 120, "129": 123}}
__M_END_METADATA
"""
