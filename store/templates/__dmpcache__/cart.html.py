# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569535840.964063
_enable_loop = True
_template_filename = 'C:/Users/Isaac/newsite/rifftideDMP/store/templates/cart.html'
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
        round = context.get('round', UNDEFINED)
        total = context.get('total', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        shipSelect = context.get('shipSelect', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        self = context.get('self', UNDEFINED)
        personSelect = context.get('personSelect', UNDEFINED)
        SBClientId = context.get('SBClientId', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n\r\n')
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
        round = context.get('round', UNDEFINED)
        total = context.get('total', UNDEFINED)
        def site_content():
            return render_site_content(context)
        shipSelect = context.get('shipSelect', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        self = context.get('self', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content" style="padding:30px 0px;">\r\n')
        if len(saleItems) != 0:
            __M_writer('    <div class="centerTab">\r\n            <hr>\r\n        <p class="filterstitle"> Your Cart  <span class="glyphicon" style="float: right;">F</span></p>\r\n   \r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th class="cartimg">\r\n                &nbsp;\r\n            </th>\r\n            <th>\r\n                Product Name\r\n            </th>\r\n            <th>\r\n                Quantity\r\n            </th>\r\n            <th>\r\n                Size\r\n            </th>\r\n            <th>\r\n                Price\r\n            </th>\r\n           \r\n            \r\n        </tr>\r\n')
            for item in saleItems :
                __M_writer('        <tr>\r\n            <td class="cartimg">\r\n                <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
                __M_writer('" class="cartimg">\r\n            </td>\r\n            <td>\r\n                <a href="/store/product/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.id))
                __M_writer('"><p class="link">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.shirtColor.capitalize()))
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)('/' + item.product.decor.capitalize() if item.product.decor != '' else ''))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name.capitalize()))
                __M_writer(' T-Shirt</p></a>\r\n            </td>\r\n            <td>\r\n                ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
                __M_writer('\r\n            </td>\r\n            <td>\r\n              ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.size))
                __M_writer('\r\n            </td>\r\n            <td>\r\n                $')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(round(item.price,2)))
                __M_writer(' \r\n            </td>\r\n            <td>\r\n                <a class="rmv glyphicon" href="/store/cart.remove/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.id))
                __M_writer('/">B</a>\r\n            </td>\r\n        </tr>\r\n')
            __M_writer('        <tr >\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                Shipping\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(tax))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                 &nbsp;\r\n            </td>\r\n\r\n        </tr>\r\n        <tr>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    Total\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                   $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
            __M_writer('\r\n                </td>\r\n                <td>\r\n                     &nbsp;\r\n                </td>\r\n    \r\n            </tr>\r\n    </table>\r\n<hr>\r\n<p class="filterstitle">Shipping <span class="glyphicon" style="float: right;" id="shipCheck">E</span></p>\r\n<form method="POST">\r\n    <p class="formlabel" style="font-size:20px;padding-left:20px; display:inline-block;">Shipping Option:\r\n        <select name="shipSelect" class="shipSelect forminput" style="font-size:20px;padding:5px 10px;">\r\n            <option value="">  </option>\r\n            <option value="IP">In Person - FREE </option>\r\n            <option value="MAIL">UPS Shipping</option>\r\n        </select>\r\n    \r\n    <span class="personselectspan hide" name="personSelect" style="margin-left:20px;" > Referring Member:\r\n            <select name="personSelect" class="personselect forminput" style="font-size:20px;padding:5px 10px;">\r\n                <option value=" ">  </option>\r\n                <option value="LN">Loryn Norton</option>\r\n                <option value="CN">Cara Nickels</option>\r\n                <option value="BE">Bri Ellis</option>\r\n                <option value="LS">Laurel Scott</option>\r\n                <option value="ZB">Zachary Boyce</option>\r\n                <option value="IM">Isaac McDougal</option>\r\n                <option value="JJ">Johnnie Johnson</option>\r\n                <option value="SH">Samuel Hepworth</option>\r\n            </select>\r\n    </span>\r\n    \r\n    <input type="submit"  value="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Checkout' if shipSelect == None else 'Save'))
            __M_writer('" id="checkoutbtn" class="mybtn clearbtn hide" style="margin-left:20px;"></a>\r\n\r\n</form>\r\n</p>\r\n</div>\r\n')
            if shipSelect != None:
                __M_writer('<hr>\r\n<p class="filterstitle">Payment <span class="glyphicon" style="float: right;">E</span></p>\r\n<div width=100%; style="text-align: center" id="Payments">\r\n    <div id="paypal-button-container" style="display:inline-block"></div>\r\n    <hr>\r\n</div>\r\n\r\n')
            __M_writer('</div>\r\n')
        else:
            __M_writer('<div class="centerTab">\r\n    <p class="homeparg">You have no items in your cart!<br> Add one <a href="/store/">here.</a></p>\r\n    \r\n</div>\r\n\r\n')
        __M_writer('<input id="randomTag" name="orderid" type="hidden"></p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        personSelect = context.get('personSelect', UNDEFINED)
        total = context.get('total', UNDEFINED)
        SBClientId = context.get('SBClientId', UNDEFINED)
        def left_content():
            return render_left_content(context)
        shipSelect = context.get('shipSelect', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<script type="text/javascript">\r\n    $(document).ready(function(){\r\n\r\n        window.scrollTo(0,1000)\r\n\r\n        $("select.shipSelect").val("')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(shipSelect))
        __M_writer('")\r\n     \r\n        var selected = $("select.shipSelect").children("option:selected").val();\r\n   \r\n        if (selected == "IP"){\r\n            $(".personselectspan").addClass("show")\r\n            $(".personselectspan").removeClass("hide")\r\n            $("select.personselect").val("')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(personSelect))
        __M_writer('") \r\n        }\r\n        if (selected != " "){\r\n            $("#shipCheck").html(\'F\');\r\n        }\r\n\r\n\r\n        $("select.shipSelect").change(function(){\r\n            var selected = $(this).children("option:selected").val();\r\n            if (selected == "IP"){\r\n                $(".personselectspan").addClass("show")\r\n                $(".personselectspan").removeClass("hide")\r\n                $("#shippingbtn").addClass("hide")\r\n                $("#shippingbtn").removeClass("show")\r\n            }\r\n            if (selected == "MAIL"){\r\n                $(".personselectspan").addClass("hide")\r\n                $(".personselectspan").removeClass("show")\r\n                $("#checkoutbtn").addClass("show")\r\n                $("#checkoutbtn").removeClass("hide")\r\n            }            \r\n        });\r\n        $("select.personselect").change(function(){\r\n            var selected = $(this).children("option:selected").val();\r\n            if (selected == ""){\r\n                $("#checkoutbtn").addClass("hide")\r\n                $("#checkoutbtn").removeClass("show")\r\n            }\r\n            else{\r\n                $("#checkoutbtn").addClass("show")\r\n                $("#checkoutbtn").removeClass("hide")\r\n            }\r\n        });\r\n       \r\n\r\n    });\r\n    </script>\r\n\r\n<script src="https://www.paypal.com/sdk/js?client-id=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(SBClientId))
        __M_writer('&currency=USD"></script>\r\n        <script>\r\n          paypal.Buttons({\r\n            createOrder: function(data, actions) {\r\n              return actions.order.create({\r\n                purchase_units: [{\r\n                  amount: {\r\n                    value: \'')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
        __M_writer('\'\r\n                  }\r\n                }]\r\n              });\r\n            },\r\n            onApprove: function(data, actions) {\r\n              return actions.order.capture().then(function(details) {\r\n                //alert(\'Transaction completed by \' + details.payer.name.given_name);\r\n                // Call your server to save the transaction\r\n\r\n                variable = data.orderID\r\n\r\n                $.ajax({\r\n                type: "POST",\r\n                url: "/store/cart.finishSale/" + data.orderID,\r\n                }).done(function(data) {\r\n            \r\n                    window.location.href="/store/receipt/" + variable;\r\n\r\n                });\r\n\r\n              });\r\n            }\r\n          }).render(\'#paypal-button-container\');\r\n        </script>\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/newsite/rifftideDMP/store/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "51": 1, "52": 2, "57": 6, "62": 148, "72": 4, "78": 4, "84": 8, "97": 8, "98": 10, "99": 11, "100": 35, "101": 36, "102": 38, "103": 38, "104": 41, "105": 41, "106": 41, "107": 41, "108": 41, "109": 41, "110": 41, "111": 44, "112": 44, "113": 47, "114": 47, "115": 50, "116": 50, "117": 53, "118": 53, "119": 57, "120": 71, "121": 71, "122": 92, "123": 92, "124": 124, "125": 124, "126": 129, "127": 130, "128": 138, "129": 139, "130": 140, "131": 146, "137": 153, "148": 153, "149": 159, "150": 159, "151": 166, "152": 166, "153": 204, "154": 204, "155": 211, "156": 211, "162": 156}}
__M_END_METADATA
"""
