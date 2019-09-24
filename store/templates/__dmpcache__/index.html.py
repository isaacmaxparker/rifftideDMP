# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569288109.7460904
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/index.html'
_template_uri = 'index.html'
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
        products = context.get('products', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
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
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nRifftide Shop\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        len = context.get('len', UNDEFINED)
        self = context.get('self', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        def site_content():
            return render_site_content(context)
        page = context.get('page', UNDEFINED)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content" style="margin:0 0px;">\r\n    <div class="parent">\r\n')
        for product in products:
            __M_writer('        <span class="product_container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('"></span>\r\n')
        __M_writer('   </div>\r\n')
        if len(products) > 0:
            __M_writer('    <table class="nextprev" width=100%>\r\n        <tr>\r\n            <td style="float:right; margin-right: 0;">\r\n')
            if page-1 != 0:
                __M_writer('                    <a class="btn btn-lg mybtn" href="/store/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
                __M_writer('">Previous</a>\r\n')
            __M_writer('            </td>\r\n        \r\n            <td width=50%>       \r\n')
            if page != numpages:
                __M_writer('                <a class="btn mybtn btn-lg" href="/store/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
                __M_writer('">Next</a>\r\n')
            __M_writer('            </td>\r\n        </tr>\r\n    </table>\r\n')
        else:
            __M_writer('    <p class = "feedback">\r\n        No Products found. Adjust the filters to broaden your search\r\n    </p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<script>\r\n        $("#filterbtn").click(function() {\r\n           if ($(".filters").hasClass("visible")){\r\n            $(".filters").removeClass("visible");\r\n            $(".filters").addClass("hidden");\r\n            $("#filterbtn").html("A");\r\n            $("#filterbtn").removeClass("buttonout");\r\n            $("#site_middle").removeClass("lefton");\r\n            $("#site_middle").addClass("leftoff");\r\n           }\r\n           else{\r\n            $(".filters").removeClass("hidden")\r\n            $(".filters").addClass("visible"); \r\n            $("#filterbtn").html("H");  \r\n            $("#filterbtn").addClass("buttonout");\r\n            $("#site_middle").removeClass("leftoff");\r\n            $("#site_middle").addClass("lefton");\r\n           }\r\n            }\r\n        )\r\n</script>\r\n\r\n<script>\r\n      if( $(filterbtn).hasclass("visible")){\r\n        alert("VISIBLE");\r\n      }  \r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "48": 1, "49": 2, "54": 6, "59": 37, "64": 67, "70": 4, "76": 4, "82": 8, "94": 8, "95": 11, "96": 12, "97": 12, "98": 12, "99": 14, "100": 15, "101": 16, "102": 19, "103": 20, "104": 20, "105": 20, "106": 20, "107": 20, "108": 22, "109": 25, "110": 26, "111": 26, "112": 26, "113": 26, "114": 26, "115": 28, "116": 31, "117": 32, "118": 36, "124": 39, "130": 39, "136": 130}}
__M_END_METADATA
"""
