# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1356321200.437
_enable_loop = True
_template_filename = 'E:\\workspacePY\\sod\\src/views/account/login.html'
_template_uri = '/account/login.html'
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
    return runtime._inherit_from(context, u'/layouts/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n    <link href="/static/css/jquery.motionCaptcha.0.2.css" rel="stylesheet" />\t\n\t<style type="text/css">\n\t\tbody{background:#231815;/*url(/static/images/bg.jpg);*/ color:#997e54; overflow:hidden; }\n\t\t.row{float:none; clear:both; zoom:1;}\n\t\t.divider{border-bottom:3px dotted #997e54; margin:5px 0;}\n\t</style>\n\t<form action="/login" method="post" id="login-form"> \t   \n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 13
        __M_writer(unicode(next))
        __M_writer(u'" />\n\t\t<div style="margin-left:auto; margin-right:auto; width:443px; height:238px; margin-top:150px; text-align:center;">\n\t\t\t<div class="row">\n\t\t\t\t<img src="/static/images/logo.gif" alt="logo" style="border:0; display:inline-block; " />\n\t\t\t\t<div class="pull-left" style="display:inline-block; vertical-align:middle; ">\u541b\u4f17\u7f51\u7edc\u7ba1\u7406\u7cfb\u7edf<br />\n\t\t\t\t\t<small style="font-size:10px;">version 1.0.0 beta</small>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="row divider"></div>\n\t\t\t<div class="row">\n\t\t\t\t\n\t\t\t\t<div style="float:left; text-align:left;  width:290px; ">\n\t\t\t\t\t<input type="text" id="username" name="username" style="border:0 none; background:url(/static/images/input.png) no-repeat; width:280px; height:35px; padding-left:80px; color:white; margin:5px 0;" />\n\t\t\t\t\t<input type="password" id="password" name="password" style="border:0 none; background:url(/static/images/input_pw.png) no-repeat; width:280px; height:35px; padding-left:80px; color:white;margin:5px 0;" />\n\t\t\t\t\t <div id="mc">\n\t\t\t\t\t   <canvas id="mc-canvas"></canvas>\n\t\t\t\t    </div>\n\t\t\t\t\t<div class="field">\n\t\t\t\t\t\t<label for="keep_logged_in"><input type="checkbox" name="keep_logged_in" id="keep_logged_in" /> \u4fdd\u6301\u6211\u7684\u767b\u5f55\u72b6\u6001</label>\n\t\t\t\t\t</div> \t\t  \t\t\t\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t<div style="float:left; vertical-align:middle; padding:30px 0;">\n\t\t\t\t    <input type="hidden" id="mc-action" value="/login" />\n\t\t\t\t\t<input type="image" disabled="disabled" src="/static/images/button.png" value="Login" style="-webkit-filter:grayscale(1);width:115px; height:30px; " />\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</form>\n\t\n\n\t<script type="text/javascript" src="/static/js/jquery.motionCaptcha.0.2.js"></script>\n\t<script>\n\t\twindow.onload = function(){  \n\t        try{  \n\t            document.createElement(\'canvas\').getContext(\'2d\');            \n\t        }catch(e){  \n\t            $(\'input[type="image"]\').attr(\'disabled\',false);\n\t        }  \n        }; \n\t\t$(\'#login-form\').motionCaptcha({\n\t\t\taction: \'#mc-action\',\n\t\t\tdivId: \'#mc\',\n\t\t\tcssClass: \'.mc-active\',\n\t\t\tcanvasId: \'#mc-canvas\',\n\t\t\tshapes: [\'triangle\', \'x\', \'rectangle\', \'circle\', \'check\', \'caret\', \'zigzag\', \'arrow\', \'leftbracket\', \'rightbracket\', \'v\', \'delete\', \'star\', \'pigtail\'],\n\t\t\terrorMsg: \'\u8bf7\u91cd\u8bd5\uff01\',\n\t\t\tsuccessMsg: \'success!\',\n\t\t\tnoCanvasMsg: "\u4f60tmd\u80fd\u6362\u4e2a\u6d4f\u89c8\u5668\u5417\uff1f - try Chrome, FF4, Safari or IE9.",\n\t\t\tlabel: \'<p>Please draw the shape in the box to submit the form:</p>\'\n\t\t});\t\t\t\t\n\t</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


