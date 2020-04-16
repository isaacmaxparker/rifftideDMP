# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1587009360.4796414
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/resources/templates/resources.html'
_template_uri = 'resources.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_links', 'page_content', 'page_scripts']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        def page_links():
            return render_page_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_links'):
            context['self'].page_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_content'):
            context['self'].page_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_scripts'):
            context['self'].page_scripts(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Resources')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_links():
            return render_page_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/resources.css">\r\n<link rel="stylesheet" media="(max-width:1240px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/resources-mobile.css">\r\n<link rel="stylesheet" media="(min-width:2140px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/resources-large.css">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        def page_content():
            return render_page_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="resourcesContent">\r\n    <div id="imgDiv">\r\n        <img id=\'backgroundImage\' src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/tealmembers.png">\r\n    </div>\r\n    <div id="resourcesGrid">\r\n        <div id="resourcesTitle">\r\n            Resources\r\n        </div>\r\n        <hr>\r\n        <div id="resourceListContainer">\r\n            <div id="resourcesList">\r\n                <div class="resource" style="margin-top:3vh;">\r\n                    <div class="resourceName">\r\n                        <a href="/404/">Vocal Warm-Ups</a>\r\n                    </div>\r\n                    <div class="resourceDetails">\r\n                        Generate random exercises to warm up your voice\r\n                    </div>\r\n                </div>\r\n                <div class="resource">\r\n                    <div class="resourceName">\r\n                        <a href="/resources/music/">Discography</a>\r\n                    </div>\r\n                    <div class="resourceDetails">\r\n                        View information about the group\'s songs.\r\n                    </div>\r\n                </div>\r\n                <div class="resource">\r\n                    <div class="resourceName">\r\n                        <a href="/resources/videos/">Music Videos</a>\r\n                    </div>\r\n                    <div class="resourceDetails">\r\n                        View information about the group\'s music videos\r\n                    </div>\r\n                </div>\r\n                <div class="resource" style="margin-bottom:6vh;">\r\n                    <div class="resourceName">\r\n                        <a href="https://www.patreon.com/rifftide" target="blank">Patreon</a>\r\n                    </div>\r\n                    <div class="resourceDetails">\r\n                        Help support Rifftide on Patreon!\r\n                    </div>\r\n                </div>\r\n                <div class="resource" style="margin-bottom:6vh;">\r\n                    <div class="resourceName">\r\n                        <a href="https://www.youtube.com/channel/UCKG2CQdai0C7qsRT21Lx8mw" target="blank">Riffclips</a>\r\n                    </div>\r\n                    <div class="resourceDetails">\r\n                        Check out Rifftide\'s bonus content on our secondary channel.\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_scripts():
            return render_page_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <script type="text/javascript">\r\n        //let showLocation;\r\n        function ready(fn) {\r\n            if (document.readyState != \'loading\') {\r\n                fn();\r\n            } else {\r\n                document.addEventListener(\'DOMContentLoaded\', fn);\r\n            }\r\n        }\r\n\r\n        ready(function () {\r\n            Global.init();\r\n            scrollToDiv = Global.scrollToDiv\r\n        });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/resources/templates/resources.html", "uri": "resources.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 3, "55": 10, "60": 68, "70": 3, "76": 3, "82": 5, "90": 5, "91": 7, "92": 7, "93": 8, "94": 8, "95": 9, "96": 9, "102": 12, "110": 12, "111": 15, "112": 15, "118": 70, "124": 70, "130": 124}}
__M_END_METADATA
"""
