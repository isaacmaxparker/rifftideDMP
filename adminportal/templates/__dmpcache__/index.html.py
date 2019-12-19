# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576743118.966822
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'page_title', 'left_content', 'site_content', 'right_content']


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
        request = context.get('request', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nAdmin Portal\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Admin')
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
        request = context.get('request', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n<div style="text-align: center; font-family: Josefin Sans, Century Gothic, Helvetica; font-size: 34px;">\r\n    <p class="homeparg" style="text-align: center; font-weight:bold;font-family:Century Gothic, Helvetica; font-size: 34px;">Welcome Isa')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name))
        __M_writer('!</p>\r\n</div>\r\n<table style="font-family: Josefin Sans, Century Gothic, Helvetica; Font-size: 44px;width:100%;">\r\n    <tr>\r\n        <td>\r\n            <a href="/adminportal/orders/">View Merch Orders</a>\r\n        </td>\r\n        <td>\r\n            <a href="/adminportal/users/">View/Edit Users</a>\r\n        </td>\r\n        <td>\r\n            <a href="/adminportal/scores/">View/Edit Scores</a>\r\n        </td>\r\n    </tr>\r\n    <tr>\r\n        <td>\r\n            <a href="/adminportal/newScore/">Create a New Score</a>\r\n        </td>\r\n    </tr>\r\n</table>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 5, "56": 7, "61": 11, "66": 39, "76": 3, "82": 3, "88": 7, "94": 7, "100": 9, "106": 9, "112": 14, "120": 14, "121": 17, "122": 17, "128": 41, "134": 41, "140": 134}}
__M_END_METADATA
"""
