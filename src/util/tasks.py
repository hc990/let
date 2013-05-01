'''
Created on 2012-11-20

@author: huangchong
'''
from celery import Celery


celery = Celery('tasks',backend='amqp', broker='amqp://guest:guest@192.168.11.177//')
@celery.task
def add(x, y):
    return x + y


from tasks import add

result=add.delay(4, 4)

print result
print result.ready()
print result.get(timeout=1)