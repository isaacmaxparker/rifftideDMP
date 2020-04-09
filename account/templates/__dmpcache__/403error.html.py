# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576734933.5831034
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/account/templates/403error.html'
_template_uri = '403error.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_header_title', 'left_content', 'site_content', 'right_content']


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
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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
        __M_writer('&mdash; Error!')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content" style="font-family: Century Gothic, Helvetica; text-align: center;">\r\n        <p style="font-size: 175px; color: rgb(100, 6, 6);">Whoops!</p>\r\n        <p style="font-size: 45px;">You don\'t have permission to view that page!</p>\r\n        <p style="font-size: 35px;">Try Logging in or contact administration to fix this error</p>\r\n     \r\n      </div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/account/templates/403error.html", "uri": "403error.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "54": 7, "59": 11, "64": 21, "74": 3, "80": 3, "86": 5, "92": 5, "98": 9, "104": 9, "110": 14, "116": 14, "122": 23, "128": 23, "134": 128}}
__M_END_METADATA
"""
