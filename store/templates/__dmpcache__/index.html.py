# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569692544.6999257
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content', 'left_content', 'right_content']


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
        catid = context.get('catid', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        len = context.get('len', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        saleItems = context.get('saleItems', UNDEFINED)
        category = context.get('category', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
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
        

        __M_writer('\r\n\r\n\r\n')
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
        products = context.get('products', UNDEFINED)
        len = context.get('len', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        def site_content():
            return render_site_content(context)
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content" style="margin:0 0px;">\r\n    <div class="parent">\r\n')
        if len(products) == 0:
            __M_writer('    <p class="homeparg">Error: No Products. Contact rifftideacapella@gmail.com</p>\r\n')
        for product in products:
            __M_writer('        <span class="product_container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('">\r\n                <a class="nocolor" href="/store/product/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('">\r\n                    <div class="product-tile">\r\n                        <div ><img class="product-image" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.image_url()))
            __M_writer('"></div>\r\n                        <div class="product-name">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.cut.capitalize() if product.cut != '' else '' ))
            __M_writer(' ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name.capitalize()))
            __M_writer(' T-Shirt</div>\r\n                        <div class="product-price">$')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
            __M_writer('</div>   \r\n                    </div>\r\n                </a>\r\n        </span>\r\n')
        __M_writer('   </div>\r\n')
        if len(products) > 0:
            __M_writer('    <table class="nextprev" width=100%>\r\n        <tr>\r\n            <td style="float:right; margin-right: 0;">\r\n')
            if page-1 != 0:
                __M_writer('                    <a class="btn btn-lg mybtn" href="/store/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(colorid))
                __M_writer('">Previous</a>\r\n')
            __M_writer('            </td>\r\n        \r\n            <td width=50%>       \r\n')
            if page != numpages:
                __M_writer('                <a class="btn mybtn btn-lg" href="/store/index/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
                __M_writer('/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(colorid))
                __M_writer('">Next</a>\r\n')
            __M_writer('            </td>\r\n        </tr>\r\n    </table>\r\n')
        else:
            __M_writer('    <p class = "feedback">\r\n        No Products found. Adjust the filters to widen your search\r\n    </p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        catid = context.get('catid', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        def left_content():
            return render_left_content(context)
        category = context.get('category', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="filterpanel">\r\n  <div class="filters">\r\n      \r\n    <p class=filterstitle> <span id="filterbtn" class="">A</span>  Filters</p>\r\n    <ul>\r\n      <!-- //////////////DONT HARD CODE THIS ////////////////// -->\r\n    <li class="catlist ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('bolder' if category is None else ' '))
        __M_writer('">\r\n        <a href="/store/index/">All Shirts</a>\r\n    </li>\r\n    <hr>\r\n    <p class=filterstitle>Shirt cut</p>\r\n')
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


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def right_content():
            return render_right_content(context)
        saleItems = context.get('saleItems', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(saleItems) > 0:
            __M_writer('<a href="/store/cart/">\r\n<div class="filterpanel">\r\n        <div class="filters" style="border: 10px rgba(245, 245, 245, 0.589) solid; width: 10vw">\r\n        <p class=filterstitle>My Cart <span class="glyphicon">C</span></p>\r\n        <hr>\r\n        <ul>\r\n')
            if len(saleItems) <= 3:
                for item in saleItems:
                    __M_writer('                <li>\r\n                    <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                    __M_writer('" class="cartimg" style="width:100%">\r\n                </li>\r\n            \r\n')
            else:
                __M_writer('            <li>\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[0].product.image_url()))
                __M_writer('" class="cartimg" style="width:100%">\r\n            </li>\r\n            <li>\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[1].product.image_url()))
                __M_writer('" class="cartimg" style="width:100%">\r\n            </li>\r\n            <li>\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[2].product.image_url()))
                __M_writer('" class="cartimg" style="width:100%">\r\n            </li>\r\n            <li style="text-align: center">...</li>\r\n')
            __M_writer('            <hr>\r\n            <li class="cartlist ">\r\n                <p>Total: $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('</p>\r\n            </li>\r\n            <hr>\r\n            <li class="cartlist bolder"> \r\n                <a href="/store/cart/">Checkout Now</a>\r\n            </li>\r\n        </ul>\r\n        </div>\r\n</div>\r\n</a>\r\n')
        __M_writer('\r\n<!-- <script>\r\n        $("#filterbtn").click(function() {\r\n           if ($(".filters").hasClass("visible")){\r\n            $(".filters").removeClass("visible");\r\n            $(".filters").addClass("hidden");\r\n            $("#filterbtn").html("A");\r\n            $("#filterbtn").removeClass("buttonout");\r\n            $("#site_middle").removeClass("lefton");\r\n            $("#site_middle").addClass("leftoff");\r\n           }\r\n           else{\r\n            $(".filters").removeClass("hidden")\r\n            $(".filters").addClass("visible"); \r\n            $("#filterbtn").html("H");  \r\n            $("#filterbtn").addClass("buttonout");\r\n            $("#site_middle").removeClass("leftoff");\r\n            $("#site_middle").addClass("lefton");\r\n           }\r\n            }\r\n        )\r\n</script> -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "54": 1, "55": 2, "60": 6, "65": 48, "70": 84, "75": 149, "81": 4, "87": 4, "93": 8, "106": 8, "107": 11, "108": 12, "109": 14, "110": 15, "111": 15, "112": 15, "113": 16, "114": 16, "115": 18, "116": 18, "117": 19, "118": 19, "119": 19, "120": 19, "121": 20, "122": 20, "123": 25, "124": 26, "125": 27, "126": 30, "127": 31, "128": 31, "129": 31, "130": 31, "131": 31, "132": 31, "133": 31, "134": 33, "135": 36, "136": 37, "137": 37, "138": 37, "139": 37, "140": 37, "141": 37, "142": 37, "143": 39, "144": 42, "145": 43, "146": 47, "152": 50, "162": 50, "163": 57, "164": 57, "165": 62, "166": 63, "167": 63, "168": 63, "169": 64, "170": 64, "171": 64, "172": 64, "173": 64, "174": 64, "175": 67, "176": 69, "177": 69, "178": 70, "179": 70, "180": 72, "181": 72, "182": 73, "183": 73, "184": 75, "185": 75, "186": 76, "187": 76, "188": 78, "189": 78, "190": 79, "191": 79, "197": 87, "207": 87, "208": 88, "209": 89, "210": 95, "211": 96, "212": 97, "213": 98, "214": 98, "215": 102, "216": 103, "217": 104, "218": 104, "219": 107, "220": 107, "221": 110, "222": 110, "223": 114, "224": 116, "225": 116, "226": 127, "232": 226}}
__M_END_METADATA
"""
