from amqplib import client_0_8 as amqp
import sys  
import json

conn = amqp.Connection(host="211.147.71.42:5672", userid="guest", password="guest", virtual_host="/", insist=False)
chan = conn.channel()

imformation = {'bandwidth':20,'port':'1/0/9'}
msg =amqp.Message(json.dumps(imformation))

msg.properties["delivery_mode"] = 2
chan.basic_publish(msg,exchange="sorting_room",routing_key="jason")

chan.close()
conn.close()