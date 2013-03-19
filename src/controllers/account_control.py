# -*- coding: utf-8 -*-
from core.basehandler import BaseHandler
from db.mongo import Mongo
from models.user import User
import datetime, hashlib 
from tornado.web import authenticated
from views.decorators import route  
from tornado.web import asynchronous

@route('/')
class IndexHandler(BaseHandler):
    @asynchronous  
    def get(self):
        #template context variables go in here
        template_values = {}  
        self.render_template('/account/login.html', **template_values)

@route('/logout')     
class LogoutHandler(BaseHandler):
    def get(self):  
        self.session['username'] = None
        self.session.destroy()
        #kill the session.
        self.clear_all_cookies()
        self.redirect("/")

@route('/login')
class LoginHandler(BaseHandler):
    def get(self):
        if not self.get_secure_cookie('username'):
            username = self.get_secure_cookie('username')
            if username:
                user = User.lookup(username)
                if user:
                    self.session['username'] = user.username
                    self.session['locale'] = user.profile.locale
            self.redirect("/")    
        else:
            template_values = {}
            template_values['next'] = self.get_argument('next', '/')
            self.render_template('/account/login.html', **template_values)

    def post(self):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)     
        if not username or not password:   
            # do something
            self.flash.error = "You must enter a username and password to proceed. Please try again."
            self.session['flash'] = self.flash
            self.redirect("/login")
            return
        pw = hashlib.sha1(password).hexdigest()
        username = User.normalize(username)
        user = User.lookup(username)
        
        #check the password.
        if not user or user['password'] != pw:
            # do something
            self.flash.error = "Login not valid"
            self.redirect("/login")
            return
        
        # check if user is suspended.
        if user.is_suspended() :
            self.flash.error = "Sorry the account you specified has been suspended."
            self.redirect("/")
            return
          
        user.history.last_login = datetime.datetime.utcnow()
        Mongo.db.ui['users'].update({'_id': username}, {
                                                    '$set' : {'history.last_login': user.history.last_login},
                                                    '$inc' : {'history.num_logins' : 1}
                                                    })        
        #add to the session.
        self.session['username'] = user._id
#        if self.get_argument("keep_logged_in", False) == "on" :
        self.session['keep_logged_in'] = True    
        self.flash.notice = "Welcome, %s" % user._id  
        self.set_current_user(user)
        if user['roletype']==2:  
            self.redirect(u'/manage') 
        elif user['roletype']==3:
            self.redirect("/product")
        else:  
            self.redirect("/signup")
           
@route('/asy_login')
class AsyLoginHandler(BaseHandler):
         
    def _do_login(self, response):
        username = self.get_argument("username", None)
        password = self.get_argument("password", None)
        if not username or not password:
            # do something
            self.flash.error = "You must enter a username and password to proceed. Please try again."
            return 
        pw = hashlib.sha1(password).hexdigest()
        username = User.normalize(username)
        user = User.lookup(username)
        #check the password.
        if not user or user['password'] != pw:
            # do something
            self.flash.error = "Login not valid"
            return
        # check if user is suspended.
        if user.is_suspended() :
            self.flash.error = "Sorry the account you specified has been suspended."
            return    
        user.history.last_login = datetime.datetime.utcnow()
        Mongo.db.ui['users'].update({'_id': username}, {
                                                    '$set' : {'history.last_login': user.history.last_login},
                                                    '$inc' : {'history.num_logins' : 1}
                                                    })        
        #add to the session.
        self.session['username'] = user._id
        #check keep_logged_in
        if self.get_argument("keep_logged_in", False) == "on" :
            self.session['keep_logged_in'] = True
            
        self.set_current_user(user)
#        self.session['current_user']= user._id
        self.flash.notice = "Welcome, %s" % user._id
        self.write(username)
        self.finish("finished")
       
    @asynchronous  
    def post(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.asy_render_template(callback=self._do_login, **template_values)
    
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/account/login.html', **template_values)
              
@route('/pwdchange')
class PasswordChanger(BaseHandler):
    
    @authenticated
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/account/pwdchange.html', **template_values)
    
    @authenticated
    def post(self):
        pw = hashlib.sha1(self.get_argument("password")).hexdigest()
        if self.get_current_user()['password'] != pw:  
            # do something
            self.flash.error = "Password not valid, please try again"
            template_values = {}
            self.render_template('/account/pwdchange.html', **template_values)
            return
          
        newPw = self.get_argument('new_pw')
        newPw2 = self.get_argument('new_pw_again')
        if newPw != newPw2 :  
            self.flash.error = "Passwords do not match, please try again"
            template_values = {}
            self.render_template('/account/pwdchange.html', **template_values)
            return
        
        password = hashlib.sha1(newPw).hexdigest()
        Mongo.db.ui['users'].update({'_id': self.get_username()}, {
                                                    '$set' : {'password': password}
                                                    })       
        self.flash.success = "Successfully updated password"
        self.redirect('/')
        
@route('/signup')
class SignupHandler(BaseHandler):  
    
#    @authenticated
#    @role_required('/signup')
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/account/signup.html', **template_values)
    
#    @authenticated
#    @role_required('/signup')
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
        self.flash.info = "Successfully created account, please let them try."
        if roletype == '2':
            self.redirect("/get_users")  
        elif roletype == '1':  
            self.redirect("/get_admin")
