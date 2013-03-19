'''
Created on 2012-9-12

@author: huangchong
'''
from mongokit import Document
import datetime
from db.mongo import Mongo
import uuid

  
@Mongo.db.connection.register
class Order(Document):    
    structure = {
                 '_id':unicode,
                 'p_id':unicode,
                 'cname':basestring,
                 'oname':basestring,
                 'status':int,
                 'percent':int,
                 'begin_at':datetime.datetime,
                 'suspended_at':datetime.datetime
                 }

    use_dot_notation = True

    @staticmethod      
    def lookup(c_id):
        return Mongo.db.ui['orders'].find_one({'_id' : c_id})
    
    @staticmethod
    def get_orders_operators(oname):
        return [u for u in Mongo.db.ui['orders'].find({'oname' : oname})]
    
    @staticmethod
    def get_orders(p_id):
        return {'orders':[{'cname':u['cname'],'percent':u['percent'],\
        'begin_at':u['begin_at'].strftime('%Y-%m-%d %H:%M') ,'suspended_at':u['suspended_at'].strftime('%Y-%m-%d %H:%M') ,'status':u['status'], \
        'oname':u['oname']
        } for u in Mongo.db.ui['orders'].find({'p_id' : p_id})]}
    
    @staticmethod
    def get_working_orders():
        return Mongo.db.ui['orders'].find()
    
#    @staticmethod
#    def get_working_orders():
#        return  Mongo.db.ui['orders'].find({'status' : 0,"begin_at":{'$lte':datetime.datetime.now()}})
    
    @staticmethod
    def get_back_orders():
        return  Mongo.db.ui['orders'].find({'status' : 1 ,"suspended_at":{'$gte':datetime.datetime.now()}})
 
    @staticmethod
    def insert(cname, oname, p_id, percent, begin_at, suspended_at):
        c = Order.instance(cname, oname, p_id, percent, begin_at, suspended_at)
        return Mongo.db.ui['orders'].insert(c)
        
    @staticmethod
    def del_order(_cid, status):
        Mongo.db.ui['orders'].remove({"_id":uuid.UUID(_cid)})
        
        
    @staticmethod
    def finish_order(_cid):
        Mongo.db.ui['orders'].update({"_id":_cid}, {'$set':{'status':1}})  
        
    @staticmethod
    def back_order(_cid):  
        Mongo.db.ui['orders'].update({"_id":_cid}, {'$set':{'status':2}})    
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(cname, oname, p_id, percent, begin_at, suspended_at):
        c = Order()
        c['_id'] = uuid.uuid1()
        c.cname = cname  
        c.oname = oname
        c.p_id = p_id
        c.status = 0
        c.percent = percent
        c.begin_at = begin_at
        c.suspended_at = suspended_at  
        return c
