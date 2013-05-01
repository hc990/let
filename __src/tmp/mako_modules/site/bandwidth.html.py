# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1361954528.5
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/bandwidth.html'
_template_uri = '/site/bandwidth.html'
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
        __M_writer(u'\r\n')
        # SOURCE LINE 46
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        cname = context.get('cname', UNDEFINED)
        p_id = context.get('p_id', UNDEFINED)
        oname = context.get('oname', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<style>\r\nhtml{font-size:12px; font-family:\'\'Hiragino Sans GB W3; -webkit-font-smoothing:antialiased; overflow:hidden; }\r\nhtml,body{margin:0; padding:0; overflow:hidden;}\r\n#primary,#secondary,#header,header{display:none;}\r\n#maincontainer,#main{background-color:white;}\r\n#main div.box{border:1px soldi red;}\r\nselect {width:120px;}\r\n</style>\r\n\r\n<form action="/bandwidth" method="post" > \r\n\t\t    <input type="hidden" id="p_id" name="p_id" value="')
        # SOURCE LINE 14
        __M_writer(unicode(p_id))
        __M_writer(u'"  class="required"/>\r\n\t\t    <input type="hidden" id="cname" name="cname" value="')
        # SOURCE LINE 15
        __M_writer(unicode(cname))
        __M_writer(u'"  class="required"/>\r\n\t\t    <input type="hidden" id="oname" name="oname" value="')
        # SOURCE LINE 16
        __M_writer(unicode(oname))
        __M_writer(u'"  class="required"/>\r\n\t\t    <p>\r\n\t\t    <label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:')
        # SOURCE LINE 18
        __M_writer(unicode(cname))
        __M_writer(u'</label>\r\n\t\t    <br/>\r\n\t\t    <label for="oname" class="label">\u8fd0\u8425\u5546\u540d\u79f0:')
        # SOURCE LINE 20
        __M_writer(unicode(oname))
        __M_writer(u'</label>  \r\n\t\t    </p>\r\n\t\t    <p>\r\n\t\t\t<label for="bandwidth" class="label">\u5e26\u5bbd:</label>\r\n\t\t\t<select id="bandwidth" name="bandwidth" class="required"/>\r\n')
        # SOURCE LINE 25
        for e in range(20):
            # SOURCE LINE 26
            __M_writer(u'\t\t\t\t         <option value=')
            __M_writer(unicode(e+1))
            __M_writer(u'>')
            __M_writer(unicode(e+1))
            __M_writer(u'</option>\r\n')
        # SOURCE LINE 28
        __M_writer(u'\t\t\t          <option value=50>50</option>  \r\n\t\t\t          <option value=100>100</option>\t\t\t      \r\n\t\t\t</select>M\r\n\t\t\t</p>\r\n\t\t\t<p>\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4:</label>\r\n\t\t\t\t <input type="datetime" id="begin_at" name="begin_at" class="datepicker_date required" required="required"/>\t\r\n\t\t\t</p>\r\n\t\t\t<p>\r\n\t\t\t<label for="suspended_at" class="label">\u7ed3\u675f\u65f6\u95f4:</label>\r\n\t\t\t\t <input type="datetime" id="suspended_at" name="suspended_at" class="datepicker_date required"/>\t\r\n\t\t\t</p>\r\n\t\t\t<p>\t\t\t\r\n\t\t\t\t<input type="submit" class="button blue small" value="\u786e\u5b9a" />\r\n\t\t\t\t<input type="reset" class="button small" value="\u91cd\u7f6e"/>\r\n\t\t\t</p>\r\n</form>\t\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


