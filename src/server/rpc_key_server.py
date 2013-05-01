# -*- coding: utf-8 -*-
import pika
import json
from file_util import read, write
import socket  
from encrypt_util import decode
localIP = socket.gethostbyname(socket.gethostname())
#localIP = "192.168.11.201"

connection = pika.BlockingConnection(pika.ConnectionParameters(
        localIP))
channel = connection.channel()
channel.queue_declare(queue='key_queue')

def do_command(fileadd, ipadd, username, password):
    keys={}
    if read(fileadd):
        keys = json.loads(read(fileadd))
    keys[ipadd] = [username, password]
    write(json.dumps(keys), fileadd)
    return json.dumps({'response_code':'250'})#成功
    
def on_request(ch, method, props, body):     
    try:
            msgs = decode(body)
            keys = json.loads(str.rstrip(msgs))
            fileadd = keys['fileadd']
            ipadd = keys['ipadd']
            username = keys['username']  
            password = keys['password']
            response = do_command(fileadd , ipadd, username, password)
            print "拯救地球 !!!"
    except Exception,e:
            print  "[Error]: ", e
            response = json.dumps({'response_code':'1748'})#操作错          
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=\
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='key_queue')
print " [x] Awaiting RPC requests"
channel.start_consuming()
