'''
Created on 2012-9-25

@author: huangchong
'''
import telnetlib
import time

def control_bandwidth(host,port,username,password,p_id,bandwidth):
    tn = telnet_login(host,port,username,password)
    do_something(tn, 'system')
    time.sleep(2)
    do_something(tn, 'interface e1/0/1')
    time.sleep(1)
    do_something(tn, 'line-rate inbound 81920')
    time.sleep(1)
    do_something(tn, 'line-rate outbound 81920')
    end_telnet(tn)

def telnet_login(host,port,username,password):
    tn = telnetlib.Telnet(host)
    if username:
        tn.read_until("Username:")
        tn.write(username + "\n")
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    return tn

def do_something(tn,comm):
    tn.write(comm+'\n')
  
def end_telnet(tn):
    tn.write("quit\n")
    tn.write("quit\n")

if __name__ == '__main__': 
    control_bandwidth('211.147.81.50','','admin','admin','e1/0/1','8192')
   
        
        