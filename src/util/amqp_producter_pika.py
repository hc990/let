import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
               '192.168.11.201'))
channel = connection.channel()

#channel.queue_declare(queue='task_queue',durable=True)
#channel.basic_publish(exchange='',
#                      routing_key='hello',
#                      body='Hello World!')
#print " [x] Sent 'Hello World!'"

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "  Fuck"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()