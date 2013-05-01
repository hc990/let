from amqplib import client_0_8 as amqp



def sentMsg(information):
        conn = amqp.Connection(host="192.168.11.201:5672", userid="guest", password="guest", virtual_host="/", insist=False)
        chan = conn.channel()
        msg =amqp.Message(information)
        msg.properties["delivery_mode"] = 2
        chan.basic_publish(msg,exchange="sorting_room",routing_key="jason")
        
        chan.close()
        conn.close()
        