# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363233688.5
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/exchange.html'
_template_uri = '/site/exchange.html'
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
        __M_writer(u'\n')
        # SOURCE LINE 160
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        paginator = context.get('paginator', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n<div class="box">\n\t<div class="box-header">\n\t\t<h1>\u4ea4\u6362\u673a\u4fe1\u606f</h1>\n\t</div>\n\t<div class="box-content">\n\t<table id="product" class="table table-hover">\n\t\t\t<thead>  \n\t\t\t\t<tr>\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\n\t\t\t\t    <th align="center">\u4ea4\u6362\u673a\u540d\u79f0</th>\n\t\t\t\t    <th align="center">ip\u5730\u5740</th>\n\t\t\t\t    <th align="center">\u72b6\u6001</th>\t\n\t\t\t\t    <th align="center">\u521b\u5efa\u65f6\u95f4</th>\t\t\n\t\t\t\t    <th align="center">\u64cd\u4f5c</th>\t\t\t\t\t\t\t\t\n\t\t\t\t</tr>\n\t\t\t</thead>\n\t\t\t<tbody>\n\t\t\t')
        # SOURCE LINE 22
        i=1 
        
        __M_writer(u'\n')
        # SOURCE LINE 23
        for c in paginator.page:
            # SOURCE LINE 24
            __M_writer(u'\t\t\t\t<tr style="cursor:pointer">\n\t\t\t\t    <td align="center" >')
            # SOURCE LINE 25
            __M_writer(unicode(i))
            __M_writer(u'</td>\n\t\t\t\t    ')
            # SOURCE LINE 26
            i=i+1 
            
            __M_writer(u'\n\t\t\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(unicode(c['ename']))
            __M_writer(u'</td>  \n\t\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(unicode(c['ipAddress']))
            __M_writer(u'</td>\n\t\t\t\t\t<td>\n')
            # SOURCE LINE 30
            if c['status']==0: 
                # SOURCE LINE 31
                __M_writer(u'\t\t\t\t\t\t  \u6ce8\u9500\n')
                # SOURCE LINE 32
            else: 
                # SOURCE LINE 33
                __M_writer(u'\t\t\t\t\t\t \u6fc0\u6d3b\n')
            # SOURCE LINE 35
            __M_writer(u'\t\t\t\t</td>\n\t\t\t\t')
            # SOURCE LINE 36
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\n\t\t\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(unicode(ct))
            __M_writer(u'</td>\t\t\n\t\t\t\t<input type="hidden" value="')
            # SOURCE LINE 38
            __M_writer(unicode(c['_id']))
            __M_writer(u'" class="e_id" name="e_id" />\t\n\t\t\t\t<td><input type="button" class="button" value="\u6ce8\u9500" /><input type="button" class="button" value="\u6fc0\u6d3b" /></td>\n\t\t\t\t</tr>\n')
        # SOURCE LINE 42
        __M_writer(u'\t\t        </tbody>\n\t\t        <tfoot>\n\t\t        <tr id="ui-detail-row" >\n\t\t        \t<td colspan="10">\n\t\t        \t\t<table id="ui-detail-content">\t\t        \t\t\t\n\t\t        \t\t</table>\n\t\t        \t</td>\n\t\t        </tr>\n\t\t\t</tfoot>\n\t</table>\n\t<div>\n\t\t\t\u7b2c ')
        # SOURCE LINE 53
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \n\t\t\t<!-- if there is a previous page print a back link -->\n')
        # SOURCE LINE 55
        if paginator.has_previous:
            # SOURCE LINE 56
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\n')
        # SOURCE LINE 58
        __M_writer(u'            <!-- if there is a previous and a next page print a divider -->\n')
        # SOURCE LINE 59
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 60
            __M_writer(u'                  | \n')
        # SOURCE LINE 62
        __M_writer(u'            <!-- if there is a next page print a next link -->\n')
        # SOURCE LINE 63
        if paginator.has_next:
            # SOURCE LINE 64
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\n')
        # SOURCE LINE 66
        __M_writer(u'\t</div>\n</div>\n</div>\n<script type="text/javascript">\n$(document).ready(function(){ \n  var tds = $("td"); \n  tds.click(tdClick); \n}); \nfunction tdClick(){ \n    var td = $(this); \n    var text = td.text(); \n    td.html("");\n    var input = $("<input>"); \n    input.attr("value",text); \n    td.append(input); \n    var inputDom = input.get(0); \n    inputDom.select(); \n    td.unbind("click"); \n    input.keyup(function(event){ \n      var myEvent = event || window.event; \n      var keyCode = myEvent.keyCode; \n      if(keyCode == 13){   \n        var _id = $(this).parent().parent().find(\'.e_id\').val()  \n        var inputNode = $(this); \n        var inputText = inputNode.val(); \n        var tdNode = inputNode.parent(); \n\t    tdNode.html(inputText); \n\t    $.ajax({\n\t\t\turl:\'update_exchange_ip?e_id=\'+_id+\'&ip=\'+inputText,  \n\t\t\ttype:\'post\',\t\t\t\n\t\t\tsuccess:success2,\t\t\t\n\t\t\tstatusCode: {\n\t\t\t\t404: function() {\n    \t\t\t\talert(\'error\');\n  \t\t\t\t}\n\t\t\t},\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\n\t\t\t\talert(textStatus);\n\t\t\t}\n\t     });   \n        tdNode.click(tdClick); \n      } \n    }); \n    function success2(){\n      tdNode.html(inputText); \n      tdNode.click(tdClick); \n\t  confirm("\u4fee\u6539\u5b8c\u6210!");\n    }\n    input.blur(function(){ \n      var inputNode = $(this); \n      var inputText = inputNode.val(); \n      var tdNode = inputNode.parent(); \n      \n    }); \n  }\n\n$(function(){\n    $(\'input[value="\u6fc0\u6d3b"]\').click(function(){  \n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6fc0\u6d3b\u8be5\u4ea4\u6362\u673a\u5417\uff1f\')) \n\t\t$.ajax({\n\t\t\turl:\'exchange_active?e_id=\'+$(this).parent().parent().find(\'.e_id\').val(),\n\t\t\ttype:\'post\',\t\t\t\n\t\t\tsuccess:success,\t\t\t\n\t\t\tstatusCode: {\n\t\t\t\t404: function() {\n    \t\t\t\talert(\'page not found\');\n  \t\t\t\t}\n\t\t\t},\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\n\t\t\t\talert(textStatus);\n\t\t\t}\n\t\t});\n\t});  \n\t$(\'input[value="\u6ce8\u9500"]\').click(function(){\n\t\tif(confirm(\'\u60a8\u786e\u5b9a\u6ce8\u9500\u8be5\u4ea4\u6362\u673a\u5417\uff1f\')) \n\t\t$.ajax({\n\t\t\turl:\'exchange_del?e_id=\'+$(this).parent().parent().find(\'.e_id\').val(),\n\t\t\ttype:\'post\',\t\t\t\n\t\t\tsuccess:success,\t\t\t\n\t\t\tstatusCode: {\n\t\t\t\t404: function() {\n    \t\t\t\talert(\'page not found\');\n  \t\t\t\t}\n\t\t\t},\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\n\t\t\t\talert(textStatus);\n\t\t\t}\n\t\t});\n\t});\n\tfunction success(){\n\t    window.location.reload();\n\t}\n});\n</script>  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


