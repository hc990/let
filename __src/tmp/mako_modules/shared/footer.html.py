# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1355724449.218
_enable_loop = True
_template_filename = u'E:\\workspacePY\\sod\\src/views/shared/footer.html'
_template_uri = u'/shared/footer.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n<footer id="footer">\n\t<div id="footer-inner">\n\t\t<div id="copyright">\n\t\t\tpowered by jztec &copy; 2012. All rights reserved.\n\t\t</div>\n\t</div>\n</footer>')
        return ''
    finally:
        context.caller_stack._pop_frame()


