'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.user import User  

@route('/get_users')
class OperatersHandler(BaseHandler):

    @authenticated
    @role_required('/get_users')
    def post(self): 
        template_values = {}
        template_values['users'] = User.getUsers(2)
        template_values['usertype']=2
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_users')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(2)  
        template_values['usertype']=2
        self.render_template('/site/users.html', **template_values)
        
@route('/get_admin')
class AdministratorsHandler(BaseHandler):

    @authenticated
    @role_required('/get_admin')
    def post(self):
        template_values = {}
        template_values['users'] = User.getUsers(1)
        template_values['usertype']=1
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_admin')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(1)
        template_values['usertype']=1
        self.render_template('/site/users.html', **template_values)
  
@route('/user_del')
class DelUserHandler(BaseHandler):
    def post(self):
        _id = self.get_argument("u_id", None)
        User.updateUser(_id,1)
        self.finish("finished")    
    
@route('/user_active')
class ActiveUserHandler(BaseHandler):
    def post(self):
        _id = self.get_argument("u_id", None)
        User.updateUser(_id,0)
        self.finish("finished")  
        
        
        