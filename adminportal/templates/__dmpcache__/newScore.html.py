# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576743758.5728552
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/adminportal/templates/newScore.html'
_template_uri = 'newScore.html'
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
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nNew Score\r\n')
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
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n<form method="POST" id="editScoreForm">\r\n\r\n                    <table style="font-family: Josefin Sans, Century Gothic, Helvetica; Font-size: 24px; width:100%; text-align: center; display: inline-block;">\r\n                            <tr>\r\n                                    <td>Score Name:</td>\r\n                               \r\n                                        <td><input type="text" name="scoreName" class="forminput" value="" width=100%></td>\r\n                               \r\n                                            <td>All Part URL</td>\r\n                         \r\n                                            <td><input type="text" name="allURL" class="forminput" value="" width=100%></td>\r\n                 \r\n                                       <td width="100px" style="text-align: center;"> <input type="submit" class="btn savebtn mybtn" style="display: inline-block;" value="Save"/></td>\r\n                                </tr>\r\n                            <tr>\r\n                              <td>\r\n                                Soprano\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL0" class="forminput" value="" width=90%>\r\n                              </td>  \r\n                              <td>\r\n                                Mezzo\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL1" class="forminput" value="" width=90%>\r\n                              </td>\r\n                            </tr>\r\n                            <tr>       \r\n                              <td>\r\n                                Alto\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL2" class="forminput" value="" width=90%>\r\n                              </td>  \r\n                              <td>\r\n                                Contralto\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL3" class="forminput" value="" width=90%>\r\n                              </td>      \r\n                            </tr>\r\n                            <tr>\r\n                              <td>\r\n                                Tenor\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL4" class="forminput" value="" width=90%>\r\n                              </td>  \r\n                              <td>\r\n                                Baritone\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL5" class="forminput" value="" width=90%>\r\n                              </td>\r\n                            </tr><tr>       \r\n                              <td>\r\n                                Bass\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL6" class="forminput" value="" width=90%>\r\n                              </td>  \r\n                              <td>\r\n                                Beatbox\r\n                              </td> \r\n                              <td>\r\n                                <input type="text" name="partURL7" class="forminput" value="" width=90%>\r\n                              </td>      \r\n                            </tr>\r\n\r\n                        </table>\r\n\r\n\r\n\r\n</form>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/adminportal/templates/newScore.html", "uri": "newScore.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 5, "50": 7, "55": 88, "61": 3, "67": 3, "73": 7, "79": 7, "85": 9, "91": 9, "97": 91}}
__M_END_METADATA
"""
