# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1577482638.8144858
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/portal/templates/songlist.html'
_template_uri = 'songlist.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodclass', 'page_header_title', 'left_content', 'site_content', 'right_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        Scores = context.get('Scores', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        message = context.get('message', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Portal')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\nclass="back2"\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nScores\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        Scores = context.get('Scores', UNDEFINED)
        def site_content():
            return render_site_content(context)
        message = context.get('message', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content" style="background: none;">\r\n')
        if message != "NONE":
            __M_writer('       <div id="messageTag" class="message">\r\n            <span >')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(message))
            __M_writer(' </span>\r\n            <span onclick="closeMessage()"><sup>X</sup></span>\r\n        </div>\r\n')
        __M_writer('        <div style="text-align: center; font-family: Josefin Sans, Century Gothic, Helvetica; font-size: 34px;">\r\n                <p class="homeparg" style=" display:inline-block;text-align: center; font-weight:bold;font-family:Century Gothic, Helvetica; font-size: 34px;">Welcome ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name))
        __M_writer('!</p> \r\n            </div>\r\n<table class="scoreTable">\r\n    <tr class="scoreTableRow "">\r\n        <th style="text-align: left; padding-left:10%">\r\n            Score Name\r\n        </th>\r\n        <th>\r\n            View Individual Score\r\n        </th>\r\n        <th>\r\n            View Full Score\r\n        </th>\r\n    </tr>\r\n')
        for score in Scores:
            __M_writer('    <tr class="scoreTableRow ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'darkRow' if score.is_dark else ''))
            __M_writer('">\r\n        <td class="scoreTableName">\r\n            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.name))
            __M_writer('\r\n        </td>\r\n        <td class="scoreTableLinks" >\r\n')
            if score.partURL != "NONE" and score.partURL != "":
                __M_writer('            <a class="scoreTablePart" href="/portal/score/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
                __M_writer('/1">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.part))
                __M_writer('</a>\r\n')
            else:
                __M_writer('            No Individual Score Available. <a href="/portal/songlist.requestScore/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
                __M_writer('">Request One</a>           \r\n')
            __M_writer('        </td>\r\n        <td>\r\n            <a class="scoreTableAll" href="/portal/score/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
            __M_writer('/0">All Parts</a>\r\n        </td>\r\n    </tr>\r\n')
        __M_writer('</table>\r\n     \r\n      </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<script>\r\n    function closeMessage(){\r\n        document.getElementById("messageTag").style.display = "none"\r\n    }\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/portal/templates/songlist.html", "uri": "songlist.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 3, "60": 8, "65": 12, "70": 16, "75": 62, "85": 3, "91": 3, "97": 6, "103": 6, "109": 10, "115": 10, "121": 14, "127": 14, "133": 19, "143": 19, "144": 21, "145": 22, "146": 23, "147": 23, "148": 27, "149": 28, "150": 28, "151": 42, "152": 43, "153": 43, "154": 43, "155": 45, "156": 45, "157": 48, "158": 49, "159": 49, "160": 49, "161": 49, "162": 49, "163": 50, "164": 51, "165": 51, "166": 51, "167": 53, "168": 55, "169": 55, "170": 59, "176": 64, "182": 64, "188": 182}}
__M_END_METADATA
"""
