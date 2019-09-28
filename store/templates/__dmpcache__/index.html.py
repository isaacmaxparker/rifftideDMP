# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569688952.356641
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
        catid = context.get('catid', UNDEFINED)
        len = context.get('len', UNDEFINED)
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        saleItems = context.get('saleItems', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        def site_content():
            return render_site_content(context)
        page = context.get('page', UNDEFINED)
        products = context.get('products', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
            __M_writer('    <p class = "feedback">\r\n        No Products found. Adjust the filters to widen your search\r\n    </p>\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        catid = context.get('catid', UNDEFINED)
        category = context.get('category', UNDEFINED)
        colorid = context.get('colorid', UNDEFINED)
        def left_content():
            return render_left_content(context)
        self = context.get('self', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        sale = context.get('sale', UNDEFINED)
        def right_content():
            return render_right_content(context)
        self = context.get('self', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(saleItems) > 0:
            __M_writer('<a href="/store/cart/">\r\n<div class="filterpanel">\r\n        <div class="filters" style="border: 10px rgba(245, 245, 245, 0.589) solid; width: 10vw">\r\n        <p class=filterstitle>My Cart <span class="glyphicon">C</span></p>\r\n        <hr>\r\n        <ul>\r\n')
            if len(saleItems) <= 3:
                for item in saleItems:
                    __M_writer('                <li style="padding:10px;">\r\n                    <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                    __M_writer('" class="cartimg">\r\n                </li>\r\n            \r\n')
            else:
                __M_writer('            <li style="padding:10px;">\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[0].product.image_url()))
                __M_writer('" class="cartimg">\r\n            </li>\r\n            <li style="padding:10px;">\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[1].product.image_url()))
                __M_writer('" class="cartimg">\r\n            </li>\r\n            <li style="padding:10px;">\r\n                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(saleItems[2].product.image_url()))
                __M_writer('" class="cartimg">\r\n            </li>\r\n            <li style="text-align: center">...</li>\r\n')
            __M_writer('            <hr>\r\n            <li class="cartlist ">\r\n                <p>Total: $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('</p>\r\n            </li>\r\n            <hr>\r\n            <li class="cartlist bolder"> \r\n                <a href="/store/cart/">Checkout Now</a>\r\n            </li>\r\n        </ul>\r\n        </div>\r\n</div>\r\n</a>\r\n')
        __M_writer('\r\n<!-- <script>\r\n        $("#filterbtn").click(function() {\r\n           if ($(".filters").hasClass("visible")){\r\n            $(".filters").removeClass("visible");\r\n            $(".filters").addClass("hidden");\r\n            $("#filterbtn").html("A");\r\n            $("#filterbtn").removeClass("buttonout");\r\n            $("#site_middle").removeClass("lefton");\r\n            $("#site_middle").addClass("leftoff");\r\n           }\r\n           else{\r\n            $(".filters").removeClass("hidden")\r\n            $(".filters").addClass("visible"); \r\n            $("#filterbtn").html("H");  \r\n            $("#filterbtn").addClass("buttonout");\r\n            $("#site_middle").removeClass("leftoff");\r\n            $("#site_middle").addClass("lefton");\r\n           }\r\n            }\r\n        )\r\n</script> -->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "54": 1, "55": 2, "60": 6, "65": 48, "70": 84, "75": 149, "81": 4, "87": 4, "93": 8, "105": 8, "106": 11, "107": 12, "108": 14, "109": 15, "110": 15, "111": 15, "112": 16, "113": 16, "114": 18, "115": 18, "116": 19, "117": 19, "118": 19, "119": 19, "120": 20, "121": 20, "122": 25, "123": 26, "124": 27, "125": 30, "126": 31, "127": 31, "128": 31, "129": 31, "130": 31, "131": 33, "132": 36, "133": 37, "134": 37, "135": 37, "136": 37, "137": 37, "138": 39, "139": 42, "140": 43, "141": 47, "147": 50, "157": 50, "158": 57, "159": 57, "160": 62, "161": 63, "162": 63, "163": 63, "164": 64, "165": 64, "166": 64, "167": 64, "168": 64, "169": 64, "170": 67, "171": 69, "172": 69, "173": 70, "174": 70, "175": 72, "176": 72, "177": 73, "178": 73, "179": 75, "180": 75, "181": 76, "182": 76, "183": 78, "184": 78, "185": 79, "186": 79, "192": 87, "202": 87, "203": 88, "204": 89, "205": 95, "206": 96, "207": 97, "208": 98, "209": 98, "210": 102, "211": 103, "212": 104, "213": 104, "214": 107, "215": 107, "216": 110, "217": 110, "218": 114, "219": 116, "220": 116, "221": 127, "227": 221}}
__M_END_METADATA
"""
