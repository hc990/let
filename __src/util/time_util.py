'''
Created on 2012-10-15

@author: huangchong
@summary: timer for close the telnet commands
'''

import time
import threading

class Timer(threading.Thread):
        def __init__(self, seconds):
                self.runTime = seconds
                threading.Thread.__init__(self)
        def run(self):
                time.sleep(self.runTime)
                print "Buzzzz!! Time's up!"

class CountDownTimer(Timer):
        def run(self):
                counter = self.runTime
                for sec in range(self.runTime):
                        print counter
                        time.sleep(1.0)
                        counter -= 1
                print "Done"

class CountDownExec(CountDownTimer):
        """
        a timer that execute an action at the end of the timer run.
        """
        def __init__(self, seconds, action, args=[]):
                self.args = args
                self.action = action
                CountDownTimer.__init__(self, seconds)
        def run(self):
                CountDownTimer.run(self)
                self.action(self.args)
                
                
def myAction(args=[]):
        """
        action demo
        """
        print "Performing my action with args:"
        print args


"""
  demo
"""      
if __name__ == "__main__":
        t = CountDownExec(3, myAction, ["hello", "world"])
        t.start()