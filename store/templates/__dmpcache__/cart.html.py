# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569301624.3149185
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/cart.html'
_template_uri = 'cart.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content', 'left_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        round = context.get('round', UNDEFINED)
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
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nCart\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        total = context.get('total', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content" style="padding:30px 0px;">\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th>\r\n                &nbsp;\r\n            </th>\r\n            <th>\r\n                Product Name\r\n            </th>\r\n            <th>\r\n                Quantity\r\n            </th>\r\n            <th>\r\n                Price\r\n            </th>\r\n            <th>\r\n                Extended\r\n            </th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for item in saleItems :
            __M_writer('        <tr>\r\n            <td>\r\n                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
            __M_writer('" class="cartimg">\r\n            </td>\r\n            <td>\r\n                <a href="/store/product/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.id))
            __M_writer('"><p class="link">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('</p></a>\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n              $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(round(item.price,2)))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                    $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.price * item.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                <a class="rmv" href="/store/cart.remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.id))
            __M_writer('/">Remove</a>\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('        <tr >\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                Tax\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(tax))
        __M_writer('\r\n            </td>\r\n            <td>\r\n                 &nbsp;\r\n            </td>\r\n\r\n        </tr>\r\n        <tr>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    Total\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                   $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
        __M_writer('\r\n                </td>\r\n                <td>\r\n                     &nbsp;\r\n                </td>\r\n    \r\n            </tr>\r\n    </table>\r\n<hr>\r\n    <p class="formlabel" style="font-size:20px;padding-left:20px; display:inline-block;">Shipping Option:\r\n        <select class="shipSelect forminput" style="font-size:20px;padding:5px 10px;">\r\n            <option value="">  </option>\r\n            <option value="IP">In Person - FREE </option>\r\n            <option value="MAIL">UPS Shipping</option>\r\n        </select>\r\n    \r\n    <span class="personselectspan hide" name="personSelect" style="margin-left:20px;" > Referring Member:\r\n            <select class="personselect forminput" style="font-size:20px;padding:5px 10px;">\r\n                <option value="">  </option>\r\n                <option value="LN">Loryn Norton</option>\r\n                <option value="CN">Cara Nickels</option>\r\n                <option value="BE">Bri Ellis</option>\r\n                <option value="LS">Laurel Scott</option>\r\n                <option value="ZB">Zachary Boyce</option>\r\n                <option value="IM">Isaac McDougal</option>\r\n                <option value="JJ">Johnnie Johnson</option>\r\n                <option value="SH">Samuel Hepworth</option>\r\n            </select>\r\n    </span>\r\n    \r\n</p>\r\n<div style="align-content:center; padding-bottom:10px; display:inline-block;">\r\n        <a id="shippingbtn" class="mybtn buybtn hide" style="margin-left:20px;" href="/store/checkout/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.id))
        __M_writer('">Enter Shipping Information</a>\r\n<a id="checkoutbtn" class="mybtn buybtn hide" style="margin-left:20px;" href="/store/checkout/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.id))
        __M_writer('">Checkout now</a>\r\n</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<script type="text/javascript">\r\n    $(document).ready(function(){\r\n        $("select.shipSelect").change(function(){\r\n            var selected = $(this).children("option:selected").val();\r\n            if (selected == "IP"){\r\n                $(".personselectspan").addClass("show")\r\n                $(".personselectspan").removeClass("hide")\r\n                $("#shippingbtn").addClass("hide")\r\n                $("#shippingbtn").removeClass("show")\r\n            }\r\n            if (selected == "MAIL"){\r\n                $(".personselectspan").removeClass("show")\r\n                $(".personselectspan").addClass("hide")\r\n                $("#shippingbtn").addClass("show")\r\n                $("#shippingbtn").removeClass("hide")\r\n                $("#checkoutbtn").addClass("hide")\r\n                $("#checkoutbtn").removeClass("show")\r\n\r\n            }            \r\n        });\r\n        $("select.personselect").change(function(){\r\n            var selected = $(this).children("option:selected").val();\r\n            if (selected == ""){\r\n                $("#checkoutbtn").addClass("hide")\r\n                $("#checkoutbtn").removeClass("show")\r\n            }\r\n            else{\r\n                $("#checkoutbtn").addClass("show")\r\n                $("#checkoutbtn").removeClass("hide")\r\n            }\r\n        });\r\n    });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "48": 1, "49": 2, "54": 6, "59": 122, "69": 4, "75": 4, "81": 8, "93": 8, "94": 29, "95": 30, "96": 32, "97": 32, "98": 35, "99": 35, "100": 35, "101": 35, "102": 38, "103": 38, "104": 41, "105": 41, "106": 44, "107": 44, "108": 47, "109": 47, "110": 51, "111": 65, "112": 65, "113": 86, "114": 86, "115": 118, "116": 118, "117": 119, "118": 119, "124": 124, "130": 124, "136": 130}}
__M_END_METADATA
"""
