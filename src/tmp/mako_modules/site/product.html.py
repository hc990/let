# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1362040287.296
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/product.html'
_template_uri = '/site/product.html'
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
        # SOURCE LINE 127
        __M_writer(u'\r\n\r\n')
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
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n<div class="box">\r\n\t<div class="box-header">\r\n\t\t<h1>\u4ea7\u54c1\u7ba1\u7406\u754c\u9762-\u4ea7\u54c1\u4fe1\u606f</h1>\r\n\t</div>\r\n\t<div class="box-content">\r\n\t<table id="product" class="table table-hover">\r\n\t\t\t<thead>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u5730\u5740</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u7535\u8bdd</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u90ae\u7bb1</th>\r\n\t\t\t\t    <th align="center">\u72b6\u6001</th>\r\n\t\t\t\t    <th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t    <th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t    <!--<th align="center">\u8d77\u59cbip</th>\r\n\t\t\t\t    <th align="center">\u7ed3\u675fip</th>-->\r\n\t\t\t\t    <th align="center">\u64cd\u4f5c</th>\t\t\t\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n\t\t\t</thead>\r\n\t\t\t<tbody>\r\n\t\t\t    ')
        # SOURCE LINE 27
        i=1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 28
        for c in paginator.page:
            # SOURCE LINE 29
            __M_writer(u'\t\t\t\t<tr style="cursor:pointer">\r\n\t\t\t\t    <td align="center" >')
            # SOURCE LINE 30
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 31
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 32
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>  \r\n\t\t\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(unicode(c['address']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(unicode(c['phonenum']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(unicode(c['email']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 37
            if c['status']==0: 
                # SOURCE LINE 38
                __M_writer(u'\t\t\t\t\t              \u6ce8\u9500\r\n')
                # SOURCE LINE 39
            else: 
                # SOURCE LINE 40
                __M_writer(u'\t\t\t\t\t              \u6fc0\u6d3b    \r\n')
            # SOURCE LINE 42
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t<td align="right" >')
            # SOURCE LINE 43
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 44
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 45
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td align="center">\r\n')
            # SOURCE LINE 47
            if c['status']==1:
                # SOURCE LINE 48
                __M_writer(u'\t\t\t\t\t\t<a href="#modal1" class="modal button small">\u64cd\u4f5c</a>\r\n\t\t\t\t\t\t<input type="hidden" class="cid" value="')
                # SOURCE LINE 49
                __M_writer(unicode(c['_id']))
                __M_writer(u'" />\r\n')
            # SOURCE LINE 51
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 54
        __M_writer(u'\t\t        </tbody>\r\n\t\t    <tfoot>\r\n\t\t        <tr id="ui-detail-row" >\r\n\t\t        \t<td colspan="10">\r\n\t\t        \t\t<table id="ui-detail-content">\t\t        \t\t\t\r\n\t\t        \t\t</table>\r\n\t\t        \t</td>\r\n\t\t        </tr>\r\n\t\t\t</tfoot>\r\n\t</table>\r\n\t<div>\r\n\t\t\t\u7b2c ')
        # SOURCE LINE 65
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \r\n\t\t\t<!-- if there is a previous page print a back link -->\r\n')
        # SOURCE LINE 67
        if paginator.has_previous:
            # SOURCE LINE 68
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\r\n')
        # SOURCE LINE 70
        __M_writer(u'            <!-- if there is a previous and a next page print a divider -->\r\n')
        # SOURCE LINE 71
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 72
            __M_writer(u'                  | \r\n')
        # SOURCE LINE 74
        __M_writer(u'            <!-- if there is a next page print a next link -->\r\n')
        # SOURCE LINE 75
        if paginator.has_next:
            # SOURCE LINE 76
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\r\n')
        # SOURCE LINE 78
        __M_writer(u'\t</div>\r\n</div>\r\n</div>\r\n\r\n\r\n\r\n\r\n<div id="modal1"  class="box">\r\n\t<div class="box-header">\r\n\t\t<h1>\u5e26\u5bbd\u64cd\u4f5c</h1>\r\n\t</div>\r\n\t<div class="box-content">\r\n\t\t<iframe src="about:blank" id="sl-product-frame"\r\n\t\t\tonresize="this.height=this.contentWindow.document.body.scrollHeight"\r\n\t\t\tstyle="padding: 0; margin:0; width:620px; height:380px; overflow:hidden;"\r\n\t\t\tframeBorder=0 scrolling=yes\r\n\t\t\tonload="this.height=this.contentWindow.document.body.scrollHeight"></iframe>\r\n\t\t\t\t\t\r\n\t\t\t\t\r\n\t\t<div class="action_bar"><a class="close button"><span class="ui-icon ui-icon-circle-close"></span>\u5173\u95ed</a></div>\t\t\t\t\r\n\t\t\t\t\t\r\n\t</div>\r\n</div>\r\n\r\n\r\n<script>\t\r\n\tfunction closeDialog(){\r\n\t\tsetTimeout(\'clozeDialog()\',1000);\t\t\r\n\t}\r\n\tfunction clozeDialog(){\r\n\t\t//$( "#dialog" ).dialog("close");\r\n\t\twindow.location.reload();\r\n\t}\r\n\t$(function(){\r\n\t\t$(\'a:contains("\u64cd\u4f5c")\').click(function(){\r\n\t\t\t$(\'#sl-product-frame\').attr(\'src\',\'/bandwidth?p_id=\'+$(this).parent().find(\'.cid\').val());\r\n\t\t\t//$( "#dialog" ).dialog("open");\t\t\r\n\t\t});\r\n\t\t$(\'#product tbody td:lt(9)\').click(function(){\t\t\r\n\t\t\t$.getJSON(\'/bandwidthlog?p_id=\'+$(this).parent().find(\'.cid\').val(), function(json){\r\n\t\t\t\tfor (i=0;i<json.orders.length;i++){\r\n\t\t\t\t   var tpl =tpl + \'<tr><td>\u5ba2\u6237\u540d\u79f0:</td><td>{0}</td><td>\u8fd0\u8425\u5546:</td><td>{1}</td><td>\u5e26\u5bbd:</td><td>{2}</td><td>\u5f00\u59cb\u65f6\u95f4:</td><td>{3}</td><td>\u7ed3\u675f\u65f6\u95f4:</td><td>{4}</td><td>\u72b6\u6001:</td><td>{5}</td></tr>\';\r\n\t\t\t\t   tpl=tpl.format(json.orders[i].cname,json.orders[i].oname,json.orders[i].bandwidth,json.orders[i].begin_at,json.orders[i].suspended_at,json.orders[i].status);\r\n\t\t\t\t}\r\n\t\t\t\t$(\'#ui-detail-content\').html(tpl);\r\n\t\t\t}); \t\t\t\r\n\t    }); \r\n\t});\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


