# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1586840284.9575367
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
        settings = context.get('settings', UNDEFINED)
        def page_links():
            return render_page_links(context._locals(__M_locals))
        def page_content():
            return render_page_content(context._locals(__M_locals))
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n    <head>\r\n        <meta charset="utf-8">\r\n        <meta name="author" content="Isaac McDougal">\r\n        <meta name="viewport" content="width=device-width,initial-scale=1.0">\r\n\r\n        <style>\r\n            @media(max-width:1200px){\r\n    .homeSlideImage{\r\n        max-width:100vw;\r\n        min-width:100vw;\r\n        min-height: 70vh !important;\r\n        object-fit: cover;\r\n    }\r\n\r\n    .homeTitle{\r\n        font-size: calc(100vw / 5) !important;\r\n        word-break: keep-all;\r\n        text-align: center;\r\n        width: 90vw;\r\n        margin-left: 5vw;\r\n    }\r\n    \r\n    #slidediv1{\r\n        width: 80vw;\r\n        left:10vw;\r\n        margin-top: 55px;\r\n        max-height: calc(90vh - 55px);\r\n    }\r\n    \r\n    #slidediv1 div{\r\n        margin-top: 50%;\r\n        transform: translate(0,-50%);\r\n    }\r\n\r\n    #p1{\r\n        font-size: calc(100vw / 6.5) !important;\r\n    }\r\n\r\n    #down1{\r\n        display: none;\r\n    }\r\n}\r\n\r\n@media(max-width:900px){\r\n\r\n    #slidediv1{\r\n        margin-top: calc(10vh + 55px);\r\n        max-height: calc(80vh - 55px);\r\n    }\r\n\r\n    #rifftide{\r\n        font-size: 250% !important;\r\n        text-align: left;\r\n        line-height: 75%;\r\n    }\r\n    .homeIcon{\r\n        font-size: calc(100vw / 8) !important;\r\n    }\r\n    .splitter{\r\n        display: block;\r\n        font-size: 1vw;\r\n    }\r\n    #we{\r\n        margin-left: 30vw;\r\n    }\r\n    #riff{\r\n        margin-left:-5vw;\r\n    }\r\n    #tide{\r\n        margin-left:5vw;\r\n    }\r\n    \r\n    #slidediv1 div{\r\n        margin-top: 50%;\r\n        transform: translate(0,-30%);\r\n    }\r\n\r\n}\r\n\r\n@media(max-width:600px){\r\n    #slidediv1 div{\r\n        margin-top: 50%;\r\n        transform: translate(0,-40%);\r\n    }\r\n}\r\n        </style>\r\n\r\n        <title>Rifftide')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/global.css">\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/global.js"></script>\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_links'):
            context['self'].page_links(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        \r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/favicon.ico">\r\n\r\n    </head>\r\n    <body>\r\n        <div id="header">\r\n            <div id="nav">\r\n                <div class="navHead">\r\n                    <a><img class="navLogo" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/thick logo - darker.png" alt="Rifftide Logo"></a>\r\n                </div>\r\n                <ul>\r\n                    <li>\r\n                        <a>About</a>\r\n                    </li>\r\n                    <li>\r\n                        <a>Contact</a>\r\n                    </li>\r\n                </ul>\r\n            </div>\r\n        </div>\r\n        <div id="content" class="content-wrap">\r\n            ')
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
        def page_links():
            return render_page_links(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
{"filename": "C:/Users/isaac/rifftideDMP/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 0, "34": 2, "39": 92, "40": 95, "41": 95, "42": 95, "43": 97, "44": 97, "49": 101, "50": 105, "51": 107, "52": 107, "53": 114, "54": 114, "59": 128, "64": 157, "70": 92, "81": 98, "89": 98, "90": 99, "91": 99, "92": 100, "93": 100, "99": 127, "105": 127, "111": 140, "117": 140, "123": 117}}
__M_END_METADATA
"""
