# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569343244.9496973
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'head', 'site_content', 'right_content']


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
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        SBClientId = context.get('SBClientId', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def head():
            return render_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

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


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        __M_writer = context.writer()
        __M_writer('\r\n<head>\r\n  <meta name="viewport" content="width=device-width, initial-scale=1">\r\n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />\r\n</head>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        SBClientId = context.get('SBClientId', UNDEFINED)
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n          <div id="paypal-button-container"></div>\r\n\r\n      </div>\r\n\r\n      \r\n\r\n        <!-- Include the PayPal JavaScript SDK -->\r\n        <script src="https://www.paypal.com/sdk/js?client-id=')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(SBClientId))
        __M_writer('&currency=USD"></script>\r\n        <script>\r\n          paypal.Buttons({\r\n            createOrder: function(data, actions) {\r\n              return actions.order.create({\r\n                purchase_units: [{\r\n                  amount: {\r\n                    value: \'0.01\'\r\n                  }\r\n                }]\r\n              });\r\n            },\r\n            onApprove: function(data, actions) {\r\n              return actions.order.capture().then(function(details) {\r\n                alert(\'Transaction completed by \' + details.payer.name.given_name);\r\n                // Call your server to save the transaction\r\n                return fetch(\'/paypal-transaction-complete\', {\r\n                  method: \'post\',\r\n                  headers: {\r\n                    \'content-type\': \'application/json\'\r\n                  },\r\n                  body: JSON.stringify({\r\n                    orderID: data.orderID\r\n                  })\r\n                });\r\n              });\r\n            }\r\n          }).render(\'#paypal-button-container\');\r\n        </script>\r\n\r\n\r\n')
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
{"filename": "C:/Users/Isaac/mysite/store/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "19": 3, "31": 0, "46": 1, "47": 2, "52": 6, "57": 13, "62": 55, "72": 4, "78": 4, "84": 8, "90": 8, "96": 15, "104": 15, "105": 24, "106": 24, "112": 57, "118": 57, "124": 118}}
__M_END_METADATA
"""
