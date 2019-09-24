# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569287110.5967517
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/store/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'left_content', 'site_content', 'right_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        shirtColor = context.get('shirtColor', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        desc = context.get('desc', UNDEFINED)
        variations = context.get('variations', UNDEFINED)
        self = context.get('self', UNDEFINED)
        price = context.get('price', UNDEFINED)
        decorColor = context.get('decorColor', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        imageurl = context.get('imageurl', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nProduct Details\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        name = context.get('name', UNDEFINED)
        shirtColor = context.get('shirtColor', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        variations = context.get('variations', UNDEFINED)
        self = context.get('self', UNDEFINED)
        price = context.get('price', UNDEFINED)
        decorColor = context.get('decorColor', UNDEFINED)
        def site_content():
            return render_site_content(context)
        imageurl = context.get('imageurl', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <table>\r\n        <tr>\r\n            <td width="38%">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(imageurl))
        __M_writer('" class="prodimgmain">\r\n            </td>\r\n            <td width="55%">\r\n               <div class="prodinfo">\r\n                   <p class="prodtitle">\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name.capitalize()))
        __M_writer(' T-Shirt\r\n                        \r\n\r\n                   </p>\r\n                    <p class="prodcolor">\r\n')
        if shirtColor != decorColor:
            __M_writer('                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(shirtColor))
            __M_writer(' / ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(decorColor))
            __M_writer('\r\n')
        else:
            __M_writer('                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(shirtColor))
            __M_writer('\r\n')
        __M_writer('\r\n                        <span class="prodprice">\r\n                                $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(price))
        __M_writer('\r\n                        </span>\r\n\r\n\r\n                    </p>\r\n                    <p class="proddesc">\r\n                            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(desc))
        __M_writer('\r\n                    </p>\r\n                   <p class="variationTitle">Other Styles:</p>\r\n                   <div class="options">\r\n')
        for var in variations:
            __M_writer('                       <input type="checkbox" class="hide" id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(var.id))
            __M_writer('">\r\n                       <a id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(var.name))
            __M_writer('-')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(var.id))
            __M_writer('" href="/store/product/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(var.id))
            __M_writer('"class="optionButton"><img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(var.image_url()))
            __M_writer('""></a>\r\n')
        __M_writer('                   </div>\r\n                   <a class="mybtn" href="/store/index/1/">Back to products</a>\r\n               </div>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<script>\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/store/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 6, "60": 10, "65": 58, "70": 63, "76": 4, "82": 4, "88": 8, "94": 8, "100": 12, "114": 12, "115": 18, "116": 18, "117": 23, "118": 23, "119": 28, "120": 29, "121": 29, "122": 29, "123": 29, "124": 29, "125": 30, "126": 31, "127": 31, "128": 31, "129": 33, "130": 35, "131": 35, "132": 41, "133": 41, "134": 45, "135": 46, "136": 46, "137": 46, "138": 47, "139": 47, "140": 47, "141": 47, "142": 47, "143": 47, "144": 47, "145": 47, "146": 49, "152": 60, "158": 60, "164": 158}}
__M_END_METADATA
"""
