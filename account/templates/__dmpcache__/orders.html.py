# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1571019970.6041205
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/account/templates/orders.html'
_template_uri = 'orders.html'
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
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        pSales = context.get('pSales', UNDEFINED)
        rSales = context.get('rSales', UNDEFINED)
        dSales = context.get('dSales', UNDEFINED)
        oSales = context.get('oSales', UNDEFINED)
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
        __M_writer('\r\nReciept\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        pSales = context.get('pSales', UNDEFINED)
        self = context.get('self', UNDEFINED)
        rSales = context.get('rSales', UNDEFINED)
        dSales = context.get('dSales', UNDEFINED)
        oSales = context.get('oSales', UNDEFINED)
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
{"filename": "C:/Users/Isaac/mysite/account/templates/orders.html", "uri": "orders.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "47": 1, "48": 2, "53": 6, "58": 245, "68": 4, "74": 4, "80": 8, "91": 8, "92": 34, "93": 35, "94": 37, "95": 38, "96": 38, "97": 38, "98": 40, "99": 42, "100": 42, "101": 42, "102": 42, "103": 45, "104": 45, "105": 48, "106": 48, "107": 51, "108": 51, "109": 54, "110": 54, "111": 57, "112": 57, "113": 60, "114": 60, "115": 66, "116": 91, "117": 92, "118": 94, "119": 95, "120": 95, "121": 95, "122": 97, "123": 99, "124": 99, "125": 99, "126": 99, "127": 102, "128": 102, "129": 105, "130": 105, "131": 108, "132": 108, "133": 111, "134": 111, "135": 114, "136": 114, "137": 118, "138": 118, "139": 124, "140": 149, "141": 150, "142": 152, "143": 153, "144": 153, "145": 153, "146": 155, "147": 157, "148": 157, "149": 157, "150": 157, "151": 160, "152": 160, "153": 163, "154": 163, "155": 166, "156": 166, "157": 169, "158": 169, "159": 172, "160": 172, "161": 176, "162": 176, "163": 182, "164": 207, "165": 208, "166": 210, "167": 211, "168": 211, "169": 211, "170": 213, "171": 215, "172": 215, "173": 215, "174": 215, "175": 218, "176": 218, "177": 221, "178": 221, "179": 224, "180": 224, "181": 227, "182": 227, "183": 230, "184": 230, "185": 236, "191": 247, "197": 247, "203": 197}}
__M_END_METADATA
"""
