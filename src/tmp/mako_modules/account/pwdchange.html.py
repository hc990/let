# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346904476.602793
_template_filename = '/Users/zongzong/Documents/workspace/kds/src/views/account/pwdchange.html'
_template_uri = '/account/pwdchange.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


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
    return runtime._inherit_from(context, u'/layouts/content.html', _template_uri)
def render_body(context, **pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n<div class="form" style="margin:0 auto 0 auto;width: 250px;">\r\n\t<div class="title">\r\n\t\t\u4fee\u6539\u5bc6\u7801\r\n\t</div>\r\n\t<form action="/signup" method="post"> \r\n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 10
        __M_writer(unicode(next))
        __M_writer(u'" /> \r\n\t\t\r\n\t\t<div class="field">\r\n\t\t\t<label for="password" class="label">\r\n\t\t\t\t\u539f\u5bc6\u7801\uff1a\r\n\t\t\t</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="password" id="password" name="password"/>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<div class="field">\r\n\t\t\t<label for="password" class="label">\r\n\t\t\t\t\u65b0\u5bc6\u7801\uff1a\r\n\t\t\t</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="password" id="new_pw" name="new_pw"/>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<div class="field">\r\n\t\t\t<label for="password2" class="label">\r\n\t\t\t\t\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a\r\n\t\t\t</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="password" id="new_pw_again" name="new_pw_again"/>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t\t<div class="buttons">\r\n\t\t\t<input type="submit" value="\u786e\u5b9a" class="button" />\r\n\t\t</div>\r\n\t</form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


