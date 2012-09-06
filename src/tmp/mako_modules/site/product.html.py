# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346922140.675495
_template_filename = '/Users/zongzong/Documents/workspace/let/src/views/site/product.html'
_template_uri = '/site/product.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 5
 
import time
    

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
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        custormers = context.get('custormers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u8fd0\u8425\u5546\u7ba1\u7406\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u7528\u6237\u4fe1\u606f\r\n\t</div>\r\n</div>\r\n\t<div class="field">\r\n<table>\r\n\t\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t\t<th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t\t<th align="center">\u8fd0\u8425\u5546</th>\r\n\t\t\t\t\t<th align="center">\u63cf\u8ff0</th>\r\n\t\t\t\t\t<th align="center">\u72b6\u6001</th>\r\n\t\t\t\t\t<th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t\t<th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t\t<th align="center">\u64cd\u4f5c</th>\t\t\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 30
        for c in custormers:
            # SOURCE LINE 31
            __M_writer(u'\t\t\t\t')
            i=1 
            
            __M_writer(u'\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <td align="center">')
            # SOURCE LINE 34
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 35
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 36
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(unicode(c['yname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 38
            __M_writer(unicode(c['description']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 40
            if c['status']==0: 
                # SOURCE LINE 41
                __M_writer(u'\t\t\t\t\t          \u6fc0\u6d3b\r\n')
                # SOURCE LINE 42
            else: 
                # SOURCE LINE 43
                __M_writer(u'\t\t\t\t\t          \u6ce8\u9500\r\n')
                pass
            # SOURCE LINE 45
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t<td align="right" >')
            # SOURCE LINE 46
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 47
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 48
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td align="center"><input type="button" class="button" value="\u64cd\u4f5c" /></td>\r\n\t\t\t\t</tr>\r\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\t\t\t</tbody>\r\n\t\t</table>\r\n</div>\r\n<div id="page-content">\r\n\t<div class="body">\r\n\t\t<a href="http://www.jztech.cn" target="new">\u66f4\u591a\u6280\u672f\u652f\u6301\uff0c\u6b22\u8fce\u8bbf\u95ee\u541b\u4f17\u79d1\u6280\u516c\u53f8\u7f51\u7ad9\uff01</a>   \r\n\t</div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


