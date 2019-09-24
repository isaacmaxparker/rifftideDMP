# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569300300.8477411
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content', 'right_content']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        __M_writer('\r\nCheckout\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content" style="margin-left:5%; padding-right:9%; width: 90%">\r\n\r\n        <form action="" method="post">\r\n            \r\n            <table class="formlabel">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
        __M_writer('\r\n            </table>\r\n\r\n            <hr>\r\n            <p class="btn btn-lg buybtn" style="margin-left:80%; margin-top:20px;" href="/catalog/checkout">Checkout</p>\r\n          </form>\r\n\r\n      </div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/store/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "44": 1, "45": 2, "50": 6, "55": 22, "65": 4, "71": 4, "77": 8, "85": 8, "86": 14, "87": 14, "93": 24, "99": 24, "105": 99}}
__M_END_METADATA
"""
