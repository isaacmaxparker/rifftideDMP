# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1569544753.895631
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
        def right_content():
            return render_right_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        shirtColor = context.get('shirtColor', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        imageurl = context.get('imageurl', UNDEFINED)
        variations = context.get('variations', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        price = context.get('price', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        name = context.get('name', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        cut = context.get('cut', UNDEFINED)
        message = context.get('message', UNDEFINED)
        decorColor = context.get('decorColor', UNDEFINED)
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
        __M_writer('\r\n\r\n')
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
        self = context.get('self', UNDEFINED)
        shirtColor = context.get('shirtColor', UNDEFINED)
        imageurl = context.get('imageurl', UNDEFINED)
        variations = context.get('variations', UNDEFINED)
        price = context.get('price', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        name = context.get('name', UNDEFINED)
        def site_content():
            return render_site_content(context)
        cut = context.get('cut', UNDEFINED)
        message = context.get('message', UNDEFINED)
        decorColor = context.get('decorColor', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <table>\r\n        <tr>\r\n            <td width="38%">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(imageurl))
        __M_writer('" class="prodimgmain">\r\n            </td>\r\n            <td width="55%">\r\n               <div class="prodinfo">\r\n                   <p class="prodtitle">\r\n                       ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cut.capitalize()))
        __M_writer('\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name.capitalize()))
        __M_writer(' T-Shirt\r\n                        \r\n\r\n                   </p>\r\n                    <p class="prodcolor">\r\n')
        if shirtColor != decorColor and decorColor != '':
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
        __M_writer('                   </div>\r\n\r\n                   <div class="centerContent">\r\n                       <div>\r\n                   <form style="vertical-align:middle;" method="POST" id="productform">\r\n\r\n                   \r\n                    <label class="formlabel" style="font-size:18px;">Quantity:</label>\r\n                    <input type="number" value="0" class="forminput fismall" step="1" name="QuantOrd">\r\n                    <select name="shirtSize" class="forminput size">\r\n                            <option value="XS">Adult XS</option>\r\n                            <option value="S">Adult Small</option>\r\n                            <option value="M">Adult Medium</option>\r\n                            <option value="L">Adult Large</option>\r\n                            <option value="XL">Adult XL</option>\r\n\r\n                            <option value="YXS">Youth XS</option>\r\n                            <option value="YS">Youth Small</option>\r\n                            <option value="YM">Youth Medium</option>\r\n                            <option value="YL">Youth Large</option>\r\n                            <option value="YXL">Youth XL</option>\r\n                    </select>\r\n                    <input type="submit" class="mybtn buybtn" value="Add to Cart">\r\n')
        if message != '':
            __M_writer('                    <p class = "message" style="text-align: center;">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(message))
            __M_writer('</p>\r\n')
        __M_writer('                   </form>\r\n\r\n\r\n \r\n                </div>\r\n            </div>\r\n            <a class="mybtn" href="/store/index/1/" style="font-size: 16px;">Back to products</a>\r\n               </div>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n\r\n\r\n')
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
{"filename": "C:/Users/Isaac/mysite/store/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "52": 1, "57": 6, "62": 10, "67": 90, "72": 95, "78": 4, "84": 4, "90": 8, "96": 8, "102": 12, "118": 12, "119": 18, "120": 18, "121": 23, "122": 23, "123": 24, "124": 24, "125": 29, "126": 30, "127": 30, "128": 30, "129": 30, "130": 30, "131": 31, "132": 32, "133": 32, "134": 32, "135": 34, "136": 36, "137": 36, "138": 42, "139": 42, "140": 46, "141": 47, "142": 47, "143": 47, "144": 48, "145": 48, "146": 48, "147": 48, "148": 48, "149": 48, "150": 48, "151": 48, "152": 50, "153": 73, "154": 74, "155": 74, "156": 74, "157": 76, "163": 92, "169": 92, "175": 169}}
__M_END_METADATA
"""
