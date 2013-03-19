# -*- coding: utf-8 -*-
'''
Created on 2012-10-17

@author: huangchong
'''
from core.basehandler import BaseHandler
from views.decorators import route 
from models.order import Order
from views.paginator import Paginator
       
@route('/bwstat')
class BwStatHandler(BaseHandler):  
    
    def get(self):
        oname = self.get_current_user()['_id']
        
        bandwidths = Order.get_orders_operators(oname)
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count', 5)
        count = count if count >= 1 else 5
        paginator = Paginator(bandwidths, page, count, len(bandwidths))
        template_values={}
        template_values['paginator'] = paginator
        self.render_template('/site/stat_bw.html', **template_values)
      
    def post(self):
        oname = self.get_current_user()['_id']
        
        bandwidths = Order.get_orders_operators(oname)
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count', 5)  
        count = count if count >= 1 else 5
        paginator = Paginator(bandwidths, page, count, len(bandwidths))
        template_values={}
        template_values['paginator'] = paginator
        self.render_template('/site/stat_bw.html', **template_values)