# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1587009264.093163
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/resources/templates/music.html'
_template_uri = 'music.html'
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
        __M_writer('&mdash; music')
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
        __M_writer('resources/styles/music.css">\r\n<link rel="stylesheet" media="(max-width:1240px)" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('resources/styles/music-mobile.css">\r\n')
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
        __M_writer('\r\n<div id="musicsContent">\r\n    <div id="musicsList">\r\n        <div class="music">\r\n            <div class="musicImgDiv">\r\n                <img onload="fadeIn(this,.4)" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/kywmback.jpg">\r\n            </div>\r\n            <div class="musicInfo">\r\n                <div class="musicSource">\r\n                    <a href=""><img onload="fadeIn(this)" class="albumArt" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('resources/kywmAlbumArt.png"></a>\r\n                </div>\r\n                <div class="musicTextContainer">\r\n                    <div class="musicText">\r\n                        <div class="musicTitle">\r\n\r\n                                <div class="musicName">\r\n                                    Keep You With Me\r\n                                </div>\r\n                                <div class="musicYear">\r\n                                    2020\r\n                                </div>\r\n                        </div>\r\n                        <div class="musicBio">\r\n                            Keep You With Me was the first original song released by the group. The song was written by group director Isaac McDougal. The song originally was dedicated\r\n                            to the members of Rifftide as they prepared to end the season, but after the Covid 19 pandemic broke out the group decided to dedicate the song to everyone\r\n                            who wasn\'t able to say goodbye to someone due to the pandemic.\r\n                        </div>\r\n                        <div class="musicCredits">\r\n                            <b>Original Artist</b>: Rifftide, \r\n                            <b>Written and Arranged by</b>: Isaac McDougal, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Album Art by</b>: Isaac McDougal.\r\n                            \r\n                        </div>\r\n                        <div class="listenNow">\r\n                            <div>\r\n                                <p>Listen Now:</p>\r\n                                <a href="" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n                                </a>\r\n                                <a href="" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/itunes.png">\r\n                                </a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="music">\r\n            <div class="musicImgDiv dark">\r\n                <img onload="fadeIn(this,.4)" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/justdanceAlbumArt.png">\r\n            </div>\r\n            <div class="musicInfo flipped">\r\n                <div class="musicSource">\r\n                    <a href=""><img onload="fadeIn(this)" class="albumArt" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('resources/justdanceAlbumArt.png"></a>\r\n                </div>\r\n                <div class="musicTextContainer">\r\n                    <div class="musicText">\r\n                        <div class="musicTitle">\r\n\r\n                                <div class="musicName">\r\n                                    Just Dance / Evacuate the Dancefloor\r\n                                </div>\r\n                                <div class="musicYear">\r\n                                    2019\r\n                                </div>\r\n                        </div>\r\n                        <div class="musicBio">\r\n                            This song is a mashup of Lady Gaga\'s "Just Dance" and Cascada\'s "Evacuate the Dancefloor". The song was originally performed back in the Spring of 2018,\r\n                            but wasn\'t recorded until 2019.\r\n                        </div>\r\n                        <div class="musicCredits">\r\n                            <b>Original Artists</b>: Lady Gaga & Cascada,\r\n                            <b>Arranged by</b>: Isaac McDougal, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Album Art by</b>: Isaac McDougal.\r\n                        </div>\r\n                        <div class="listenNow">\r\n                            <div>\r\n                                <p>Listen Now:</p>\r\n                                <a href="https://open.spotify.com/track/3oLxWFaZNR4BhKNUDE4d8D" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n                                </a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="music">\r\n            <div class="musicImgDiv">\r\n                <img onload="fadeIn(this,.4)" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/dreamAlbumArt.png">\r\n            </div>\r\n            <div class="musicInfo">\r\n                <div class="musicSource">\r\n                    <a href=""><img onload="fadeIn(this)" class="albumArt" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('resources/dreamAlbumArt.png"></a>\r\n                </div>\r\n                <div class="musicTextContainer">\r\n                    <div class="musicText">\r\n                        <div class="musicTitle">\r\n\r\n                                <div class="musicName">\r\n                                    Dream\r\n                                </div>\r\n                                <div class="musicYear">\r\n                                    2019\r\n                                </div>\r\n                        </div>\r\n                        <div class="musicBio">\r\n                            Dream was recorded and released just months after it was chosen and arranged. \r\n                            This was Rifftide\'s first single self-recorded by the group. \r\n                        </div>\r\n                        <div class="musicCredits">\r\n                            <b>Original Artist</b>: Imagine Dragons, \r\n                            <b>Arranged by</b>: Emily Grether \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Album Art by</b>: Isaac McDougal.\r\n                            \r\n                        </div>\r\n                        <div class="listenNow">\r\n                            <div>\r\n                                <p>Listen Now:</p>\r\n                                <a href="https://open.spotify.com/track/1nldk66lxxwRuselDP4Doq" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n                                </a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="music">\r\n            <div class="musicImgDiv dark">\r\n                <img onload="fadeIn(this,.4)" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/moveAlbumArt.jpg">\r\n            </div>\r\n            <div class="musicInfo flipped">\r\n                <div class="musicSource">\r\n                    <a href=""><img onload="fadeIn(this)" class="albumArt" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('resources/moveAlbumArt.jpg"></a>\r\n                </div>\r\n                <div class="musicTextContainer">\r\n                    <div class="musicText">\r\n                        <div class="musicTitle">\r\n\r\n                                <div class="musicName">\r\n                                    Move Along\r\n                                </div>\r\n                                <div class="musicYear">\r\n                                    2018\r\n                                </div>\r\n                        </div>\r\n                        <div class="musicBio">\r\n                            Move Along was the second Rifftide cover selected to be on a Best of BYU A Cappella album. \r\n                            The song was recorded as part of that album\'s release, and then released as a single a few months later.\r\n                        </div>\r\n                        <div class="musicCredits">\r\n                            <b>Original Artist</b>: The All-American Rejects\r\n                            <b>Arranged by</b>: Isaac McDougal, \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Album Art by</b>: Isaac McDougal.\r\n                            \r\n                        </div>\r\n                        <div class="listenNow">\r\n                            <div>\r\n                                <p>Listen Now:</p>\r\n                                <a href="https://open.spotify.com/album/1A9bWfQWtnR3Sb6gQveDKl" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n                                </a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n        <div class="music">\r\n            <div class="musicImgDiv">\r\n                <img onload="fadeIn(this,.4)" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('backgrounds/singback.png">\r\n            </div>\r\n            <div class="musicInfo">\r\n                <div class="musicSource">\r\n                    <a href=""><img onload="fadeIn(this)" class="albumArt" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('resources/singAlbumArt.jpg"></a>\r\n                </div>\r\n                <div class="musicTextContainer">\r\n                    <div class="musicText">\r\n                        <div class="musicTitle">\r\n\r\n                                <div class="musicName">\r\n                                    Sing!\r\n                                </div>\r\n                                <div class="musicYear">\r\n                                    2017\r\n                                </div>\r\n                        </div>\r\n                        <div class="musicBio">\r\n                            Sing! was the first single ever released by Rifftide. It was selected to be on the 2017 Best of BYU A Cappella album. \r\n                            The song was recorded as part of that album\'s release, and then released as a single a month later. The song remains as\r\n                            Rifftide\'s most well known cover.\r\n                        </div>\r\n                        <div class="musicCredits">\r\n                            <b>Original Artist</b>: Pentatonix,\r\n                            <b>Arranged by</b>: Scott Shattuck \r\n                            <b>Mixed by</b>: Becky Willard, \r\n                            <b>Album Art by</b>: Isaac McDougal.\r\n                            \r\n                        </div>\r\n                        <div class="listenNow">\r\n                            <div>\r\n                                <p>Listen Now:</p>\r\n                                <a href="https://open.spotify.com/album/6qK5m07etOecI5Kiif5QEa" target="blank">\r\n                                    <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n                                </a>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <div id="listenToUs">\r\n\r\n        <div style="z-index: 500;">\r\n            Listen to Rifftide on any platform!\r\n        </div>\r\n        <div class="musicLogos">\r\n            <a href="https://open.spotify.com/artist/6TRcbaV03EF0bofJNKUSI8" target="blank">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/spotify.png">\r\n            </a>\r\n            <a href="https://music.apple.com/us/artist/rifftide/1229959671" target="blank">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/itunes.png">\r\n            </a>\r\n            <a href="https://www.youtube.com/playlist?list=PLJaVJrQa31zOv6yErJMfBFDF_vBZkwNOL&app=desktop" target="blank">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/youtube.png">\r\n            </a>\r\n            <a href="https://music.youtube.com/channel/UCsbF4jCCUrORCMV8s0WJhcQ" target="blank">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/youtubemusic.png">\r\n            </a>\r\n            <a href="https://music.amazon.com/artists/B06XWJ26J2?tab=CATALOG&ref=dm_wcp_artist_link_ad" target="blank">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(settings.IMAGE_URL))
        __M_writer('logos/amazon music.png">\r\n            </a>\r\n        </div>\r\n    </div>\r\n</div>\r\n')
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
{"filename": "C:/Users/isaac/rifftideDMP/resources/templates/music.html", "uri": "music.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 3, "55": 9, "60": 253, "70": 3, "76": 3, "82": 5, "90": 5, "91": 7, "92": 7, "93": 8, "94": 8, "100": 11, "108": 11, "109": 16, "110": 16, "111": 20, "112": 20, "113": 49, "114": 49, "115": 52, "116": 52, "117": 62, "118": 62, "119": 66, "120": 66, "121": 93, "122": 93, "123": 103, "124": 103, "125": 107, "126": 107, "127": 135, "128": 135, "129": 145, "130": 145, "131": 149, "132": 149, "133": 177, "134": 177, "135": 187, "136": 187, "137": 191, "138": 191, "139": 220, "140": 220, "141": 236, "142": 236, "143": 239, "144": 239, "145": 242, "146": 242, "147": 245, "148": 245, "149": 248, "150": 248, "156": 255, "162": 255, "168": 162}}
__M_END_METADATA
"""
