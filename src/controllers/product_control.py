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
  
@route('/product')
class ProductHandler(BaseHandler):

    @authenticated
    @role_required('/product')
    def get(self):
        user = self.get_username()
        custormers = Custormer.getProducts(user)
        template_values = {}
        template_values['custormers'] = custormers
        self.render_template('/site/product.html', **template_values)