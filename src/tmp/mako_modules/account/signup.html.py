# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363162705.64
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/account/signup.html'
_template_uri = '/account/signup.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
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
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\t<div class="box">\n\t<div class="box-header">\n\t\t<h1>\u6ce8\u518c</h1>\n\t</div>\n\t<div class="box-content">\n\t<form action="/signup" method="post"> \n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 10
        __M_writer(unicode(next))
        __M_writer(u'" /> \n\t\t<p>\n\t\t\t<label for="username" class="label">\n\t\t\t\t\u540d\u79f0\uff1a\n\t\t\t</label>\n\t\t\t\t<input type="text" id="username" name="username" class="required"/>\n\t\t</p>\n\t\t<p>\n\t\t\t<label for="password" class="label">\n\t\t\t\t\u5bc6\u7801\uff1a\n\t\t\t</label>\n\t\t\t\t<input type="password" id="password" name="password" class="required" /> \n\t\t</p>\n\t\t<p>\n\t\t\t<label for="password2" class="label">\n\t\t\t\t\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801\uff1a\n\t\t\t</label>\n\t\t\t\t<input type="password" id="password2" name="password2" class="required" />\n\t\t</p>\n\t\t<p>\n\t\t\t<label for="password" class="label">\n\t\t\t\t\u89d2\u8272\uff1a\n\t\t\t</label>\n\t\t\t\t<select id="roletype" name ="roletype">\n                    <option value=1>\u7ba1\u7406\u5458</option>\n                    <option value=2>\u8fd0\u8425\u5546</option>\n\t\t\t\t</select>\n\t\t</p>\n\t\t<p>\n\t\t\t<input type="submit" value="\u6ce8\u518c" class="button blue" />\n\t\t</p>\n\t</form>\n</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


