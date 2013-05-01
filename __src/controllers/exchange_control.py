# -*- coding: utf-8 -*-
'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
from tornado.web import authenticated
from views.decorators import route
from models.exchange import Exchange
from client.rpc_client import TelnetRpcClient
from tornado.options import options 
import json
from views.paginator import Paginator 
from core.log import Log

@route('/get_exchanges')
class ExchangesHandler(BaseHandler):

    @authenticated
#    @role_required('/get_exchanges')
    def get(self): 
        oname = self.get_username()
        template_values = {}
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1
        #get the document count param
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10
        exchanges = Exchange.get_exchanges(oname)
        paginator = Paginator(exchanges, page, count, len(exchanges))
        template_values['paginator'] = paginator
        template_values['status'] = ''
        self.render_template('/site/exchange.html', **template_values)

    @authenticated
#    @role_required('/get_exchanges')
    def post(self):
        oname = self.get_username()
        ename = self.get_argument("ename", None)
        status = self.get_argument("status", None)  
        template_values = {}
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1
        #get the document count param
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10
        if status is not None:
            template_values['status'] = status
        else:
            template_values['status'] = ''
        exchanges = Exchange.get_condition_exchanges(oname,ename,template_values['status'])
        paginator = Paginator(exchanges, page, count, len(exchanges))
        template_values['paginator'] = paginator
        template_values['ename'] = ename
        self.render_template('/site/exchange.html', **template_values)#/site/bandwidth.html
        
@route('/add_exchange')
class AddExchangeHandler(BaseHandler):
    
    @authenticated
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/site/exchange_add.html', **template_values)
    
    @authenticated
    def post(self):  
        oname = self.get_username()
        ipAddress = self.get_argument("ipAddress", None)
        ename = self.get_argument("ename", None)
        tusername = self.get_argument("tusername", None)
        tpassword = self.get_argument("tpassword", None)
        if not tusername or not tpassword:
            # do something
            self.flash.error = "You must enter a username and password to proceed. Please try again."
            self.redirect("/add_exchange")
            return
        
        if tpassword != self.get_argument("tpassword2", None) :
            self.flash.error = "Passwords do not match. Please try again."
            self.redirect("/add_exchange")
            return
        Exchange.insert(ename,oname,ipAddress)
        rpc = TelnetRpcClient(options.service_ip)
        msg = json.dumps({'fileadd':options.telnet_key_dir, \
                                                    'ipadd':ipAddress,'username':tusername,"password":tpassword})
        from util import encrypt_util  
        encoded = encrypt_util.encode(msg)
        response = rpc.call("key_queue",encoded)
        Log.info(response)
        ##加密传输入保存
        self.redirect("/get_exchanges")     
    
@route('/exchange_del')
class DelExchangeHandler(BaseHandler):

    def post(self):
        _cid = self.get_argument("e_id", None)
        Exchange.updateExchange(_cid, 0)  
        self.finish("finished")  
    
@route('/exchange_active')
class ActiveExchangeHandler(BaseHandler):

    def post(self):
        _cid = self.get_argument("e_id", None)
        Exchange.updateExchange(_cid, 1)  
        self.finish("finished")
        
@route('/exchange_up')
class ExchangeChange(BaseHandler):
    
    @authenticated
    def get(self):
        template_values = {}
#        template_values['next'] = self.get_argument('next', '/')
        e_id = self.get_argument('e_id')  
        e = Exchange.lookup(e_id)
        print e
        template_values['exchange'] = e
        self.render_template('/site/exchange_update.html', **template_values)
    
    @authenticated
    def post(self):   
        e_id = self.get_argument('e_id')
        e = Exchange.lookup(e_id)
        tusername = self.get_argument('username')
        newPw = self.get_argument('new_pw')
        newPw2 = self.get_argument('new_pw_again')
        if newPw != newPw2 :
            self.flash.error = "Passwords do not match, please try again"
            self.redirect("/exchange_up")
            return
        tpassword =newPw  
        rpc = TelnetRpcClient(options.service_ip)
        msg = json.dumps({'fileadd':options.telnet_key_dir,'ipadd':e['ipAddress'],'username':tusername,"password":tpassword})
        from util import encrypt_util
        encoded = encrypt_util.encode(msg)
        response = rpc.call("key_queue",encoded)
        Log.info(response)
        self.flash.success = "Successfully updated password"
        self.redirect('/exchange_up')       
        

@route('/update_exchange_ip')
class UpdateExchangeIp(BaseHandler):
    
    @authenticated
    def post(self):   
        e_id = self.get_argument('e_id')
        ip = self.get_argument('ip')
        Exchange.updateExchangeIp(e_id,ip)
        self.finish("success")
        