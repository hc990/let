'''
Created on 2012-11-28

@author: huangchong
'''
'''
Created on 2012-9-12

@author: huangchong
'''
from mongokit import Document
import datetime
from db.mongo import Mongo
import uuid
  
#@Mongo.db.connection.register
class Exchange(Document):   
     
    use_dot_notation = True
     
    structure = {
                 '_id':unicode,
                 'ename':basestring,
                 'oname':basestring,
                 'elogo':basestring,
                 'etype':basestring,
                 'status':int,
                 'ipAddress':basestring,
                 'created_at':datetime.datetime
                 }
    
    @staticmethod  
    def lookup(e_id):
        return Mongo.db.ui.exchanges.find_one({'_id' : uuid.UUID(e_id)})
    
#     @staticmethod  
#     def look(e_id):
#         return Mongo.db.ui.exchanges.find_one({'_id' : e_id})
    
    
    @staticmethod  
    def get_exchange(e_id):
        return Mongo.db.ui.exchanges.find_one({'_id' : e_id})
    
    @staticmethod  
    def get_exchanges(oname):
        return [u for u in Mongo.db.ui.exchanges.find({'oname' : oname})] 
    
    
    @staticmethod  
    def get_active_exchanges(oname,status):
        return [u for u in Mongo.db.ui.exchanges.find({'oname' : oname,'status':int(status)})] 
    
    @staticmethod  
    def get_status_exchanges(status):
        return [u for u in Mongo.db.ui.exchanges.find({'status':int(status)})] 
    
    @staticmethod  
    def get_condition_exchanges(oname,ename,status):
        e = Exchange()
        if oname:
            e.oname = oname
        if ename:
            e.ename = ename
        if status:
            e.status = status
            return [u for u in Mongo.db.ui.exchanges.find({'ename':{'$regex':e.ename}, 'oname' : oname,'status':int(e.status)})] 
        else:
            return [u for u in Mongo.db.ui.exchanges.find({'ename':{'$regex':e.ename},'oname' : oname})] 
        
        
    @staticmethod
    def insert(ename,oname,ipAddress,elogo,etype):
        c = Exchange.instance(ename,oname,1,elogo,etype,ipAddress,datetime.datetime.now())
        return Mongo.db.ui['exchanges'].insert(c)  
            
    @staticmethod
    def updateExchange(_eid, status):
        Mongo.db.ui['exchanges'].update({"_id":uuid.UUID(_eid)}, {'$set':{'status':status}})  
        
        
    @staticmethod
    def updateExchangeIp(_eid, ip):
        Mongo.db.ui['exchanges'].update({"_id":uuid.UUID(_eid)}, {'$set':{'ipAddress':ip}})  
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(ename,oname,status,elogo,etype,ipAddress,created_at):
        c = Exchange()
        c['_id'] = uuid.uuid1()
        c.ename = ename
        c.oname = oname
        c.status = status
        c.elogo = elogo
        c.etype = etype          
        c.ipAddress = ipAddress
        c.created_at = created_at
        return c