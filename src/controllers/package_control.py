'''
Created on 2013-3-13
Description: This is about package post and get function
@author: Kelly
'''
from core.basehandler import BaseHandler
from tornado.web import authenticated
from views.decorators import route
from models.package import Package
from client.rpc_client import TelnetRpcClient
from tornado.options import options 
import json
from views.paginator import Paginator 
from core.log import Log
import datetime
#from ubuntuone.storageprotocol import request

import tornado.httpserver
import tornado.httputil

@route('/insert_package')
class InsertPackageHandler(BaseHandler):  
    
    @authenticated
    def get(self): 
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/site/insertPackage.html', **template_values)
        
        
    @authenticated
    def post(self):
        p = Package()
        p._id = self.get_argument("package_name", None)
        p.avail_timelong = int(self.get_argument("avail_timelong", None))
        p.avail_begintime = int(self.get_argument("avail_begintime", None))
        avail_endtime =  self.get_argument("avail_endtime1", None)
        if avail_endtime:
            p.avail_endtime = int(avail_endtime)
        else:
            p.avail_endtime = 0
        '''
        if avail_endhour <= avail_beginhour:
            p.effective_length = avail_endhour+24 - avail_beginhour
        else:
            p.effective_length = avail_endhour - avail_beginhour
        '''
 
        '''
        p.avail_begintime =  datetime.datetime.strptime(self.get_argument("avail_begintime", None), "%H:%M")
        p.avail_endtime =  datetime.datetime.strptime(self.get_argument("avail_endtime", None),"%H:%M")
        
        avail_beginhourstr =  self.get_argument("avail_begintime", None)
        nPos1 =avail_beginhourstr.index(':')
        avail_beginhour = int(avail_beginhourstr[0:nPos1])
     
        avail_endhourstr =  self.get_argument("avail_endtime", None)
        nPos2 =avail_endhourstr.index(':')
        avail_endhour = int(avail_endhourstr[0:nPos2])
        
        if avail_endhour <= avail_beginhour:
            p.effective_length = avail_endhour+24 - avail_beginhour
        else:
            p.effective_length = avail_endhour - avail_beginhour
        '''
        #p.avail_begintime =  datetime.datetime.strptime(avail_begintime+':00', "%H:%M")
        #p.avail_endtime =  datetime.datetime.strptime(avail_endtime+':00',"%H:%M")
        #print  p.avail_begintime, p.avail_endtime
        p.is_weekday = int(self.get_argument("is_weekday", None))
        p.lifecycle = 1
        p.created_at = datetime.datetime.now()
        p.status = 1
        #p.uname = self.get_username()   
        p.insert(p)
        self.redirect("/get_packages") 


@route('/get_packages')
class SearchPackageHandler(BaseHandler):  
    
    @authenticated
    def get(self):
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10     
        packages = Package.getPackages()                 
        paginator = Paginator(packages, page, count, len(packages))
        template_values = {}
        template_values['paginator'] = paginator
        self.render_template('/site/searchPackage.html', **template_values)
     
    @authenticated    
    def post(self):  
        package_name = self.get_argument("package_name", None)
        status = self.get_argument("status", None)
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10
        template_values = {}
        if package_name is not None:
            if status is not None and status != '':
                packages = Package.getPackageByCondition(package_name, int(status))
                template_values['status'] = int(status)
            else:
                print package_name
                packages = Package.getPackageByName(package_name)
                print packages
                template_values['status'] = ''  
        else:
            if status is not None and status != '':
                packages = Package.getPackageByStatus(int(status))
                template_values['status'] = int(status)  
            else:
                packages = Package.getallPackages()
                template_values['status'] = ''  
        #create a Paginator object
        paginator = Paginator(packages, page, count, len(packages))
        template_values['_id'] = package_name
        template_values['paginator'] = paginator
        self.render_template('/site/searchPackage.html', **template_values)
              
        
@route('/update_package')        
class UpdatePackageHandler(BaseHandler):
    
    @authenticated
    def get(self):

        package_name = self.get_argument('package_name')
        package = Package.getPackageByName(package_name)
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1
        #get the document count param
        count = self.get_argument('count', 10)
        count = count if count >= 1 else 10
        paginator = Paginator(package, page, count, len(package))
        template_values = {}
        template_values['paginator'] = paginator
        template_values['next'] = self.get_argument('next','/')
        self.render_template('/site/updatePackage.html',**template_values)
  
    @authenticated  
    def post(self):
        
        p = Package()
        p._id = self.get_argument('package_name')
        package = Package.lookup(p._id)
        p.avail_timelong = int(self.get_argument('avail_timelong', package['avail_timelong']))
        p.avail_begintime = int(self.get_argument("avail_begintime", package['avail_begintime']))
        p.avail_endtime =  int(self.get_argument("avail_endtime1", package['avail_endtime']))
        #p.avail_begintime =  datetime.datetime.strptime(avail_begintime+':00', "%H:%M")
        #p.avail_endtime =  datetime.datetime.strptime(avail_endtime+':00',"%H:%M")
        '''
        p.pname = self.get_argument('package_name')
        p.avail_timelong = int(self.get_argument('avail_timelong'))
        p.avail_begintime = datetime.datetime.strptime(self.get_argument("avail_begintime"), "%H:%M")
        p.avail_endtime = datetime.datetime.strptime(self.get_argument("avail_endtime"), "%H:%M")
        
        avail_beginhourstr =  self.get_argument("avail_begintime", None)
        nPos1 =avail_beginhourstr.index(':')
        avail_beginhour = int(avail_beginhourstr[0:nPos1])
     
        avail_endhourstr =  self.get_argument("avail_endtime", None)
        nPos2 =avail_endhourstr.index(':')
        avail_endhour = int(avail_endhourstr[0:nPos2])
        
        if avail_endhour <= avail_beginhour:
            p.effective_length = avail_endhour+24 - avail_beginhour
        else:
            p.effective_length = avail_endhour - avail_beginhour
        '''
        p.is_weekday= int(self.get_argument("is_weekday", package['is_weekday']))
        p.created_at = datetime.datetime.now()
        Package.updatePackage(p)
        self.redirect("/get_packages")
        

@route('/delPackage')
class DelPackage(BaseHandler):
    
    def post(self):
        _package_name = self.get_argument("package_name", None)
        uname = self.get_username()
        Package.delPackage(_package_name)  
        self.finish("finished") 
        
    
@route('/active_package')
class ActivePackageHandler(BaseHandler):

    def post(self):
        package_name = self.get_argument("package_name", None)  
        Package.activePackage(package_name)  
        self.finish("finished")    
    
@route('/logoff_package')
class LogoffPackageHandler(BaseHandler):

    def post(self):
        package_name = self.get_argument("package_name", None)
        Package.logoffPackage(package_name)  
        self.finish("finished")
        
        