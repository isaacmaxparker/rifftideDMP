# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569362781.4758415
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_header_title', 'navbar_items', 'left_content', 'right_content']


from store import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Store')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nstore\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n  <li class="nav-item mynav-item">\r\n    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='index' else ' '))
        __M_writer('"  href="/store/">Store</a>\r\n  </li>         \r\n  <li class="nav-item mynav-item" id="musictab">\r\n      <a class="nav-link"  href="https://open.spotify.com/artist/6TRcbaV03EF0bofJNKUSI8" target="_blank">Music</a>\r\n  </li>  \r\n  <li class="nav-item mynav-item" style="float:right">\r\n      <a class="nav-link glyphicon twentyfour"  href="https://www.youtube.com/rifftideacapella" target="_blank">L</a>\r\n  </li> \r\n  <li id="instagram" style="float:right">\r\n    <a class="nav-link glyphicon twentyfour" href="https://www.instagram.com/rifftideacappella/" target="_blank">K</a>\r\n  </li>    \r\n  <li id="instagram" style="float:right">\r\n      <a class="nav-link glyphicon twentyfour" href="https://www.facebook.com/rifftideacappella/" target="_blank">J</a>\r\n  </li>    \r\n')
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
{"filename": "C:/Users/Isaac/mysite/store/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "48": 1, "49": 2, "54": 5, "59": 10, "64": 29, "69": 33, "74": 38, "80": 5, "86": 5, "92": 8, "98": 8, "104": 13, "112": 13, "113": 15, "114": 15, "120": 31, "126": 31, "132": 36, "138": 36, "144": 138}}
__M_END_METADATA
"""
