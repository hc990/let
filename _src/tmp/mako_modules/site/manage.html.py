# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1346902919.407605
_template_filename = '/Users/zongzong/Documents/workspace/kds/src/views/site/manage.html'
_template_uri = '/site/manage.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 11
 
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
        status = context.get('status', UNDEFINED)
        cname = context.get('cname', UNDEFINED)
        custormers = context.get('custormers', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<script type="text/javascript">\r\nfunction _do_del(cname){\r\nalert(cname);\r\n}\r\n\r\n</script>\r\n\r\n')
        # SOURCE LINE 13
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u8fd0\u8425\u5546\u7ba1\u7406\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u7528\u6237\u4fe1\u606f\r\n\t</div>\r\n</div>\r\n<table>\r\n<form action="/manage" method="post" >\r\n\t \r\n  <tr>\r\n     <td><label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label></td>\r\n\t\t\t  <td>\r\n\t\t\t\t<input type="text" id="cname" name="cname" value="')
        # SOURCE LINE 28
        __M_writer(unicode(cname))
        __M_writer(u'"/>\r\n\t\t\t</td>\r\n\t<td><label for="status" class="status">\u72b6\u6001:</label></td>\r\n     <td>\r\n\t\t<select id="status" name ="status">\r\n')
        # SOURCE LINE 33
        if status == '0':
            # SOURCE LINE 34
            __M_writer(u"              <option value='0'  selected >\u6fc0\u6d3b</option>  \r\n              <option value='1' >\u6ce8\u9500</option> \r\n")
            # SOURCE LINE 36
        else:
            # SOURCE LINE 37
            __M_writer(u"\t\t      <option value='0'> \u6fc0\u6d3b</option>  \r\n              <option value='1' selected >\u6ce8\u9500</option> \r\n")
            pass
        # SOURCE LINE 40
        __M_writer(u'\t\t\r\n                  \r\n        </select>\r\n    </td><td><input type="submit"  class="button" value="\u67e5\u8be2" /></td>\r\n   </tr>\r\n</form>\r\n</table>\r\n<br>\r\n\t<div class="field">\r\n<table>\r\n\t\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t\t<th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t\t<th align="center">\u63cf\u8ff0</th>\r\n\t\t\t\t\t<th align="center">\u72b6\u6001</th>\r\n\t\t\t\t\t<th align="center">\u6ee1\u5e45\u5e26\u5bbd(\u5355\u4f4d:\u5146)</th>\r\n\t\t\t\t\t<th align="center">\u5269\u4f59\u65f6\u95f4(\u5355\u4f4d:\u5c0f\u65f6)</th>\r\n\t\t\t\t\t<th align="center">\u6ce8\u518c\u65f6\u95f4</th>\t\r\n\t\t\t\t\t<th align="center">\u4f7f\u7528\u8d77\u59cb</th>\r\n\t\t\t\t\t<th align="center">\u4f7f\u7528\u7ed3\u675f</th>\r\n\t\t\t\t\t<th align="center">\u64cd\u4f5c</th>\r\n\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n\t\t\t\t')
        # SOURCE LINE 64
        i = 1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 65
        for c in custormers:
            # SOURCE LINE 66
            __M_writer(u'\t\t\t\t<tr>\r\n\t\t\t\t    <td align="center">')
            # SOURCE LINE 67
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 68
            i = i + 1 
            
            __M_writer(u'\r\n\t\t\t\t    \r\n\t\t\t\t \r\n\t\t\t\t\t<td>')
            # SOURCE LINE 71
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 72
            __M_writer(unicode(c['description']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 74
            if c['status'] == 1: 
                # SOURCE LINE 75
                __M_writer(u'\t\t\t\t\t          \u672a\u6fc0\u6d3b\r\n')
                # SOURCE LINE 76
            else: 
                # SOURCE LINE 77
                __M_writer(u'\t\t\t\t\t          \u6fc0\u6d3b\r\n')
                pass
            # SOURCE LINE 79
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t \r\n\t\t\t\t\t<td align="right" >')
            # SOURCE LINE 81
            __M_writer(unicode(c['ctype']))
            __M_writer(u'</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 82
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t')
            # SOURCE LINE 83
            cn = c['_id'] 
            
            __M_writer(u'\r\n\t\t\t\t\t<td align="right">')
            # SOURCE LINE 84
            __M_writer(unicode(c['continue_to']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 85
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 87
            __M_writer(unicode(c['begin_at']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 88
            __M_writer(unicode(c['suspended_at']))
            __M_writer(u'</td>\r\n\t\t\t\t\t\r\n\t\t\t\t\t<td align="center"><input type="button" class="button" value="\u6ce8\u9500" onclick="_do_del(')
            # SOURCE LINE 90
            __M_writer(unicode(cn))
            __M_writer(u')"  />  <input type="button" class="button" value="\u6fc0\u6d3b" /></td>\r\n\t\t\t\t</tr>\r\n')
            pass
        # SOURCE LINE 93
        __M_writer(u'\t\t\t</tbody>\r\n\t\t</table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


