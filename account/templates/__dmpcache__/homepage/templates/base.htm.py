# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1571016444.3363037
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'head', 'navbar_items', 'page_header_title', 'left_content', 'site_content', 'site_right', 'right_content']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n\r\n    <title>\r\n        Rifftide\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n        </title>\r\n\r\n \r\n')
        __M_writer('        <!-- <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\jquery.js"></script> -->\r\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/js/bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/css/bootstrap.min.css" rel="stylesheet" type="text/css">\r\n        <!-- <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script> -->\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/glyphs.css">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/josefin.css">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/fonts/centurygothic.css">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/base.scss">\r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/base.scss.css">\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico">\r\n\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        __M_writer('\r\n\r\n<style>\r\nbody{\r\n\r\n    background-image: url("https://storage.cloud.google.com/rifftidesite-content/whitesparkle2.jpg");\r\n}\r\n.bigger{\r\n    font-size:178px !important;\r\n    text-shadow: 0px 12px 13px rgba(11, 216, 216, 0.699) !important;\r\n}\r\n</style>\r\n\r\n    </head>\r\n    <body>\r\n        <header>\r\n        <div id="Topbar">\r\n            \r\n                <ul class="myNav">\r\n                    <li class="homeImg">\r\n                        <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/thick logo.png" alt="python"  />\r\n                    </li>\r\n                    <li>\r\n\r\n                    </li>\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                 </ul>\r\n        </div>\r\n\r\n            <div id="bigTitle" class="title ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bigger' if request.dmp.page =='index' else ''))
        __M_writer('" style="font-family:Josefin;font-weight: bolder;">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('</div>\r\n        </header>\r\n        \r\n       <table class=main>\r\n           <tr>\r\n            <td id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n            </td>\r\n            \r\n            <td id="site_middle">\r\n           \r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n            </td>\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n            </td>\r\n        </tr>\r\n        </table>\r\n\r\n        <footer>\r\n            \r\n            ')
        __M_writer('\r\n\r\n           <p class="copy"> &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().strftime("%Y") ))
        __M_writer(' Isaac McDougal</p>\r\n\r\n        </footer>\r\n\r\n        </body>\r\n\r\n</html>\r\n<script>\r\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n                My Project!\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n                We are\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('Left Side')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('Error Page Content not found')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <td id="site_right" >\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('right Side')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 90, "19": 91, "20": 0, "44": 2, "49": 11, "50": 16, "51": 16, "52": 16, "53": 18, "54": 18, "55": 19, "56": 19, "57": 23, "58": 23, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26, "64": 26, "65": 27, "66": 27, "67": 29, "68": 30, "69": 30, "70": 31, "71": 31, "76": 34, "77": 54, "78": 54, "83": 61, "84": 65, "85": 65, "90": 67, "95": 73, "100": 78, "105": 82, "110": 83, "111": 90, "112": 92, "113": 92, "119": 9, "125": 9, "131": 33, "137": 33, "143": 59, "149": 59, "155": 65, "161": 65, "167": 73, "173": 73, "179": 78, "185": 78, "191": 80, "197": 80, "203": 83, "209": 83, "215": 209}}
__M_END_METADATA
"""
