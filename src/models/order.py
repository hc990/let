# -*- coding:utf-8 -*-
'''
Created on 2012-9-12

@author: huangchong
'''
from db.mongo import Mongo
from mongokit import Document
import datetime
import uuid

# @Mongo.db.connection.register
class Order(Document):    
    structure = {
                 '_id':unicode,
                 # 套餐类型
                 'otype':int,
                 'package_id':basestring,
                 # 交换机类型
                 'e_id':basestring,
                 # 端口号
                 'port':basestring,
                 # 操作状态 0未执行/1执行
                 'status':int,
                 # 创建时间
                 'created_at':datetime.datetime,
                 'ipAddress':basestring,
                 # 调整时间
                 'custom_time':datetime.datetime,
                 'bandwidth':int,
                 # 用户名
                 'u_id':basestring,
                 # 工单编号
                 'p_id':unicode
                 }

    use_dot_notation = True

    @staticmethod      
    def lookup(c_id):
        return Mongo.db.ui['orders'].find_one({'_id' : c_id})   
    
    @staticmethod
    def getOrders():
        return [u for u in Mongo.db.ui['orders'].find()]

    @staticmethod
    def get_working_orders(status,e_id):
        return Mongo.db.ui['orders'].find({'status':status,'e_id':e_id,"custom_time":{'$lte':datetime.datetime.now()}})
      
    @staticmethod
    def get_back_orders():
        return  Mongo.db.ui['orders'].find({'status' : 0 , "custom_time":{'$lte':datetime.datetime.now()}})
    
    @staticmethod
    def insert(bandwidth, package_id, e_id, otype, port, status, custom_time, created_at, ipAddress, u_id, p_id):
        o = Order.instance(bandwidth, package_id, e_id, otype, port, status, custom_time, created_at, ipAddress, \
                           u_id, p_id)
        return Mongo.db.ui['orders'].insert(o)
        
    @staticmethod
    def del_order(_cid, status):
        Mongo.db.ui['orders'].remove({"_id":uuid.UUID(_cid)})
          
    @staticmethod
    def finish_order(_cid):
        Mongo.db.ui['orders'].update({"_id":_cid}, {'$set':{'status':0}})  
        
    @staticmethod
    def withdraw_order(_pid):
        Mongo.db.ui['orders'].update({"p_id":uuid.UUID(_pid)}, {'$set':{'status':0}}, upsert=False, multi=True)  
              
    @staticmethod
    def active_order(_pid):
        Mongo.db.ui['orders'].update({'$and':[{"p_id":uuid.UUID(_pid), 'custom_time':{'$gte':datetime.datetime.now()}, }]}, \
                                     {'$set':{'status':1}}, upsert=False, multi=True)
    @staticmethod
    def back_order(_cid):  
        Mongo.db.ui['orders'].update({"_id":_cid}, {'$set':{'status':1}})    
        
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(bandwidth, package_id, e_id, otype, port, status, custom_time, created_at, ipAddress, u_id, p_id):
        o = Order()
        o['_id'] = uuid.uuid1()
        o.bandwidth = bandwidth
        o.package_id = package_id
        o.e_id = e_id  
        o.otype = otype
        o.port = port
        o.status = status
        o.custom_time = custom_time
        o.created_at = created_at
        o.ipAddress = ipAddress 
        o.p_id = p_id
        o.u_id = u_id
        return o
