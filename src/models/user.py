# -*- coding: utf-8 -*-
'''
Created on 2012/2/22

@author: ishida
'''

from mongokit import Document
import datetime
import hashlib, re   
from db.mongo import Mongo  
import uuid 

'''
normalizes a username or email address
'''
def normalize(username):
    if not username :
        return None
    #allow legal email address
#    name = username.strip().lower()
#    name = re.sub(r'[^a-z0-9\\.\\@_\\-~#]+', '', username)
#    name = re.sub('\\s+', '_', name)
#    #don't allow $ and . because they screw up the db.
#    name = name.replace(".", "")
#    name = name.replace("$", "")
    return username;

@Mongo.db.connection.register
class User(Document):
    structure = {
                 '_id':unicode,
                 'email':unicode,
                 'roles':list,
                 'password':unicode,
                 'roletype':int,
                 'status':int,
                 'created_at':datetime.datetime,
                 'history' : {
                              'last_login' : datetime.datetime,
                              'num_logins' : long
                              },
                 'timezone':unicode,
                 'suspended_at':datetime.datetime,
                 }
    use_dot_notation = True
    
    @staticmethod
    def normalize(username):
        return normalize(username)
        
    
    @staticmethod
    def lookup(username):
        return Mongo.db.ui['users'].User.find_one({'_id' : normalize(username)})
    
    @staticmethod
    def getUsers(roletype):
        return [u for u in  Mongo.db.ui['users'].find({'roletype':roletype})]
        
    '''
    creates a new user instance. unsaved
    '''
    @staticmethod
    def instance(username, password, roletype):
        from views.decorators import route
        username = normalize(username)
        user = User()    
        roles = [role[0] for role in route.get_routes()]
        if roletype == 1:
            roles.remove('/manage')
            roles.remove('/custorm_add')
            roles.remove('/custorm_mod')
            roles.remove('/product')
        elif roletype == 2:
            roles.remove('/signup')
            roles.remove('/product')
        elif roletype == 3:
            roles.remove('/signup')
            roles.remove('/manage')
            roles.remove('/custorm_add')
            roles.remove('/custorm_mod')
        else :
            print 'there is something wrong'
        user.roletype = roletype
        user.roles = roles
        user.status= 0
        user['_id'] = username
        user.password = hashlib.sha1(password).hexdigest()
        user.created_at = datetime.datetime.now()
        user.history = {
                        'num_logins' : 0
                        }
        return user
    
    def add_role(self, role):
        if not self.get('roles', False):
            self['roles'] = []
        
        if role in self['roles'] :
            return
        self['roles'].append(role)
        
    def remove_role(self, role):
        if not self.get('roles', False):
            self['roles'] = []
        try :
            while True:
                self['roles'].remove(role)
        except :
            pass
        
    def has_role(self, role):
        if not self.get('roles', False):
            self['roles'] = []
        if isinstance(role, basestring):
            return role in self['roles']
        else:
            for r in role:
                if r in self['roles']:
                    return True
    
    def name(self):
        return self._id
    
    def get_timezone(self):
        tz = self.get('timezone', None)
        if tz :
            return tz
        return 'China/Bei_Jing'
                
    def is_suspended(self):
        if self.get('suspended_at', None) == None :
            return False
        return self.suspended_at < datetime.datetime.utcnow()
    
    @staticmethod  
    def updateUser(_id, status):
        Mongo.db.ui['users'].update({"_id":_id}, {'$set':{'status':status}})

