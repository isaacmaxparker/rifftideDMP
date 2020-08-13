# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1597289554.0964131
_enable_loop = True
_template_filename = 'C:/Users/isaac/rifftideDMP/homepage/templates/latestVideo.html'
_template_uri = 'latestVideo.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer("<script>\r\n   const RELEASE_URL = 'https://raw.githubusercontent.com/isaacmcdgl/RifftideJSON/master/JSON/releases.json'\r\n   const REQUEST_STATUS_OK = 200;\r\n    const REQUEST_STATUS_ERROR = 400;\r\n\r\n   function ajax(url, successCallback, failureCallback, skipJsonParse) {\r\n\r\n    let request = new XMLHttpRequest();\r\n    request.open('GET', url, true);\r\n\r\n    request.onload = function() {\r\n        if (this.status >= REQUEST_STATUS_OK && this.status < REQUEST_STATUS_ERROR) {\r\n        \r\n            let data = (\r\n                skipJsonParse \r\n                ? request.response \r\n                : JSON.parse(request.response)\r\n            );\r\n\r\n            if (typeof successCallback === 'function') {\r\n                successCallback(data);\r\n            }\r\n        } else {\r\n            if (typeof failureCallback === 'function') {\r\n                failureCallback(request);\r\n            }\r\n        }\r\n    };\r\n\r\n    request.onerror = failureCallback;\r\n    request.send();\r\n    };\r\n\r\n    window.onload = (event) => {\r\n        loadURL();\r\n    };\r\n\r\n    function sortByKey(array, key) {\r\n    return array.sort(function(a, b) {\r\n        var x = a[key]; var y = b[key];\r\n        return ((x > y) ? -1 : ((x < y) ? 1 : 0));\r\n    });\r\n    }\r\n\r\n    function loadURL(){\r\n        ajax(RELEASE_URL, function(data) {\r\n                releases = data;\r\n                releaser = sortByKey(releases,'release_date')\r\n                console.log(releaser)\r\n                release = releaser[0];\r\n\r\n                //window.location.href = release.youtube_url;\r\n            }\r\n        );\r\n    }\r\n</script>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/isaac/rifftideDMP/homepage/templates/latestVideo.html", "uri": "latestVideo.html", "source_encoding": "utf-8", "line_map": {"18": 0, "23": 1, "29": 23}}
__M_END_METADATA
"""
