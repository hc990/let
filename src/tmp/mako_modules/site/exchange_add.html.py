# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1363162403.859
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/exchange_add.html'
_template_uri = '/site/exchange_add.html'
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
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<div class="box">\r\n\t<div class="box-header">\r\n\t\t<h1>\u6dfb\u52a0\u4ea4\u6362\u673a\u4fe1\u606f</h1>\r\n\t</div>\n<div class="box-content">\n<form action="/add_exchange" method="post" >\r\n<p>\r\n\t\t\t<label for="cname" class="label">\u4ea4\u6362\u673a\u540d\u79f0:</label>\r\n\t\t\t\t<input type="text" id="ename" name="ename" class="required" placeholder="\u5982\u4f55\u586b\u5199\u8bf7\u4e0e\u541b\u4f17\u516c\u53f8\u786e\u8ba4"  />\r\n</p>\r\n<p>\t\r\n\t\t\t<label for="ipAddress" class="label">IP\u5730\u5740:</label>\r\n\t\t\t\t<input type="text" id="ipAddress" name="ipAddress" placeholder="127.0.0.1"  />\r\n</p>\r\n<p>\r\n\t\t\t<label for="phonenum" class="label">\u7528\u6237\u540d:</label>  \r\n\t\t\t\t<input type="text" id="tusername" name="tusername" class="required"/>\r\n</p>\r\n<p>\r\n\t\t\t<label for="device" class="label">\u5bc6\u7801:</label>\r\n\t\t\t\t  <input type="password" id="tpassword" name="tpassword" class="required" />\r\n</p>\r\n<p>\r\n\t\t\t<label for="device" class="label">\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801:</label>\r\n\t\t\t\t <input type="password" id="tpassword2" name="tpassword2" class="required" />\r\n</p>\r\n<p>\r\n\t\t\t\t<input type="submit" class="button blue" value="\u6dfb\u52a0"/>   \r\n\t\t\t\t<input type="reset" class="button" value="\u91cd\u7f6e"/>\r\n\t</p>\r\n</form>\r\n</div>\t\t\t\t\r\n</div>\r\n<script type="text/javascript">\r\n $(function() {\r\n            $.validator.addMethod(\'IP4Checker\', function(value) {\r\n                var ip = /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;  \r\n                return ip.test(value);  \r\n            }, "Invalid IP address7");  \r\n        });\r\n/*$(\'#fileTab\').tabs({\r\n\t\tajaxOptions: {\r\n\t\t\terror: function( xhr, status, index, anchor ) {\r\n\t\t\t\t$( anchor.hash ).html("\u8be5\u9875\u65e0\u6cd5\u663e\u793a\uff0c\u6ca1\u6cd5\u534e\u4e3d\u626f\u6de1\uff01" );\r\n\t\t\t}\r\n\t\t},\r\n\t\tselect:function(obj,tab){\t\t\r\n\t\t\tvar subWeb = document.frames ? document.frames[tab.panel.id].document : document.getElementById(tab.panel.id).contentDocument;\r\n\t\t\tswitch(tab.panel.id)\r\n\t\t\t{\r\n\t\t\tcase "thisMonth":$(tab.panel).find(\'iframe\').attr(\'src\',\'/manage\');\r\n\t\t\t//$(tab.panel).find(\'iframe\').attr("height",subWeb.body.scrollHeight);break;\r\n\t\t\tdefault:$(tab.panel).find(\'iframe\').attr(\'src\',\'\');break;\r\n\t\t\t}\t\t\r\n\t\t}\r\n\t});*/\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


