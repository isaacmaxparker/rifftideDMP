# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1586814987.4442167
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_content', 'page_scripts']


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
        self = context.get('self', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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
        __M_writer('&mdash; Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def page_content():
            return render_page_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="homeContent">\r\n  <div class="slide" id="slide1">\r\n      <div class="imgDiv" id="imgDiv1">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/Jumpin.jpg">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv1">\r\n          <div>\r\n              <p id="p1">\r\n                  <span id="we">We</span> <span id="are">Are</span><br><span class="splitter"><br></span><span id="rifftide"><span id="riff">Riff</span><span class="splitter"></span><span id="tide">tide</span></span>\r\n              </p>\r\n          </div>\r\n          <p id="down1" class="icon homeIcon bottom">\r\n              <span onclick="scrollToDiv(\'slide2\')" onmouseover="hoverOn(\'down1\')" onmouseout="hoverOff(\'down1\')">#</span>\r\n          </p>\r\n      </div>\r\n  </div>\r\n  <div class="slide" id="slide2">\r\n      <div class="imgDiv" id="imgDiv2">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/Facebook Header.png">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv2">\r\n          <p id="up2" class="icon homeIcon top">\r\n              <span onclick="scrollToDiv(\'slide1\')" onmouseover="hoverOn(\'up2\')" onmouseout="hoverOff(\'up2\')">%</span>\r\n          </p>\r\n          <div>\r\n              <p class="homeTitle">\r\n                  Meet the Members\r\n              </p>\r\n              <p class="homeSubtitle">\r\n                  View <a>member profiles</a> or browse <a>member cards</a>\r\n              </p>\r\n          </div>\r\n          <p id="down2"class="icon homeIcon bottom">\r\n              <span onclick="scrollToDiv(\'slide3\')" onmouseover="hoverOn(\'down2\')" onmouseout="hoverOff(\'down2\')">#</span>\r\n          </p>\r\n      </div>\r\n  </div>\r\n  <div class="slide" id="slide3">\r\n      <div class="imgDiv" id="imgDiv3">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/T-shirt banner.png">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv3" >\r\n          <p id="up3" class="icon homeIcon top">\r\n              <span onclick="scrollToDiv(\'slide2\')" onmouseover="hoverOn(\'up3\')" onmouseout="hoverOff(\'up3\')">%</span>\r\n          </p>\r\n              <div>\r\n                  <p class="homeTitle">\r\n                      Support Our Music\r\n                  </p>\r\n                  <p class="homeSubtitle">\r\n                      Check out our <a>Merch</a> or <a>Donate</a> through patreon!\r\n                  </p>\r\n              </div>\r\n          <p id="down3" class="icon homeIcon bottom">\r\n              <span onclick="scrollToDiv(\'slide4\')" onmouseover="hoverOn(\'down3\')" onmouseout="hoverOff(\'down3\')">#</span>\r\n          </p>\r\n      </div>\r\n  </div>\r\n  <div class="slide" id="slide4">\r\n      <div class="imgDiv" id="imgDiv4">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/V.gif">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv4" >\r\n          <p id="up4" class="icon homeIcon top">\r\n              <span onclick="scrollToDiv(\'slide3\')" onmouseover="hoverOn(\'up4\')" onmouseout="hoverOff(\'up4\')">%</span>\r\n          </p>\r\n              <div>\r\n                  <p class="homeTitle">\r\n                      Watch Our Videos\r\n                  </p>\r\n                  <p class="homeSubtitle">\r\n                      Check out our <a>Music Videos</a> on <a>Youtube</a>\r\n                  </p>\r\n              </div>\r\n          <p id="down4" class="icon homeIcon bottom">\r\n              <span onclick="scrollToDiv(\'slide5\')" onmouseover="hoverOn(\'down4\')" onmouseout="hoverOff(\'down4\')">#</span>\r\n          </p>\r\n      </div>\r\n  </div>      \r\n  <div class="slide" id="slide5">\r\n      <div class="imgDiv" id="imgDiv5">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/comparison.png">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv5" >\r\n          <p id="up5" class="icon homeIcon top">\r\n              <span onclick="scrollToDiv(\'slide4\')" onmouseover="hoverOn(\'up5\')" onmouseout="hoverOff(\'up5\')">%</span>\r\n          </p>\r\n              <div>\r\n                  <p class="homeTitle">\r\n                      Stream Our Music\r\n                  </p>\r\n                  <p class="homeSubtitle">\r\n                      Stream our songs on <a>Spotify</a>,<a>iTunes</a>,<a>Apple Music</a>,<a>AmazonMusic</a>, and <a>More!</a>\r\n                  </p>\r\n              </div>\r\n          <p id="down5" class="icon homeIcon bottom">\r\n              <span onclick="scrollToDiv(\'slide6\')" onmouseover="hoverOn(\'down5\')" onmouseout="hoverOff(\'down5\')">#</span>\r\n          </p>\r\n      </div>\r\n  </div>\r\n  <div class="slide" id="slide6">\r\n      <div class="imgDiv" id="imgDiv6">\r\n          <div class="blackCover"></div>\r\n          <img class="homeSlideImage" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.IMAGE_URL ))
        __M_writer('backgrounds/contactback.jpg">\r\n      </div>\r\n      <div class="slidediv center" id="slidediv6" >\r\n          <p id="up6" class="icon homeIcon top">\r\n              <span onclick="scrollToDiv(\'slide5\')" onmouseover="hoverOn(\'up6\')" onmouseout="hoverOff(\'up6\')">%</span>\r\n          </p>\r\n              <div>\r\n                  <p class="homeTitle">\r\n                      Contact Us\r\n                  </p>\r\n                  <p class="homeSubtitle">\r\n                      <a>Contact us</a> for <a>Bookings</a>, <a>Collaborations</a>, or anything else!\r\n                  </p>\r\n              </div>\r\n          <p class="bottom">\r\n\r\n          </p>\r\n      </div>\r\n  </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_scripts():
            return render_page_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n<script type="text/javascript">\r\n  //let showLocation;\r\n  function ready(fn) {\r\n      if (document.readyState != \'loading\') {\r\n          fn();\r\n      } else {\r\n          document.addEventListener(\'DOMContentLoaded\', fn);\r\n      }\r\n  }\r\n\r\n  ready(function () {\r\n      Global.init();\r\n      Home.init();\r\n      scrollToDiv = Home.scrollToDiv\r\n      hoverOn = Global.hoverOn\r\n      hoverOff = Global.hoverOff\r\n  });\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "52": 134, "62": 3, "68": 3, "74": 5, "82": 5, "83": 10, "84": 10, "85": 26, "86": 26, "87": 48, "88": 48, "89": 70, "90": 70, "91": 92, "92": 92, "93": 114, "94": 114, "100": 136, "106": 136, "112": 106}}
__M_END_METADATA
"""
