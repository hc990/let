'''
Created on 2013-3-12
Description: About Package model defining and Mondodb data control 
@author: Administrator
'''
# -*- coding: utf-8 -*-

from mongokit import Document
import datetime
import hashlib, re   
from db.mongo import Mongo  
import uuid
    
'''
normalizes a username or email address
'''

# @Mongo.db.connection.register
class Package(Document):
    structure = {
                 '_id':unicode,
                 'avail_timelong':int,
                 'avail_begintime':int,
                 'avail_endtime':int,
                 'is_weekday':int,
                 'lifecycle': int,
                 'created_at':datetime.datetime,
                 'status':int
                }
    
    use_dot_notation = True

    @staticmethod  
    def lookup(_id):
        return  Mongo.db.ui.package.find_one({'_id' : _id})

    @staticmethod  
    def getPackages():
        #return [u for u in Mongo.db.ui.package.find({'status':1}).sort({'package_name':-1})] 
        return [u for u in Mongo.db.ui.package.find({'status':1})] 
    
    @staticmethod 
    def getallPackages():
        return [u for u in Mongo.db.ui.package.find()]  
          
    @staticmethod 
    def getPackageByName(package_name): 
        return  [u for u in Mongo.db.ui.package.find({'_id':package_name})]
    
    @staticmethod 
    def getPackageByCondition(package_name,status):                      
        return [u for u in Mongo.db.ui.package.find({'_id':package_name,'status':status})]
    
    @staticmethod
    def getPackageByStatus(status):
        return [u for u in Mongo.db.ui.package.find({'status':status})]
                                                   
    @staticmethod
    def insert(p):
        return Mongo.db.ui['package'].insert(p)
       
    @staticmethod
    def delPackage(_package_name):
        Mongo.db.ui['package'].remove({"_id": _package_name})
    
    @staticmethod    
    def activePackage(package_name):
        Mongo.db.ui['package'].update({"_id":package_name}, {"$set":{"status":1}})
    
    @staticmethod    
    def logoffPackage(package_name):
        Mongo.db.ui['package'].update({"_id":package_name}, {"$set":{"status":0}})
        
    @staticmethod    
    def updatePackage(p):
        Mongo.db.ui['package'].update({"_id":p._id}, {'$set': {
                                                               "avail_timelong":p.avail_timelong,
                                                               "avail_begintime":p.avail_begintime,
                                                               "avail_endtime":p.avail_endtime,
                                                               "is_weekday":p.is_weekday,
                                                               "created_at":p.created_at}})

        

