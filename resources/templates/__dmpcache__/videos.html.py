# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1587013477.8546722
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/resources/templates/videos.html'
_template_uri = 'videos.html'
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
        self = context.get('self', UNDEFINED)
        def page_content():
            return render_page_content(context._locals(__M_locals))
        settings = context.get('settings', UNDEFINED)
        def page_links():
            return render_page_links(context._locals(__M_locals))
        def page_scripts():
            return render_page_scripts(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('&mdash; videos')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def page_links():
            return render_page_links(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/videos.css">\r\n<link rel="stylesheet" media="(max-width:1240px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/videos-mobile.css">\r\n<script>\r\n    fadeIn = function(element,opacity=1,addtnl=0){\r\n    $(element).animate({\'opacity\':opacity},800)\r\n    if (addtnl !== 0){\r\n    $(addtnl).animate({\'opacity\':opacity},800)\r\n    }\r\n  }\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_content():
            return render_page_content(context)
        settings = context.get('settings', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="videosContent">\r\n    <div id="videosList">\r\n        <div class="video">\r\n            <div class="videoImgDiv">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/kywmback.jpg" onload="fadeIn(this,.4)">\r\n            </div>\r\n            <div class="videoInfo">\r\n                <div class="videoSource">\r\n                    <iframe onload="fadeIn(this,1,this.parentElement.parentElement.children[1])" class="youtubeVideo" src="https://www.youtube.com/embed/videoseries?list=PLJaVJrQa31zNG6P_6ltV3y-CJ6qUtgn0U&autoplay=1&mute=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n                </div>\r\n                <div class="videoTextContainer" >\r\n                    <div class="videoText" onload="fadeIn(this)">\r\n                        <div class="videoTitle">\r\n\r\n                                <div class="videoName">\r\n                                    Keep You With Me\r\n                                </div>\r\n                                <div class="videoYear">\r\n                                    2020\r\n                                </div>\r\n                        </div>\r\n                        <div class="videoBio">\r\n                            Keep You With Me was the first original song released by the group. The video is set years into the future, and follows each member as they\'ve moved on and participate in various activies.\r\n                            Each member finds a mysterious envelope which leads them to a communal meeting spot in the end.\r\n                        </div>\r\n                        <div class="videoCredits">\r\n                            <b>Song by</b>: Isaac McDougal, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Filmed by</b>: Josh Sales, \r\n                            <b>Edited by</b>: Isaac McDougal,\r\n                            <b>Costumes by</b>: Rifftide,<br>\r\n                            <b>Script by</b>: Isaac McDougal, Sam Hepworth, Laurel Scott.\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="video">\r\n            <div class="videoImgDiv dark">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/hocback.jpg" onload="fadeIn(this,.4)">\r\n            </div>\r\n            <div class="videoInfo flipped">\r\n                <div class="videoSource">\r\n                    <iframe onload="fadeIn(this,1,this.parentElement.parentElement.children[1])" class="youtubeVideo" src="https://www.youtube.com/embed/videoseries?list=PLJaVJrQa31zMLN9vecpvFYdNunXJWN5Kd" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n                </div>\r\n                <div class="videoTextContainer">\r\n                    <div class="videoText">\r\n                        <div class="videoTitle">\r\n\r\n                                <div class="videoName">\r\n                                    Hymn of Christmas\r\n                                </div>\r\n                                <div class="videoYear">\r\n                                    2019\r\n                                </div>\r\n                        </div>\r\n                        <div class="videoBio">\r\n                           Hymn of Christmas is the largest scale project Rifftide has done to date. The song was a mashup of 7 well known Christmas carols and \r\n                           featured 13 local artists! The video follows a one-shot style showcasing all of the collaborators.\r\n                        </div>\r\n                        <div class="videoCredits">\r\n                            <b>Song by</b>: Isaac McDougal and Sam Hepworth,\r\n                            <b>Produced By</b>: JustNick,\r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Filmed and Edited by</b>: Brandon Young,\r\n                            <b>Script by</b>: Isaac McDougal,Sam Hepworth, Bri Ellis.\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="video">\r\n            <div class="videoImgDiv">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/justdanceback.jpeg" onload="fadeIn(this,.4)">\r\n            </div>\r\n            <div class="videoInfo">\r\n                <div class="videoSource">\r\n                    <iframe onload="fadeIn(this,1,this.parentElement.parentElement.children[1])" class="youtubeVideo" src="https://www.youtube.com/embed/RP2v7NnYGmg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n                </div>\r\n                <div class="videoTextContainer">\r\n                    <div class="videoText">\r\n                        <div class="videoTitle">\r\n\r\n                                <div class="videoName">\r\n                                    Just Evacuate\r\n                                </div>\r\n                                <div class="videoYear">\r\n                                    2019\r\n                                </div>\r\n                        </div>\r\n                        <div class="videoBio">\r\n                            This song is a mashup of "Just Dance" by Lady Gaga and "Evacuate the Dancefloor" by Cascada. The video takes place in a footloose-style town where\r\n                            dancing is not allowed. It shows each Rifftide member as two characters, an office employee in the town, and a technocolored visitor from the future \r\n                            who travels back in time to show the office people how to dance. \r\n                        </div>\r\n                        <div class="videoCredits">\r\n                            <b>Arranged by</b>: Isaac McDougal, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Filmed by</b>: Tyler Edwards,\r\n                            <b>Edited by</b>: Isaac McDougal,\r\n                            <b>Costumes by</b>: Rifftide,<br>\r\n                            <b>Script by</b>: Isaac McDougal, Emily Grether.\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="video">\r\n            <div class="videoImgDiv dark">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/dreamback.jpeg" onload="fadeIn(this,.4)">\r\n            </div>\r\n            <div class="videoInfo flipped">\r\n                <div class="videoSource">\r\n                    <iframe onload="fadeIn(this,1,this.parentElement.parentElement.children[1])" class="youtubeVideo" src="https://www.youtube.com/embed/videoseries?list=PLJaVJrQa31zMAlXuG341gdQe3s9zRgaWm" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n                </div>\r\n                <div class="videoTextContainer">\r\n                    <div class="videoText">\r\n                        <div class="videoTitle">\r\n\r\n                                <div class="videoName">\r\n                                    Dream\r\n                                </div>\r\n                                <div class="videoYear">\r\n                                    2019\r\n                                </div>\r\n                        </div>\r\n                        <div class="videoBio">\r\n                            Dream was the first large scale music video Rifftide took on. The video is set far in a post-apocalyptic wasteland. The 8 members have formed a small clan and the video follows them as they \r\n                            travel around trying to survive. Halfway they are separated, but they are able to rejoin using smoke bombs as flares for one last standoff. It ends with a twist!\r\n                        </div>\r\n                        <div class="videoCredits">\r\n                            <b>Song by</b>: Imagine Dragons, \r\n                            <b>Arranged by</b>: Emily Grether, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Filmed and Edited by</b>: Tyler Edwards, \r\n                            <b>Costumes by</b>: Rifftide,<br>\r\n                            <b>Script by</b>: Isaac McDougal, Emily Grether, Bri Ellis.\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="video">\r\n            <div class="videoImgDiv">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/singback.png" onload="fadeIn(this,.4)">\r\n            </div>\r\n            <div class="videoInfo">\r\n                <div class="videoSource">\r\n                    <iframe onload="fadeIn(this,1,this.parentElement.parentElement.children[1])" class="youtubeVideo" src="https://www.youtube.com/embed/7dsw2vkYSoU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n                </div>\r\n                <div class="videoTextContainer">\r\n                    <div class="videoText">\r\n                        <div class="videoTitle">\r\n\r\n                                <div class="videoName">\r\n                                    Sing!\r\n                                </div>\r\n                                <div class="videoYear">\r\n                                    2017\r\n                                </div>\r\n                        </div>\r\n                        <div class="videoBio">\r\n                            Sing! was the debut music video for Rifftide. The video shows each member in a Brady Bunch Intro style rainbox box performing the song. \r\n                        </div>\r\n                        <div class="videoCredits">\r\n                            <b>Song by</b>: Pentatonix, \r\n                            <b>Arranged by</b>: Scott Shattuck,\r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Filmed and Edited by</b>: Isaac McDougal.\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_scripts(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_scripts():
            return render_page_scripts(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <script type="text/javascript">\r\n        //let showLocation;\r\n        function ready(fn) {\r\n            if (document.readyState != \'loading\') {\r\n                fn();\r\n            } else {\r\n                document.addEventListener(\'DOMContentLoaded\', fn);\r\n            }\r\n        }\r\n\r\n        ready(function () {\r\n            Global.init();\r\n            fadeIn = Global.fadeIn\r\n            scrollToDiv = Global.scrollToDiv\r\n        });\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/resources/templates/videos.html", "uri": "videos.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 3, "55": 17, "60": 196, "70": 3, "76": 3, "82": 5, "90": 5, "91": 7, "92": 7, "93": 8, "94": 8, "100": 19, "108": 19, "109": 24, "110": 24, "111": 59, "112": 59, "113": 93, "114": 93, "115": 129, "116": 129, "117": 164, "118": 164, "124": 198, "130": 198, "136": 130}}
__M_END_METADATA
"""
