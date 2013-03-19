# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363063711.859
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/manage.html'
_template_uri = '/site/manage.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
_exports = ['body']


# SOURCE LINE 4
 
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
        status = context.get('status', UNDEFINED)
        int = context.get('int', UNDEFINED)
        cname = context.get('cname', UNDEFINED)
        request = context.get('request', UNDEFINED)
        paginator = context.get('paginator', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(u'\r\n<div class="box">\r\n<div class="box-header">\r\n    <h1>\u8fd0\u8425\u5546\u7ba1\u7406\u754c\u9762 - \u7528\u6237\u4fe1\u606f</h1>\r\n</div>\r\n<div class="box-content">\r\n<form action="/manage" method="post" >\r\n\t<table>\t\t \r\n\t\t<tr>\r\n\t\t\t<td><label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label></td>\r\n\t\t\t<td>\r\n\t\t\t\t<input type="text" id="cname" name="cname" value="')
        # SOURCE LINE 17
        __M_writer(unicode(cname or ''))
        __M_writer(u'" />\r\n\t\t\t</td>\r\n\t\t\t<td><label for="status" class="status">\u72b6\u6001:</label></td>\r\n\t\t\t<td>\r\n\t\t\t\t<select id="status" name ="status" placeholder="City" class="{validate:{required:true}}">\r\n')
        # SOURCE LINE 22
        if status is not None and status is not '':
            # SOURCE LINE 23
            if int(status) == 0:
                # SOURCE LINE 24
                __M_writer(u"\t\t\t\t      <option value='' >\u5168\u90e8</option>\r\n\t\t\t\t\t  <option value=0  selected>\u6ce8\u9500</option>  \r\n\t\t\t\t\t  <option value=1 >\u6fc0\u6d3b</option>   \r\n")
                # SOURCE LINE 27
            else:
                # SOURCE LINE 28
                __M_writer(u"\t\t\t\t      <option value='' >\u5168\u90e8</option>\r\n\t\t\t\t\t  <option value=0 >\u6ce8\u9500</option>\r\n\t\t\t\t\t  <option value=1 selected>\u6fc0\u6d3b</option> \r\n")
            # SOURCE LINE 32
        else:   
            # SOURCE LINE 33
            __M_writer(u"\t\t\t\t      <option value='' selected>\u5168\u90e8</option>\r\n\t\t\t\t      <option value=0 >\u6ce8\u9500</option>\r\n\t\t\t\t\t  <option value=1 >\u6fc0\u6d3b</option> \r\n")
        # SOURCE LINE 37
        __M_writer(u'\t\t\t\t</select>\r\n\t\t\t</td>\r\n\t\t\t<td><button type="submit" class="button"><span class="ui-icon ui-icon-search"></span>\u67e5\u8be2</button></td>\r\n\t\t</tr>\r\n\t</table>\r\n</form>\r\n</div>\r\n</div>\r\n<div class="box">\r\n<div class="box-header"></div>\r\n<div class="box-content">\r\n\t<table>\r\n\t\t<thead>\r\n\t\t\t<tr>\r\n\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u5730\u5740</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u7535\u8bdd</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u90ae\u7bb1</th>\r\n\t\t\t\t<th align="center">\u72b6\u6001</th>\r\n\t\t\t\t<th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t<th align="center">\u5269\u4f59\u65f6\u95f4</th>\r\n\t\t\t\t<th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t<!--<th align="center">\u8d77\u59cbIP</th>\r\n\t\t\t\t<th align="center">\u7ed3\u675fIP</th>-->\r\n\t\t\t\t<th align="center">\u4ef7\u683c</th>\r\n\t\t\t\t<th align="center">\u4f7f\u7528\u8d77\u59cb</th>\r\n\t\t\t\t<th align="center">\u4f7f\u7528\u7ed3\u675f</th>\r\n\t\t\t\t<th align="center">\u64cd\u4f5c</th>\t\t\t\t\r\n\t\t\t</tr>\r\n\t\t</thead>\r\n\t\t<tbody>\r\n\t\t\t')
        # SOURCE LINE 69
        i=1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 70
        for c in paginator.page:
            # SOURCE LINE 71
            __M_writer(u'\t\t\t<tr>\r\n\t\t\t\t<td align="center">')
            # SOURCE LINE 72
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t')
            # SOURCE LINE 73
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t<td>')
            # SOURCE LINE 74
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 75
            __M_writer(unicode(c['address']))
            __M_writer(u'</td>\r\n\t\t\t    <td>')
            # SOURCE LINE 76
            __M_writer(unicode(c['phonenum']))
            __M_writer(u'</td>\r\n\t\t\t    <td>')
            # SOURCE LINE 77
            __M_writer(unicode(c['email']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>\r\n')
            # SOURCE LINE 79
            if c['status']==0: 
                # SOURCE LINE 80
                __M_writer(u'\t\t\t\t\t\t  \u6ce8\u9500\r\n')
                # SOURCE LINE 81
            else: 
                # SOURCE LINE 82
                __M_writer(u'\t\t\t\t\t\t \u6fc0\u6d3b\r\n')
            # SOURCE LINE 84
            __M_writer(u'\t\t\t\t</td>\r\n\t\t\t\t<td align="right" >')
            # SOURCE LINE 85
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t')
            # SOURCE LINE 86
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t')
            # SOURCE LINE 87
            cn=c['cname'] 
            
            __M_writer(u'\r\n\t\t\t\t<td align="right">')
            # SOURCE LINE 88
            __M_writer(unicode(c['continue_to']))
            __M_writer(u'h</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 89
            __M_writer(unicode(ct))
            __M_writer(u'</td>\t\r\n\t\t\t\t<td>')
            # SOURCE LINE 90
            __M_writer(unicode(c['price']))
            __M_writer(u'\u5143</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 91
            __M_writer(unicode(c['begin_at']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 92
            __M_writer(unicode(c['suspended_at']))
            __M_writer(u'</td>\t\t\t\t\r\n\t\t\t\t<td align="center">\r\n\t\t\t\t\t<input type="hidden" value="')
            # SOURCE LINE 94
            __M_writer(unicode(c['_id']))
            __M_writer(u'" class="c_id" name="c_id" />\n\t\t\t\t\t<input type="button" class="button small blue" value="\u6fc0\u6d3b" />\r\n\t\t\t\t\t<input type="button" class="button small" value="\u6ce8\u9500" /> \n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        # SOURCE LINE 100
        __M_writer(u'\t\t</tbody>\r\n\t</table>  \r\n\t\t\t\u7b2c ')
        # SOURCE LINE 102
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \r\n\t\t\t<!-- if there is a previous page print a back link -->\r\n')
        # SOURCE LINE 104
        if paginator.has_previous:
            # SOURCE LINE 105
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\r\n')
        # SOURCE LINE 107
        __M_writer(u'            <!-- if there is a previous and a next page print a divider -->\r\n')
        # SOURCE LINE 108
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 109
            __M_writer(u'                  | \r\n')
        # SOURCE LINE 111
        __M_writer(u'            <!-- if there is a next page print a next link -->\r\n')
        # SOURCE LINE 112
        if paginator.has_next:
            # SOURCE LINE 113
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\r\n')
        # SOURCE LINE 115
        __M_writer(u'     </div>\r\n</div>\r\n<script type="text/javascript">\r\n$(function(){\r\n    $(\'input[value="\u6fc0\u6d3b"]\').click(function(){  \r\n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6fc0\u6d3b\u8be5\u5ba2\u6237\u5417\uff1f\')) \r\n\t\t$.ajax({\r\n\t\t\turl:\'custorm_active?c_id=\'+$(this).parent().parent().find(\'.c_id\').val(),\r\n\t\t\ttype:\'post\',\t\t\t\r\n\t\t\tsuccess:success,\t\t\t\r\n\t\t\tstatusCode: {\r\n\t\t\t\t404: function() {\r\n    \t\t\t\talert(\'page not found\');\r\n  \t\t\t\t}\r\n\t\t\t},\r\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\r\n\t\t\t\talert(textStatus);\r\n\t\t\t}\r\n\t\t});\r\n\t});  \r\n\t$(\'input[value="\u6ce8\u9500"]\').click(function(){\r\n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6ce8\u9500\u8be5\u5ba2\u6237\u5417\uff1f\')) \r\n\t\t$.ajax({\r\n\t\t\turl:\'custorm_del?c_id=\'+$(this).parent().parent().find(\'.c_id\').val(),\r\n\t\t\ttype:\'post\',\t\t\t\r\n\t\t\tsuccess:success,\t\t\t\r\n\t\t\tstatusCode: {\r\n\t\t\t\t404: function() {\r\n    \t\t\t\talert(\'page not found\');\r\n  \t\t\t\t}\r\n\t\t\t},\r\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\r\n\t\t\t\talert(textStatus);\r\n\t\t\t}\r\n\t\t});\r\n\t});\r\n\tfunction success(){\r\n\t    window.location.reload();\r\n\t}\r\n});\r\n</script>        \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


