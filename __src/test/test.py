'''
Created on 2013-2-28

@author: huangchong
'''
import tornado.web, tornado.httpserver, tornado.ioloop, tornado.options
from tornado.options import options
from config import options_setup
import sys, os

        #parse the app config
tornado.options.parse_config_file('E:/workspacePY/bandwidth/src/config/settings.py')  
        #parse the command line args
tornado.options.parse_command_line() 


from db.mongo import Mongo

Mongo.create(host=options.db_host, port=options.db_port)

from models.order import Order 
from models.product import Product  
from models.exchange import Exchange 
from client.rpc_client import TelnetRpcClient    

import json,datetime
from util import encrypt_util


rpc = TelnetRpcClient(options.service_ip)   
need_do = ''

orders = Order.get_working_orders()
for order in orders:    
    product = Product.lookup(order['p_id'])
    exchange = Exchange.lookup(product['e_id'])  
    need_do = need_do+json.dumps({'switch_name':exchange['ename'],"vlan":product['port'], \
                    "port_name":product['port'], "host":exchange['ipAddress'], \
                    "bandwidth":order['bandwidth'],"flag":1})
    Order.finish_order(order['_id'])         
need_back=''
orders = Order.get_back_orders()
for order in orders:
    product = Product.lookup(order['p_id'])
    exchange = Exchange.lookup(product['e_id'])
    need_back = need_back+json.dumps({'switch_name':exchange['ename'],"vlan":product['port'], \
                    "port_name":product['port'], "host":exchange['ipAddress'], \
                    "bandwidth":order['bandwidth'],"flag":0})
    Order.back_order(order['_id'])

orders = {"1":need_do,"0":need_back}  
encoded = encrypt_util.encode(str(orders))
response = rpc.call("rpc_queue",encoded)

print response
#        rpc = TelnetRpcClient('192.168.0.2')
#        orders = Order.get_working_orders()
#        for order in orders:
#            product = Product.lookup(order['p_id'])
#            exchange = Exchange.lookup(product['e_id']) 
#            response = rpc.call(json.dumps({'switch_name':'TelnetManage3560', "vlan":product['vlan'],
#                            "port_name":product['port'], "host":exchange['ipAddress'], "bandwidth":product['ctype']*order['percent']/100}))
print 'set_bandwidth_job end at ', datetime.datetime.now()