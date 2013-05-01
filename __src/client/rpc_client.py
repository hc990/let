'''
Created on 2012-11-5

@author: huangchong
'''
import pika
import uuid
import json

class TelnetRpcClient(object):
    
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host))
        self.channel = self.connection.channel()  
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
            
    def call(self,routing_key, params):
        self.response = None  
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',  
                                   routing_key=routing_key,
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id,
                                         ),
                                   body=params)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

'''demo for use it'''
#rpc = TelnetRpcClient('211.147.71.42')
#print " [x] Requesting from rpc"
#response = rpc.call(json.dumps({'switch_name':'TelnetManage3560', 
#                                "port_name":"e1/0/1", "host":"211.147.71.41", "bandwidth":2}))
#print " [.] Got %r" % (response,)
