# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346228632.039205
_template_filename = '/Users/zongzong/Documents/workspace/kds/src/views/site/users.html'
_template_uri = '/site/users.html'
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
def render_body(context, **pageargs):
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
        users = context.get('users', UNDEFINED)
        endif = context.get('endif', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u8fd0\u8425\u5546\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u4fe1\u606f\u67e5\u8be2\r\n\t</div>\r\n</div>\r\n\t<div class="field">\r\n<table>\r\n\t\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u8fd0\u8425\u5546\u540d\u79f0</th>\r\n\t\t\t\t\t<th align="center">\u6ce8\u518c\u65e5\u671f</th>\r\n\t\t\t\t\t<th align="center">\u767b\u9646\u6b21\u6570</th>\r\n\t\t\t\t\t<th align="center">\u4e0a\u6b21\u767b\u9646\u65f6\u95f4</th>\r\n\t\t\t\t\t<th align="center">\u64cd\u4f5c</th>\r\n\t\t\t\t</tr>\r\n\t\t\t\t')
        # SOURCE LINE 27
        i = 1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 28
        for c in users:
            # SOURCE LINE 29
            __M_writer(u'\t\t\t\t<tr>\r\n\t\t\t\t    <td align="center">')
            # SOURCE LINE 30
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 31
            i = i + 1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(unicode(c['_id']))
            __M_writer(u'</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 33
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(unicode(c['history']['num_logins']))
            __M_writer(u'</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 36
 
            lt = ''
            if c['history']['num_logins'] > 0: 
               lt = c['history']['last_login'].strftime("%y-%m-%d %H:%M:%S")  
            else:
               lt = ''          
            endif
                                                     
            
            # SOURCE LINE 43
            __M_writer(u'\r\n\t\t\t\t\t <td>')
            # SOURCE LINE 44
            __M_writer(unicode(lt))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td align="center"><input type="button" class="button" value="\u6ce8\u9500" />  <input type="button" class="button" value="\u6fc0\u6d3b" /></td>\r\n\t\t\t\t</tr>\r\n')
            pass
        # SOURCE LINE 48
        __M_writer(u'\t\t\t</tbody>\r\n\t\t</table>\r\n</div>\r\n<div id="page-content">\r\n\t<div class="body">\r\n\t\t<a href="http://www.jztech.cn" target="new">\u66f4\u591a\u6280\u672f\u652f\u6301\uff0c\u6b22\u8fce\u8bbf\u95ee\u541b\u4f17\u79d1\u6280\u516c\u53f8\u7f51\u7ad9\uff01</a>   \r\n\t</div>\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


