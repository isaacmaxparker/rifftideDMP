# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576730266.3454218
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/portal/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodclass', 'page_header_title', 'left_content', 'site_content', 'right_content']


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
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        Scores = context.get('Scores', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Portal')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\nclass="back2"\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nScores\r\n')
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
        Scores = context.get('Scores', UNDEFINED)
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n<table class="scoreTable">\r\n')
        for score in Scores:
            __M_writer('    <tr class="scoreTableRow ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'darkRow' if score.id % 2 == 0 else ''))
            __M_writer('">\r\n        <td class="scoreTableName">\r\n            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.name))
            __M_writer('\r\n        </td>\r\n        <td class="scoreTableLinks" >\r\n            <a class="scoreTablePart" href="/portal/score/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
            __M_writer('/1">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.part))
            __M_writer('</a>\r\n            <a class="scoreTableAll" href="/portal/score/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
            __M_writer('/0">All Parts</a>\r\n        </td>\r\n    </tr>\r\n')
        __M_writer('</table>\r\n     \r\n      </div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/portal/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "48": 1, "53": 3, "58": 8, "63": 12, "68": 16, "73": 36, "83": 3, "89": 3, "95": 6, "101": 6, "107": 10, "113": 10, "119": 14, "125": 14, "131": 19, "139": 19, "140": 22, "141": 23, "142": 23, "143": 23, "144": 25, "145": 25, "146": 28, "147": 28, "148": 28, "149": 28, "150": 29, "151": 29, "152": 33, "158": 38, "164": 38, "170": 164}}
__M_END_METADATA
"""
