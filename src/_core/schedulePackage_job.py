# -*- coding: utf-8 -*-
'''
Created on 2012-11-8
 
@author: huangchong
'''
from _pydev_log import Log
from apscheduler.scheduler import Scheduler
from client.rpc_client import TelnetRpcClient
from config import options_setup, options_setup
from core.scheduler import JzScheduler
from db.mongo import Mongo
from models import package
from models.exchange import Exchange
from models.order import Order
from models.package import Package
from models.product import Product
# from models.user import User
from pysnmp.entity.rfc3413.oneliner import cmdgen
from tornado.options import define, define, options
from util import encrypt_util
import datetime
import json
import logging
import string
import sys
import time
import uuid
# from client.rpc_client import TelnetRpcClient
'''  
cron jobs 
'''
 
def job_function():    
    print '[x] Requesting'
    print 'set_bandwidth_job start at ', datetime.datetime.now()
            
def job_package():
#       Log.info("请异步发送")
        need_do = ''
        orders = Order.get_working_orders()
        for order in orders:
            product = Product.lookup(order['p_id'])
            exchange = Exchange.get_exchange(order['e_id'])
            packages = Package.getPackageByName(order['package_id'])
            for package in packages:
                need_do = need_do+json.dumps({'port':product['port'],'bandwidth':order['bandwidth'],\
                           'status':order['status'],'port_name':product['port'], 'ipAddress':exchange['ipAddress'], \
                          'package_id':package['package_name']})
#             Order.finish_order(order['_id'])   
                                
        need_back=''
        orders = Order.get_back_orders()
        for order in orders:
             custom_time = order['custom_time']
             product = Product.lookup(order['p_id'])
             exchange = Exchange.look(order['e_id'])
             packages = Package.getPackageByName(order['package_id'])
             for package in packages:
                 need_back = need_back+json.dumps({'port':product['port'],'ex_bandwidth':order['bandwidth'],\
                           'status':order['status'],'port_name':product['port'], 'ipAddress':exchange['ipAddress'], \
                          'package_id':package['package_name']})
#              Order.back_order(order['_id'])
        print 'set_package_job end at ',datetime.datetime.now()
                                
#         orders = {}   
#         flag = False  
#         if(need_do!=''):
#             orders['need_do']=need_do
#             flag = True
#         if(need_back!=''):
#             orders['need_back']=need_back
#             flag = True
#         if(flag!=True):
#             rpc = TelnetRpcClient(options.service_ip)
#             encoded = encrypt_util.encode(str(orders))
#             response = rpc.call("rpc_queue",encoded)                    
                               
      
def dss_jobsPackage():  
    logging.error("")    
    sche = JzScheduler()
    sche.add_interval_job(job_package,minutes=30)
    sche.start()
   
if __name__ == '__main__':    
    Mongo.create(host='192.168.11.111', port=27017)
    dss_jobsPackage()