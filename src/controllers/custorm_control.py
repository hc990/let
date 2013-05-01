# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: zongzong
'''  
from core.basehandler import BaseHandler
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.product import Product
from models.order import Order
from views.paginator import Paginator
import json
import datetime


@route('/product')
class ProductHandler(BaseHandler):

    @authenticated
    @role_required('/product')
    def get(self):
        user = self.get_username()
        products = Product.getProduct(user)
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1    
        #get the document count param
        count = self.get_argument('count', 5)
        count = count if count >= 1 else 5
        paginator = Paginator(products, page, count, len(products))
        template_values = {}
        template_values['paginator'] = paginator
        self.render_template('/site/product.html', **template_values)
             
@route('/bandwidth')
class OrderHandler(BaseHandler):
    
    @authenticated
    def get(self):
        template_values = {}
        p_id = self.get_argument('p_id', '')  
        product = Product.lookup(p_id)
        template_values['p_id'] = product['_id'] 
        template_values['oname'] = product['oname']
        template_values['cname'] = product['cname'] 
        template_values['next'] = self.get_argument('next', '/')     
        self.render_template('/site/bandwidth.html', **template_values)
      
    @authenticated   
    def post(self):
        cname = self.get_argument("cname", None) 
        oname = self.get_argument("oname", None) 
        percent = self.get_argument("percent", None)   
        begin_at = datetime.datetime.strptime(self.get_argument("begin_at", None),"%m/%d/%Y %H:%M")
        suspended_at = datetime.datetime.strptime(self.get_argument("suspended_at", None),"%m/%d/%Y %H:%M")
        p_id = self.get_argument("p_id", None)  
        Order.insert(cname, oname, p_id, percent, begin_at, suspended_at) 
        self.finish("finished<script>parent.closeDialog();</script>")  
         
@route('/bandwidthlog')
class OrderLogsHandler(BaseHandler):
    
    @authenticated
    def get(self):
        p_id = self.get_argument("p_id", None)
        bandwidths = Order.get_orders(p_id)
        self.finish(json.dumps(bandwidths))  
      
    @authenticated 
    def post(self):
        p_id = self.get_argument("p_id", None)
        bandwidths = Order.get_orders(p_id)  
        self.finish(json.dumps(bandwidths))  
