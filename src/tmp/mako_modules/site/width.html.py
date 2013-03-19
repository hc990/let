# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1362995621.531
_enable_loop = True
_template_filename = 'E:\\workspacePY\\bandwidth\\src/views/site/width.html'
_template_uri = '/site/width.html'
_source_encoding = 'utf-8'
from views.filters import Cycler,Filters
_exports = ['body']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<style>\r\n')
        # SOURCE LINE 97
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<!DOCTYPE HTML>\r\n<html>\r\n\t<head>\r\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\r\n\t\t<title>\u6d41\u91cf\u5206\u6790\u56fe</title>\r\n\t\t<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>\r\n<script type="text/javascript">\r\n$(function () {\r\n    var chart;\r\n    var date  = new Date(2013, 01, 01, 00, 00, 00, 00);\r\n    $(document).ready(function() {\r\n        chart = new Highcharts.Chart({\r\n            chart: {\r\n                renderTo: \'container\',\r\n                type: \'area\'\r\n            },\r\n            title: {\r\n                text: \'\u4ea4\u6362\u673a\u6d41\u91cf\u5206\u6790\u56fe\'\r\n            },\r\n            subtitle: {\r\n                text: \'\u4ea4\u6362\u673aip\u5730\u5740\uff1a\'\r\n            },\r\n            xAxis: {\r\n                labels: {\r\n                    formatter: function() {\r\n                        return this.value; // clean, unformatted number for year\r\n                    }\r\n                }\r\n            },\r\n            yAxis: {\r\n                title: {\r\n                    text: \'\u4ea4\u6362\u673a\u6d41\u91cf\u5206\u6790\'\r\n                },\r\n                labels: {\r\n                    formatter: function() {\r\n                        return this.value / 1024+\'k\';\r\n                    }\r\n                }\r\n            },\r\n            tooltip: {\r\n                formatter: function() {\r\n                    return \'\u65f6\u95f4\u4e3a\'+this.x+ \'\'+this.series.name +\'\'+\r\n                        Highcharts.numberFormat(this.y, 0) +\'</b><br/>\u6d41\u91cf\u4e3a \';\r\n                }\r\n            },\r\n           \r\n            plotOptions: {\r\n                area: {\r\n                    pointStart: date.getYear()+date.getDay(),\r\n                    pointInterval:200,\r\n                    marker: {\r\n                        enabled: false,\r\n                        symbol: \'circle\',\r\n                        radius: 2,\r\n                        states: { \r\n                            hover: {\r\n                                enabled: true\r\n                            }\r\n                        }\r\n                    }\r\n                }\r\n            },\r\n            series: [{\r\n                name: \'\u8f93\u5165\u6d41\u91cf\',\r\n                data: [null, null, null, null, null, 6 , 11, 32, 110, 235, 369, 640,\r\n                    1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126,\r\n                    27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662,\r\n                    26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,\r\n                    24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586,\r\n                    22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950,\r\n                    10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104 ]\r\n            }, {\r\n                name: \'\u8f93\u51fa\u6d41\u91cf\', \r\n                data: [null, null, null, null, null, null, null , null , null ,null,\r\n                5, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322,\r\n                4238, 5221, 6129, 7089, 8339, 9399, 10538, 11643, 13092, 14478,\r\n                15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049,\r\n                33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000,\r\n                35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,\r\n                21000, 20000, 19000, 18000, 18000, 17000, 16000]\r\n            }]\r\n        });\r\n    });\r\n    \r\n});\r\n</script>\r\n</head>\r\n\t<body>\r\n<script src="http://code.highcharts.com/highcharts.js"></script>\r\n<script src="http://code.highcharts.com/modules/exporting.js"></script>\r\n<div id="container" style="min-width: 400px; height: 400px; margin: 0 auto"></div>\r\n\t</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


