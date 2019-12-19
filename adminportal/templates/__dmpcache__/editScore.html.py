# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576742661.515702
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/editScore.html'
_template_uri = 'editScore.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'page_title', 'site_content']


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
        scores = context.get('scores', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        scores = context.get('scores', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(scores[0].name))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Scores')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        scores = context.get('scores', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n<form method="POST" id="editScoreForm">\r\n    <table width="100%">\r\n        <tr>\r\n            <td>\r\n                    <table style="font-family: Josefin Sans, Century Gothic, Helvetica; Font-size: 24px; width:50%; text-align: center; display: inline-block;">\r\n')
        for score in scores:
            __M_writer('                            <tr>\r\n                              <td>\r\n                                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.part))
            __M_writer('\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.id))
            __M_writer('" class="forminput" value="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(score.partURL))
            __M_writer('" width=90%>\r\n                              </td>            \r\n                            </tr>\r\n')
        __M_writer('                        </table>\r\n            </td>\r\n            <td>\r\n                    <table style="font-family: Josefin Sans, Century Gothic, Helvetica; Font-size: 24px; width:100%; text-align: center; display: inline-block;">\r\n                        <tr>\r\n                            <td>Score Name:</td>\r\n                        </tr>    \r\n                        <tr>\r\n                                <td><input type="text" name="scoreName" class="forminput" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(scores[0].name))
        __M_writer('" width=100%></td>\r\n                        </tr>\r\n                        <tr>\r\n                                    <td>All Part URL</td>\r\n                        </tr>\r\n                        <tr>\r\n                                    <td><input type="text" name="allURL" class="forminput" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(scores[0].allURL))
        __M_writer('" width=100%></td>\r\n                        </tr>\r\n                        <tr>\r\n                               <td> <input type="submit" class="btn  mybtn" value="Save"/></td>\r\n                        </tr>\r\n                    </table>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n\r\n\r\n</form>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/editScore.html", "uri": "editScore.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 5, "52": 7, "57": 54, "63": 3, "71": 3, "72": 4, "73": 4, "79": 7, "85": 7, "91": 9, "99": 9, "100": 16, "101": 17, "102": 19, "103": 19, "104": 22, "105": 22, "106": 22, "107": 22, "108": 26, "109": 34, "110": 34, "111": 40, "112": 40, "118": 112}}
__M_END_METADATA
"""
