# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576743691.496142
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['BodyBackImage', 'head', 'left_content', 'right_content']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def BodyBackImage():
            return render_BodyBackImage(context._locals(__M_locals))
        def head():
            return render_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'BodyBackImage'):
            context['self'].BodyBackImage(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
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


def render_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        __M_writer = context.writer()
        __M_writer("\r\n<style>\r\n.backlink{\r\n    color:rgb(138, 138, 138);\r\n    font-family: 'Century Gothic','Arial','Sans-Serif';\r\n    margin-bottom:100px;\r\n}\r\n.savebtn{\r\n    background-color: rgba(37, 148, 37, 0.795);\r\n    color:white;\r\n    padding:20px;\r\n}\r\n\r\n.scoreTable{\r\n    width:100%;\r\n    /* border:solid 10px lightgrey; */\r\n\r\n    padding:20px;\r\n    font-family:  'Century Gothic','Arial','Sans-Serif';\r\n}\r\n\r\n.darkRow{\r\n    background-color:rgba(211, 211, 211, 0.462);\r\n}\r\n\r\n.scoreTableRow{\r\n    padding:10px;\r\n}\r\n\r\n.scoreTableName{\r\n    color:black;\r\n    font-weight: bold;\r\n    font-size:26px;\r\n}\r\n\r\n.scoreTablePart{\r\n    color:rgba(0, 0, 0, 0.76);\r\n    font-style: italic;\r\n    font-size: 24px;\r\n    text-align: left;\r\n}\r\n\r\n.scoreTableLinks{\r\n    width:40%;\r\n}\r\n\r\n.scoreTableAll{\r\n    color:rgb(6, 116, 106);\r\n    font-weight: bold;\r\n    float:right;\r\n    font-size: 24px;\r\n}\r\n\r\n</style>\r\n")
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


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 12, "52": 68, "57": 72, "62": 77, "68": 3, "74": 3, "80": 14, "86": 14, "92": 70, "98": 70, "104": 74, "110": 74, "116": 110}}
__M_END_METADATA
"""
