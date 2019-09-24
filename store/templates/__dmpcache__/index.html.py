# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569304554.3025632
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content', 'left_content', 'site_right', 'right_content']


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
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        catid = context.get('catid', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
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
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

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
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        category = context.get('category', UNDEFINED)
        products = context.get('products', UNDEFINED)
        len = context.get('len', UNDEFINED)
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
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


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        catid = context.get('catid', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def left_content():
            return render_left_content(context)
        colorid = context.get('colorid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="filterpanel">\r\n  <div class="filters">\r\n      \r\n    <p class=filterstitle> <span id="filterbtn" class="">A</span>  Filters</p>\r\n    <ul>\r\n      <!-- //////////////DONT HARD CODE THIS ////////////////// -->\r\n    <li class="catlist ')
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


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n \r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<!-- <script>\r\n        $("#filterbtn").click(function() {\r\n           if ($(".filters").hasClass("visible")){\r\n            $(".filters").removeClass("visible");\r\n            $(".filters").addClass("hidden");\r\n            $("#filterbtn").html("A");\r\n            $("#filterbtn").removeClass("buttonout");\r\n            $("#site_middle").removeClass("lefton");\r\n            $("#site_middle").addClass("leftoff");\r\n           }\r\n           else{\r\n            $(".filters").removeClass("hidden")\r\n            $(".filters").addClass("visible"); \r\n            $("#filterbtn").html("H");  \r\n            $("#filterbtn").addClass("buttonout");\r\n            $("#site_middle").removeClass("leftoff");\r\n            $("#site_middle").addClass("lefton");\r\n           }\r\n            }\r\n        )\r\n</script> -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "54": 1, "55": 2, "60": 6, "65": 37, "70": 73, "75": 77, "80": 101, "86": 4, "92": 4, "98": 8, "110": 8, "111": 11, "112": 12, "113": 12, "114": 12, "115": 14, "116": 15, "117": 16, "118": 19, "119": 20, "120": 20, "121": 20, "122": 20, "123": 20, "124": 22, "125": 25, "126": 26, "127": 26, "128": 26, "129": 26, "130": 26, "131": 28, "132": 31, "133": 32, "134": 36, "140": 39, "150": 39, "151": 46, "152": 46, "153": 51, "154": 52, "155": 52, "156": 52, "157": 53, "158": 53, "159": 53, "160": 53, "161": 53, "162": 53, "163": 56, "164": 58, "165": 58, "166": 59, "167": 59, "168": 61, "169": 61, "170": 62, "171": 62, "172": 64, "173": 64, "174": 65, "175": 65, "176": 67, "177": 67, "178": 68, "179": 68, "185": 75, "191": 75, "197": 79, "203": 79, "209": 203}}
__M_END_METADATA
"""
