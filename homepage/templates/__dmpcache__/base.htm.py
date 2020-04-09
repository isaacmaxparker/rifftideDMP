# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1586395207.9951699
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'headLinks', 'page_content', 'page_scripts']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        def page_content():
            return render_page_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def headLinks():
            return render_headLinks(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n    <head>\r\n\r\n        <title>Rifftide')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/global.css">\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/global.js"></script>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headLinks'):
            context['self'].headLinks(**pageargs)
        

        __M_writer('\r\n         <!-- <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/glyphs.css">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/josefin.css">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/centurygothic.css"> -->\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logos/favicon.ico">\r\n\r\n    </head>\r\n    <body>\r\n        <div id="header">\r\n            <div id="nav">\r\n                <div class="navHead">\r\n                    <a><img class="navLogo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logos/thick logo - darker.png" alt="Rifftide Logo"></a>\r\n                </div>\r\n                <ul>\r\n                    <li>\r\n                        <a>About</a>\r\n                    </li>\r\n                    <li>\r\n                        <a>Contact</a>\r\n                    </li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n        <div id="content" class="content-wrap">\r\n            ')
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


def render_headLinks(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def headLinks():
            return render_headLinks(context)
        __M_writer = context.writer()
        __M_writer('\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/home.css">\r\n        <script src="')
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
{"filename": "C:/Users/Isaac/mysite/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "33": 2, "38": 7, "39": 10, "40": 10, "41": 10, "42": 12, "43": 12, "48": 16, "49": 17, "50": 17, "51": 18, "52": 18, "53": 19, "54": 19, "55": 22, "56": 23, "57": 23, "58": 24, "59": 24, "60": 31, "61": 31, "66": 45, "71": 74, "77": 7, "88": 13, "96": 13, "97": 14, "98": 14, "99": 15, "100": 15, "106": 44, "112": 44, "118": 57, "124": 57, "130": 124}}
__M_END_METADATA
"""
