'''
Created on 2012-11-8

@author: huangchong
'''
from core.singleton import Singleton  
from apscheduler.scheduler import Scheduler
'''
    Singleton
'''
class JzScheduler(Singleton): 

    '''
        Accessor for ui specific database.
    '''   
    def __init__(self,**kwargs):
        self.schedudler = Scheduler(daemonic = kwargs['daemonic'])  