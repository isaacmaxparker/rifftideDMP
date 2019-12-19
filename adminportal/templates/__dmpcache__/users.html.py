# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576740485.3134532
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/users.html'
_template_uri = 'users.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'page_title', 'left_content', 'site_content', 'right_content']


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
        request = context.get('request', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nAdmin Portal\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Users')
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
        users = context.get('users', UNDEFINED)
        def site_content():
            return render_site_content(context)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n<div style="text-align: center; font-family: Josefin Sans, Century Gothic, Helvetica; font-size: 34px;">\r\n    <p class="homeparg" style="text-align: center; font-weight:bold;font-family:Century Gothic, Helvetica; font-size: 34px;">Welcome Isa')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name))
        __M_writer('!</p>\r\n</div>\r\n<table style="font-family: Josefin Sans, Century Gothic, Helvetica; Font-size: 24px; width:100%; text-align: center;">\r\n    <tr>\r\n        <th>\r\n            First Name\r\n        </th>\r\n        <th>\r\n            Last Name\r\n        </th>\r\n        <th>\r\n            Username\r\n        </th>\r\n        <th>\r\n            Voice Part\r\n        </th>\r\n        <th>\r\n            Actions\r\n        </th>\r\n    </tr>\r\n')
        for user in users:
            __M_writer('    <tr>\r\n      <td>\r\n        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.first_name))
            __M_writer('\r\n      </td>\r\n      <td>\r\n        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.last_name))
            __M_writer('\r\n      </td>\r\n      <td>\r\n        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.username))
            __M_writer('\r\n      </td>\r\n      <td>\r\n        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(user.voicepart))
            __M_writer('\r\n      </td>    \r\n      <td>\r\n        <a>Change Password</a>\r\n        <a>Delete</a>\r\n        <a href="/adminportal/editUser/">Edit</a>\r\n      </td>            \r\n    </tr>\r\n')
        __M_writer('</table>\r\n</div>\r\n\r\n')
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
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/users.html", "uri": "users.html", "source_encoding": "utf-8", "line_map": {"29": 0, "47": 1, "52": 5, "57": 7, "62": 11, "67": 61, "77": 3, "83": 3, "89": 7, "95": 7, "101": 9, "107": 9, "113": 14, "122": 14, "123": 17, "124": 17, "125": 37, "126": 38, "127": 40, "128": 40, "129": 43, "130": 43, "131": 46, "132": 46, "133": 49, "134": 49, "135": 58, "141": 63, "147": 63, "153": 147}}
__M_END_METADATA
"""
