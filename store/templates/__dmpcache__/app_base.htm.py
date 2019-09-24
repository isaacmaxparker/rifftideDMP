# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569288197.7994466
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_header_title', 'navbar_items', 'left_content', 'site_middle', 'right_content']


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
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        filtered = context.get('filtered', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        catid = context.get('catid', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_middle():
            return render_site_middle(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
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
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_middle'):
            context['self'].site_middle(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n<li class="mynav-item">\r\n  <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
        __M_writer('"  href="/">Home</a>\r\n</li>\r\n  <li class="nav-item mynav-item">\r\n    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='index' else ' '))
        __M_writer('"  href="/store/">Store</a>\r\n  </li>             \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        filtered = context.get('filtered', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        catid = context.get('catid', UNDEFINED)
        def left_content():
            return render_left_content(context)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="filterpanel">\r\n    <button id="filterbtn" class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('buttonout' if filtered else ''))
        __M_writer('">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('H' if filtered else 'A'))
        __M_writer('</button>\r\n  <div class="filters ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('visible' if filtered else 'hidden'))
        __M_writer('">\r\n    <p class=filterstitle>Filters</p>\r\n    <ul>\r\n      <!-- //////////////DONT HARD CODE THIS ////////////////// -->\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if category is None else ' '))
        __M_writer('">\r\n        <a href="/store/index/">All Products</a>\r\n    </li>\r\n    <hr>\r\n    <p class=filterstitle>Shirt cut</p>\r\n')
        for cat in cmod.Category.objects.order_by('name'):
            __M_writer('    <li class="catlist ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if category == cat else ' '))
            __M_writer('">\r\n      <a href="/store/index/1/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cat.id))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(colorid))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cat.name))
            __M_writer('</a>\r\n    </li>\r\n')
        __M_writer('    <hr>\r\n    <p class=filterstitle>Shirt color</p>\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if colorid == 1 else ' '))
        __M_writer('">\r\n      <a href="/store/index/1/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(catid))
        __M_writer('/1">Black</a>\r\n    </li>\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if colorid == 2 else ' '))
        __M_writer('">\r\n        <a href="/store/index/1/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(catid))
        __M_writer('/2">White</a>\r\n    </li>\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if colorid == 3 else ' '))
        __M_writer('">\r\n        <a href="/store/index/1/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(catid))
        __M_writer('/3">Teal</a>\r\n    </li>\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if colorid == 4 else ' '))
        __M_writer('">\r\n        <a href="/store/index/1/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(catid))
        __M_writer('/4">Grey</a>\r\n    </li>\r\n    </ul>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_middle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_middle():
            return render_site_middle(context)
        self = context.get('self', UNDEFINED)
        filtered = context.get('filtered', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="site_middle" class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('lefton' if filtered else 'leftoff'))
        __M_writer('">\r\n')
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
{"filename": "C:/Users/Isaac/mysite/store/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "54": 1, "55": 2, "60": 5, "65": 10, "70": 20, "75": 56, "80": 60, "85": 64, "91": 5, "97": 5, "103": 8, "109": 8, "115": 13, "123": 13, "124": 15, "125": 15, "126": 18, "127": 18, "133": 22, "144": 22, "145": 24, "146": 24, "147": 24, "148": 24, "149": 25, "150": 25, "151": 29, "152": 29, "153": 34, "154": 35, "155": 35, "156": 35, "157": 36, "158": 36, "159": 36, "160": 36, "161": 36, "162": 36, "163": 39, "164": 41, "165": 41, "166": 42, "167": 42, "168": 44, "169": 44, "170": 45, "171": 45, "172": 47, "173": 47, "174": 48, "175": 48, "176": 50, "177": 50, "178": 51, "179": 51, "185": 58, "193": 58, "194": 59, "195": 59, "201": 62, "207": 62, "213": 207}}
__M_END_METADATA
"""
