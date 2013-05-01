from amqplib import client_0_8 as amqp  




conn = amqp.Connection(host="192.168.11.201:5672", userid="guest", password="guest", virtual_host="/", insist=False)
channel = conn.channel()

#bing exchange with queue
channel.queue_declare(queue="po_box", durable=True, exclusive=True, auto_delete=True)
channel.exchange_declare(exchange="sorting_room", type="direct", durable=True, auto_delete=True)
channel.queue_bind(queue="po_box", exchange="sorting_room", routing_key="jason")





def recv_callback(msg): 
    print 'Received: ' + msg.body + ' from channel #' + str(msg.channel.channel_id) 

#chan.basic_consume(queue='po_box', no_ack=True, callback=recv_callback, consumer_tag="testtag")
#while True:
#    chan.wait()
#chan.basic_cancel("testtag")
#
#chan.close()
#conn.close()
