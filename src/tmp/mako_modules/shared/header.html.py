# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346809769.266106
_template_filename = u'/Users/zongzong/Documents/workspace/kds/src/views/shared/header.html'
_template_uri = u'/shared/header.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = []


def render_body(context, **pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_logged_in = context.get('is_logged_in', UNDEFINED)
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<header id="header">\n\t<div id="header-inner">\n\t    <link rel="shortcut icon" href="/static/images/images.ico" type="image/x-icon" />\n\t\t<div id="logo">\n\t\t\t<h1>\n\t\t\t\t<a href="/">\u7f51\u7edc\u5e26\u5bbd\u7ba1\u7406\u7cfb\u7edf</a>\n\t\t\t</h1>\n\t\t</div>\n\t\t<div id="user-menu">\n')
        # SOURCE LINE 11
        if is_logged_in :
            # SOURCE LINE 12
            __M_writer(u'\t\t\t\t')
            __M_writer(unicode(current_user['_id']))
            __M_writer(u' : \n\t\t\t\t<a href="/logout">log-out</a>\n')
            # SOURCE LINE 14
        else :
            # SOURCE LINE 15
            __M_writer(u'\t\t\t\t<a href="/login">log-in</a>\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\t\t</div>\n\t\t<div class="clear"></div>\n\t</div>\n</header>')
        return ''
    finally:
        context.caller_stack._pop_frame()


