'''
Created on 2012-12-14

@author: huangchong
'''

from pika.adapters.tornado_connection import TornadoConnection

class PikaClient(object):
    def connect(self):
        self.connection = TornadoConnection(on_connected_callback=self.on_connected)

# Create our Tornado Application
application = tornado.web.Application([
    (r"/", ExampleHandler)
], **settings)

# Create our Pika Client
application.pika = PikaClient()

# Start the HTTPServer
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8080)

# Get a handle to the instance of IOLoop
ioloop = tornado.ioloop.IOLoop.instance()

# Add our Pika connect to the IOLoop since we loop on ioloop.start
ioloop.add_timeout(500, application.pika.connect)

# Start the IOLoop
ioloop.start()