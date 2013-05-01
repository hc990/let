'''
Created on 2013-2-28

@author: huangchong
'''
import telnetlib
import time
import threading

def telnet_login(host, username, password):
    tn = telnetlib.Telnet(str(host))
    if username:
        tn.read_until("Username:")
        tn.write(str(username) + "\n")
    if password:
        tn.read_until("Password:")
        tn.write(str(password) + "\n")
    return tn

def do_something(tn, comm):
    tn.write(comm + '\n')
    
def worker(data):
    tn = telnet_login("192.168.11.250","","jztec")
    do_something(tn,"en")
    tn.read_until("Password:")
    tn.write("jztec" + "\n")  
    do_something(tn,"configure terminal")
    print "interface GigabitEthernet1/%s" % data
    do_something(tn,"interface GigabitEthernet1/%s" % data)
    do_something(tn,"service-policy input rate-limit")
    do_something(tn,"service-policy output rate-limit")
    time.sleep(1)
    do_something(tn,"exit")



threads = []
for i in range(3):
    threads.append(threading.Thread(target=worker,args=(i+1,)))
for t in threads:
    t.start()
for t in threads:
    t.join()     
print "finish"


