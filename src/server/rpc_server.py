# -*- coding: utf-8 -*-
import pika
import json
from file_util import read
import socket
from util import encrypt_util  

#key_file = '/home/junzhong/keys/jz_keys'
key_file = 'e:/keys/jz_keys.txt'

#localIP = socket.gethostbyname(socket.gethostname())

localIP = "192.168.11.201"

connection = pika.BlockingConnection(pika.ConnectionParameters(
        localIP))
    
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def do_command(switch_name, host , port_name, username, password, bandwidth):  
    tm = switch_name(host, port_name, username, password, bandwidth)
    tm.set_bandwidth()
    return json.dumps({'response_code':'250'})#成功
    
def on_request(ch, method, props, body):     
    try:
        if read(key_file):
            keys = json.loads(encrypt_util.decode(body)) 
            host = keys['host']   
            username, password = json.loads(read(key_file))[host]#here is the switch address 
            switch_name = keys['switch_name']       
            port_name = keys['port_name']     
            bandwidth = keys['bandwidth']  
            vlan = keys['vlan']  
            response = do_command(switch_name, host, vlan, username, password, bandwidth)    
            print "拯救地球 !!!"
        else:
            response = json.dumps({'response_code':'4587'})#密码错
    except:
            response = json.dumps({'response_code':'4588'})#操作错
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=\
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print " [x] Awaiting RPC requests"
channel.start_consuming()
  





                










