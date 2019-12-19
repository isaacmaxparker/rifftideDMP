# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576739392.4122963
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/orders.html'
_template_uri = 'orders.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['BodyBackImage', 'page_header_title', 'site_content', 'right_content']


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
        oSales = context.get('oSales', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        dSales = context.get('dSales', UNDEFINED)
        pSales = context.get('pSales', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        rSales = context.get('rSales', UNDEFINED)
        def BodyBackImage():
            return render_BodyBackImage(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'BodyBackImage'):
            context['self'].BodyBackImage(**pageargs)
        

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


def render_BodyBackImage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def BodyBackImage():
            return render_BodyBackImage(context)
        __M_writer = context.writer()
        __M_writer('\r\n<style>\r\nhtml{\r\n    background-image: url("https://storage.cloud.google.com/rifftidesite-content/blacksparklebackground.jpg?authuser=1");\r\n}\r\n#site_middle{\r\n    background: rgba(255, 255, 255, 0.906);\r\n}\r\n</style>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nOrders\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        oSales = context.get('oSales', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        dSales = context.get('dSales', UNDEFINED)
        pSales = context.get('pSales', UNDEFINED)
        rSales = context.get('rSales', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content">\r\n    <h2>Purchased</h2>\r\n    <hr>\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th></th>\r\n            <th>\r\n                Sale\r\n            </th>\r\n            <th>\r\n                Status\r\n            </th>\r\n            <th>\r\n                Referrer\r\n            </th>\r\n            <th>\r\n                Date\r\n            </th>\r\n            <th>\r\n                Total\r\n            </th>\r\n             <th>\r\n                Options\r\n            </th>\r\n        </tr>\r\n')
        for sale in pSales:
            __M_writer('        <tr>\r\n            <td>\r\n')
            for item in sale.getitems():
                __M_writer('                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                __M_writer('" style="width:20px;display: inline-block;">\r\n')
            __M_writer('            </td>\r\n            <td>\r\n                <a href="/store/receipt/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('</a>\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.status))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.referrer))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.purchased))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('\r\n            </td>\r\n            <th>\r\n                <a href="/account/orders.update/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                    F\r\n                </a>\r\n                <a href="/account/orders.delete/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                    B\r\n                </a>\r\n            </th>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n    <h2>Ordered</h2>\r\n    <hr>\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n            <tr>\r\n                <th></th>\r\n                <th>\r\n                    Sale\r\n                </th>\r\n                <th>\r\n                    Status\r\n                </th>\r\n                <th>\r\n                    Referrer\r\n                </th>\r\n                <th>\r\n                    Date\r\n                </th>\r\n                <th>\r\n                    Total\r\n                </th>\r\n                 <th>\r\n                    Options\r\n                </th>\r\n            </tr>\r\n')
        for sale in oSales:
            __M_writer('            <tr>\r\n                    <td>\r\n')
            for item in sale.getitems():
                __M_writer('                                <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                __M_writer('" style="width:20px;display: inline-block;">\r\n')
            __M_writer('                        </td>\r\n                <td>\r\n                    <a href="/store/receipt/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('</a>\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.status))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.referrer))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.purchased))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                    ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('\r\n                </td>\r\n                <th>\r\n                    <a href="/account/orders.downdate/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                        E\r\n                    </a>\r\n                    <a></a>\r\n                    <a href="/account/orders.update/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                        F\r\n                    </a>\r\n                </th>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n    <h2>Picked Up</h2>\r\n    <hr>\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th></th>\r\n            <th>\r\n                Sale\r\n            </th>\r\n            <th>\r\n                Status\r\n            </th>\r\n            <th>\r\n                Referrer\r\n            </th>\r\n            <th>\r\n                Date\r\n            </th>\r\n            <th>\r\n                Total\r\n            </th>\r\n             <th>\r\n                Options\r\n            </th>\r\n        </tr>\r\n')
        for sale in rSales:
            __M_writer('        <tr>\r\n                <td>\r\n')
            for item in sale.getitems():
                __M_writer('                            <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                __M_writer('" style="width:20px;display: inline-block;">\r\n')
            __M_writer('                    </td>\r\n            <td>\r\n                <a href="/store/receipt/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('</a>\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.status))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.referrer))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.purchased))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('\r\n            </td>\r\n            <th>\r\n                <a href="/account/orders.downdate/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                    E\r\n                </a>\r\n                <a></a>\r\n                <a href="/account/orders.update/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                    F\r\n                </a>\r\n            </th>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n    <h2>Delivered</h2>\r\n    <hr>\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th></th>\r\n            <th>\r\n                Sale\r\n            </th>\r\n            <th>\r\n                Status\r\n            </th>\r\n            <th>\r\n                Referrer\r\n            </th>\r\n            <th>\r\n                Date\r\n            </th>\r\n            <th>\r\n                Total\r\n            </th>\r\n             <th>\r\n                Options\r\n            </th>\r\n        </tr>\r\n')
        for sale in dSales:
            __M_writer('        <tr>\r\n                <td>\r\n')
            for item in sale.getitems():
                __M_writer('                            <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                __M_writer('" style="width:20px;display: inline-block;">\r\n')
            __M_writer('                    </td>\r\n            <td>\r\n                <a href="/store/receipt/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.orderID))
            __M_writer('</a>\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.status))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.referrer))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.purchased))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.total))
            __M_writer('\r\n            </td>\r\n            <th>\r\n                <a href="/account/orders.downdate/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(sale.id))
            __M_writer('" style="font-family: Glyphter2;">\r\n                    E\r\n                </a>\r\n            </th>\r\n        </tr>\r\n')
        __M_writer('    </table>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/orders.html", "uri": "orders.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "49": 1, "50": 2, "55": 13, "60": 17, "65": 256, "75": 4, "81": 4, "87": 15, "93": 15, "99": 19, "110": 19, "111": 45, "112": 46, "113": 48, "114": 49, "115": 49, "116": 49, "117": 51, "118": 53, "119": 53, "120": 53, "121": 53, "122": 56, "123": 56, "124": 59, "125": 59, "126": 62, "127": 62, "128": 65, "129": 65, "130": 68, "131": 68, "132": 71, "133": 71, "134": 77, "135": 102, "136": 103, "137": 105, "138": 106, "139": 106, "140": 106, "141": 108, "142": 110, "143": 110, "144": 110, "145": 110, "146": 113, "147": 113, "148": 116, "149": 116, "150": 119, "151": 119, "152": 122, "153": 122, "154": 125, "155": 125, "156": 129, "157": 129, "158": 135, "159": 160, "160": 161, "161": 163, "162": 164, "163": 164, "164": 164, "165": 166, "166": 168, "167": 168, "168": 168, "169": 168, "170": 171, "171": 171, "172": 174, "173": 174, "174": 177, "175": 177, "176": 180, "177": 180, "178": 183, "179": 183, "180": 187, "181": 187, "182": 193, "183": 218, "184": 219, "185": 221, "186": 222, "187": 222, "188": 222, "189": 224, "190": 226, "191": 226, "192": 226, "193": 226, "194": 229, "195": 229, "196": 232, "197": 232, "198": 235, "199": 235, "200": 238, "201": 238, "202": 241, "203": 241, "204": 247, "210": 258, "216": 258, "222": 216}}
__M_END_METADATA
"""
