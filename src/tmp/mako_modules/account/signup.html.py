# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346212299.818378
_template_filename = '/Users/zongzong/Documents/workspace/kds/src/views/account/signup.html'
_template_uri = '/account/signup.html'
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
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n<div class="form" style="margin:0 auto 0 auto;width: 250px;">\n\t<div class="title">\n\t\t\u6ce8\u518c\n\t</div>\n\t<form action="/signup" method="post"> \n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 10
        __M_writer(unicode(next))
        __M_writer(u'" /> \n\t\t<div class="field">\n\t\t\t<label for="username" class="label">\n\t\t\t\t\u540d\u79f0\uff1a\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t<input type="text" id="username" name="username"/>\n\t\t\t</div>\n\t\t</div>\n\t\t\n\t\t<div class="field">\n\t\t\t<label for="password" class="label">\n\t\t\t\t\u5bc6\u7801\uff1a\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t<input type="password" id="password" name="password"/>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="field">\n\t\t\t<label for="password2" class="label">\n\t\t\t\t\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t<input type="password" id="password2" name="password2"/>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="field">\n\t\t\t<label for="password" class="label">\n\t\t\t\t\u89d2\u8272\uff1a\n\t\t\t</label>\n\t\t\t<div class="input">\n\t\t\t\t\t<select id="roletype" name ="roletype">\n                         <option value=1>\u7ba1\u7406\u5458</option>\n                         <option value=2>\u8fd0\u8425\u5546</option>\n            </select>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class="buttons">\n\t\t\t<input type="submit" value="Signup" class="button" />\n\t\t</div>\n\t</form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


