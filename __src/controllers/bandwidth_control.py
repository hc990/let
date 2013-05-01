'''
Created on 2013-3-11

@author: huangchong
'''


from core.basehandler import BaseHandler
from views.decorators import route 
from pysnmp.entity.rfc3413.oneliner import cmdgen  

  
@route('/widthchart')
class WidthChartHandler(BaseHandler):

    def get(self):
        cg = cmdgen.CommandGenerator()
        comm_data = cmdgen.CommunityData('jztec', 'jztec',)
        transport = cmdgen.UdpTransportTarget(('192.168.11.253', 161)) 
        variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 10) 
        errIndication, errStatus, errIndex, result = cg.nextCmd(comm_data, transport, variables)  
        variables = (1, 3, 6, 1, 2, 1, 2, 2, 1, 16) 
        errIndication, errStatus, errIndex, result = cg.nextCmd(comm_data, transport, variables) 
        template_values = {}    
        self.render_template('/site/width.html', **template_values)
        
        


        