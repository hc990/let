# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1345814279.030134
_template_filename = '/Users/zongzong/Documents/workspace/kds/src/views/site/index.html'
_template_uri = '/site/index.html'
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
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n <div id="page-header">\n\t<div class="title">\n\t\t\u6b22\u8fce\u4f7f\u7528\uff01\n\t</div>\n\t<div class="subtitle">\n\t\tversion 1.0\t\n\t</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


