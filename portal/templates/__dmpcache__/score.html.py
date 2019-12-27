# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1577485237.5227928
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/portal/templates/score.html'
_template_uri = 'score.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        Url = context.get('Url', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        Url = context.get('Url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n            <iframe src="https://flat.io/embed/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(Url))
        __M_writer('?layout=track&branding=false&controlsPrint=false&controlsPosition=top&themeIconsPrimary=%23000000&themeControlsBackground=%23000000&themeSlider=%2312fccd&themeCursorV0=%2355fbda&sharingKey=164bcd1f4d8c50336b4e96d38ff26bb5a8c851970bada3baa25857b0184d2a051a6c11e5d9b42d074ba50f0838632d1aca23caab542e19a2e6aacba2f5b4b00e" width="100%" height="1000vh" frameBorder="0" allowfullscreen allow="midi"></iframe>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/portal/templates/score.html", "uri": "score.html", "source_encoding": "utf-8", "line_map": {"18": 0, "36": 1, "44": 1, "45": 2, "46": 2, "52": 46}}
__M_END_METADATA
"""
