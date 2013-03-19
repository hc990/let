'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
from db.mongo import Mongo
import datetime, hashlib
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.customer import Custormer
from models.user import User


@route('/get_users')
class UserHandler(BaseHandler):

    @authenticated
    @role_required('/get_users')
    def post(self):
        name = self.get_arguments("name", False)
        type = self.get_arguments("type", False)
        
        template_values = {}
        template_values['users'] = User.getUsers(2)
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_users')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(2)
        self.render_template('/site/users.html', **template_values)
        
@route('/get_admin')
class AdminHandler(BaseHandler):

    @authenticated
    @role_required('/get_admin')
    def post(self):
        name = self.get_arguments("name", False)
        type = self.get_arguments("type", False)
        
        template_values = {}
        template_values['users'] = User.getUsers(1)
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_admin')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(1)
        self.render_template('/site/users.html', **template_values)

@route('/signup')
class SignupHandler(BaseHandler):
    
    @authenticated
    @role_required('/signup')
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        
        self.render_template('/account/signup.html', **template_values)
    
    
    
    @authenticated
    @role_required('/signup')
    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        roletype = self.get_argument("roletype", None)

        if not username or not password:
            # do something
            self.flash.error = "You must enter a username and password to proceed. Please try again."
            self.redirect("/signup")
            return
        
        if password != self.get_argument("password2", None) :
            self.flash.error = "Passwords do not match. Please try again."
            self.redirect("/signup")
            return
        
        user = User.instance(username, password, int(roletype))
        Mongo.db.ui['users'].insert(user)
        self.flash.info = "Successfully created your account, please log in."
        self.redirect("/login")
        
        
        
        
        
