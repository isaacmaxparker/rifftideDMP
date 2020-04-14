# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1586840461.5409486
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/homepage/templates/cards.html'
_template_uri = 'cards.html'
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
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
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
        __M_writer('&mdash; Cards')
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
        __M_writer('homepage/styles/cards.css">\r\n<link rel="stylesheet" media="(max-width:1375px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/cards-mobile.css">\r\n<script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/cards.js"></script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="cardsContent">\r\n    <div id="loadingScreen">\r\n        <img src="https://storage.googleapis.com/rifftidesite-static/images/loaders/clearLoadFlower.gif" alt="loading GIF">\r\n    </div>\r\n    <div id="cards">\r\n      <div id="filtersDiv">\r\n            <div id="filters">\r\n              <div id="sortby">\r\n              </div>\r\n              \r\n            </div>\r\n            <div id="filtersTab" >\r\n              <p><span id="memberFilter" onclick="toggleFilters()"><span class="icon">p</span> Member</span> | <span id="eventFilter"><span class="icon">x</span> Event</span> | <span id="inactiveFilter" onclick="showInactives()"><span id="inactiveIcon" class=icon>S</span> Inactives</span>  </p>\r\n          </div>\r\n      </div>\r\n        <div id="cardLists">\r\n        </div>\r\n    </div>\r\n    <div id="cardPopUp">\r\n        <p class="closeSlider icon" onclick="closeModal()">*</p>\r\n        <div id="cardsScroller" >\r\n            <div class="sliderContainer">\r\n                <div id="cardSlider">\r\n\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div class="widthGetter">\r\n        <div id="cardsScroller">\r\n            <div class="sliderContainer">\r\n                <div id="cardSlider2" style="transform: translate3d(581.435px, 0px, 0px); width: 9032px;">\r\n\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_scripts():
            return render_page_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <script type="text/javascript">\r\n        //let showLocation;\r\n        function ready(fn) {\r\n            if (document.readyState != \'loading\') {\r\n                fn();\r\n            } else {\r\n                document.addEventListener(\'DOMContentLoaded\', fn);\r\n            }\r\n        }\r\n\r\n        ready(function () {\r\n          Global.init();\r\n          Cards.init();\r\n          prev = Cards.prev\r\n          next = Cards.next\r\n          showCards = Cards.showCards\r\n          showCardPopup = Cards.showCardPopup\r\n          imgLoaded = Cards.imgLoaded\r\n          switchCards = Cards.switchCards\r\n          closeModal = Cards.closeModal\r\n          toggleFilters = Cards.toggleFilters\r\n          showInactives = Cards.showInactive\r\n    });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/homepage/templates/cards.html", "uri": "cards.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 3, "54": 10, "59": 51, "69": 3, "75": 3, "81": 5, "89": 5, "90": 7, "91": 7, "92": 8, "93": 8, "94": 9, "95": 9, "101": 12, "107": 12, "113": 53, "119": 53, "125": 119}}
__M_END_METADATA
"""
