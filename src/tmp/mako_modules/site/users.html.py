# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363055699.406
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/users.html'
_template_uri = '/site/users.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
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
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        usertype = context.get('usertype', UNDEFINED)
        users = context.get('users', UNDEFINED)
        endif = context.get('endif', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<div class="box">\r\n')
        # SOURCE LINE 5
        __M_writer(u'\r\n<div class="box-header">\r\n\t\t<h1> \r\n')
        # SOURCE LINE 8
        if usertype==1:
            # SOURCE LINE 9
            __M_writer(u'\t\t\u7ba1\u7406\u5458\r\n')
            # SOURCE LINE 10
        else:
            # SOURCE LINE 11
            __M_writer(u'\t          \u8fd0\u8425\u5546\r\n')
        # SOURCE LINE 13
        __M_writer(u'\t     -\u4fe1\u606f\u67e5\u8be2</h1>\r\n</div>\r\n<div class="box-content">\r\n\t<table id="product" class="table table-hover">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u540d\u79f0</th>\r\n\t\t\t\t    <th align="center">\u72b6\u6001</th>\r\n\t\t\t\t\t<th align="center">\u6ce8\u518c\u65e5\u671f</th>\r\n\t\t\t\t\t<th align="center">\u767b\u5f55\u6b21\u6570</th>\r\n\t\t\t\t\t<th align="center">\u4e0a\u6b21\u767b\u5f55\u65f6\u95f4</th>\r\n\t\t\t\t\t<th align="center">\u64cd\u4f5c</th>\r\n\t\t\t\t</tr>\t\t\t\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n\t\t\t\t')
        # SOURCE LINE 29
        i=1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 30
        for c in users:
            # SOURCE LINE 31
            __M_writer(u'\t\t\t\t<tr style="cursor:pointer">\r\n\t\t\t\t    <td align="center">')
            # SOURCE LINE 32
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 33
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(unicode(c['_id']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 36
            if c['status']==0: 
                # SOURCE LINE 37
                __M_writer(u'\t\t\t\t\t\t  \u6fc0\u6d3b\r\n')
                # SOURCE LINE 38
            else: 
                # SOURCE LINE 39
                __M_writer(u'\t\t\t\t\t\t  \u6ce8\u9500\r\n')
            # SOURCE LINE 41
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 42
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 43
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 44
            __M_writer(unicode(c['history']['num_logins']))
            __M_writer(u'</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 45
 
            lt = ''
            if c['history']['num_logins'] >0 : 
               lt = c['history']['last_login'].strftime("%y-%m-%d %H:%M:%S")  
            else:
               lt = ''          
            endif
                                                     
            
            # SOURCE LINE 52
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 53
            __M_writer(unicode(lt))
            __M_writer(u'</td>\r\n\t\t\t\t\t<input type="hidden" value="')
            # SOURCE LINE 54
            __M_writer(unicode(c['_id']))
            __M_writer(u'" class="_id" name="_id" />\r\n\t\t\t\t\t<td align="center"><input type="button" class="button" value="\u6ce8\u9500" />  <input type="button" class="button" value="\u6fc0\u6d3b" /></td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 58
        __M_writer(u'\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n<script type="text/javascript">\r\n$(function(){\r\n$(\'input[value="\u6fc0\u6d3b"]\').click(function(){\r\n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6fc0\u6d3b\u8be5\u7528\u6237\u5417\uff1f\')) \r\n\t\t$.ajax({\r\n\t\t\turl:\'user_active?u_id=\'+$(this).parent().parent().find(\'._id\').val(),\r\n\t\t\ttype:\'post\',\t\t\t\r\n\t\t\tsuccess:success,\t\t\t\r\n\t\t\tstatusCode: {\r\n\t\t\t\t404: function() {\r\n    \t\t\t\talert(\'page not found\');\r\n  \t\t\t\t}\r\n\t\t\t},\r\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\r\n\t\t\t\talert(textStatus);\r\n\t\t\t}\r\n\t\t});\r\n\t});\r\n\t$(\'input[value="\u6ce8\u9500"]\').click(function(){\r\n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6ce8\u9500\u8be5\u7528\u6237\u5417\uff1f\')) \r\n\t\t$.ajax({\r\n\t\t\turl:\'user_del?u_id=\'+$(this).parent().parent().find(\'._id\').val(),\r\n\t\t\ttype:\'post\',\t\t\t\r\n\t\t\tsuccess:success,\t\t\t\r\n\t\t\tstatusCode: {\r\n\t\t\t\t404: function() {\r\n    \t\t\t\talert(\'page not found\');\r\n  \t\t\t\t}\r\n\t\t\t},\r\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\r\n\t\t\t\talert(textStatus);\r\n\t\t\t}\r\n\t\t});\r\n\t});\r\n\tfunction success(){\r\n\t    window.location.reload();\r\n\t}\r\n});\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


