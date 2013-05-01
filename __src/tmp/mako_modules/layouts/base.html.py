# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1356321200.5
_enable_loop = True
_template_filename = u'E:\\workspacePY\\sod\\src/views/layouts/base.html'
_template_uri = u'/layouts/base.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
_exports = ['scripts', 'page_title', 'head_tags']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!doctype html>\n<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="zh-CN"> <![endif]-->\n<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="zh-CN"> <![endif]-->\n<!--[if IE 8]>    <html class="no-js lt-ie9" lang="zh-CN"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class="no-js" lang="zh-CN">\n<!--<![endif]-->\n<head>\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t<meta charset="utf-8">\n\t<meta name="apple-mobile-web-app-capable" content="yes" />\n\t<meta name="apple-mobile-web-app-status-bar-style" content="black" />\n\n\t')
        # SOURCE LINE 15
        __M_writer(u'\n\t<title>\n\t\t')
        # SOURCE LINE 17
        __M_writer(unicode(self.page_title()))
        __M_writer(u'\n\t</title>\n\t\n\t<meta name="keywords" content="" />\n\t<meta name="description" content="">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<!--[if lt IE 9]>\n\t\t<script src="http://html5shim.googlecode.com/svn/trunk/html5-els.js?')
        # SOURCE LINE 24
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<![endif]-->\n\t\n\t<link rel="stylesheet" href="/static/css/reset.css?')
        # SOURCE LINE 27
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/icons.css?')
        # SOURCE LINE 28
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/formalize.css?')
        # SOURCE LINE 29
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/checkboxes.css?')
        # SOURCE LINE 30
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/sourcerer.css?')
        # SOURCE LINE 31
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/jqueryui.css?')
        # SOURCE LINE 32
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/tipsy.css?')
        # SOURCE LINE 33
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/calendar.css?')
        # SOURCE LINE 34
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/tags.css?')
        # SOURCE LINE 35
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/fonts.css?')
        # SOURCE LINE 36
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/selectboxes.css?')
        # SOURCE LINE 37
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/960.css?')
        # SOURCE LINE 38
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" href="/static/css/main.css?')
        # SOURCE LINE 39
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="stylesheet" media="all and (orientation:portrait)" href="/static/css/portrait.css?')
        # SOURCE LINE 40
        __M_writer(unicode(Filters.version()))
        __M_writer(u'" />\n\t<link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png" />\n\t<link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />\n\t\n\t\n\t\n\t<!--[if lt IE 9]>\n    <script src="/static/js/html5.js?')
        # SOURCE LINE 47
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n    <![endif]-->\n\n\t<!-- JavaScript -->\n\t<script src="/static/js/jquery.min.js?')
        # SOURCE LINE 51
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jqueryui.min.js?')
        # SOURCE LINE 52
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.cookies.js?')
        # SOURCE LINE 53
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.pjax.js?')
        # SOURCE LINE 54
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/formalize.min.js?')
        # SOURCE LINE 55
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.metadata.js?')
        # SOURCE LINE 56
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.validate.js?')
        # SOURCE LINE 57
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.checkboxes.js?')
        # SOURCE LINE 58
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.chosen.js?')
        # SOURCE LINE 59
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.fileinput.js?')
        # SOURCE LINE 60
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.datatables.js?')
        # SOURCE LINE 61
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.sourcerer.js?')
        # SOURCE LINE 62
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.tipsy.js?')
        # SOURCE LINE 63
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.calendar.js?')
        # SOURCE LINE 64
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.inputtags.min.js?')
        # SOURCE LINE 65
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.wymeditor.js?')
        # SOURCE LINE 66
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.livequery.js?')
        # SOURCE LINE 67
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery.flot.min.js?')
        # SOURCE LINE 68
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/jquery-ui-timepicker-addon.js?')
        # SOURCE LINE 69
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t<script src="/static/js/application.js?')
        # SOURCE LINE 70
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t\n\t')
        # SOURCE LINE 72
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n\t')
        # SOURCE LINE 73
        __M_writer(u'\n</head>\n<body>\n\t<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->\n\t\n\t')
        # SOURCE LINE 78
        __M_writer(unicode(next.body()))
        __M_writer(u'\n\t  \n    \n\t')
        # SOURCE LINE 81
        __M_writer(unicode(self.scripts()))
        __M_writer(u' \n\t')
        # SOURCE LINE 82
        __M_writer(u'\n\t\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(u'\u541b\u4f17\u79d1\u6280')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


