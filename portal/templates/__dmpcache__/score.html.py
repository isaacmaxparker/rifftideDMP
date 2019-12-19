# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1576730335.4330575
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/portal/templates/score.html'
_template_uri = 'score.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'navbar_items', 'bodclass', 'page_header_title', 'left_content', 'site_content', 'right_content']


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
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        Url = context.get('Url', UNDEFINED)
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
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


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n<li class="nav-item mynav-item">\r\n<a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
        __M_writer('"  href="/store/">Store</a>\r\n</li>     \r\n<li class="nav-item mynav-item">\r\n        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
        __M_writer('"  href="/portal/">Scores</a>\r\n</li>            \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\ngs://rifftidesite-content/tealsparkle.png\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(title))
        __M_writer('\r\n')
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
        Url = context.get('Url', UNDEFINED)
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <iframe src="https://flat.io/embed/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(Url))
        __M_writer('?layout=track&branding=false&controlsPrint=false&controlsPosition=top&themeIconsPrimary=%23000000&themeControlsBackground=%23000000&themeSlider=%2312fccd&themeCursorV0=%2355fbda&sharingKey=164bcd1f4d8c50336b4e96d38ff26bb5a8c851970bada3baa25857b0184d2a051a6c11e5d9b42d074ba50f0838632d1aca23caab542e19a2e6aacba2f5b4b00e" width="100%" height="1000vh" frameBorder="0" allowfullscreen allow="midi"></iframe>\r\n            <a class="backlink" href="/portal/">Back to scores</a>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/portal/templates/score.html", "uri": "score.html", "source_encoding": "utf-8", "line_map": {"29": 0, "52": 1, "57": 3, "62": 12, "67": 16, "72": 20, "77": 24, "82": 30, "92": 3, "98": 3, "104": 5, "112": 5, "113": 7, "114": 7, "115": 10, "116": 10, "122": 14, "128": 14, "134": 18, "142": 18, "143": 19, "144": 19, "150": 22, "156": 22, "162": 27, "170": 27, "171": 28, "172": 28, "178": 32, "184": 32, "190": 184}}
__M_END_METADATA
"""
