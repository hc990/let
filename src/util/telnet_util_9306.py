'''
Created on 2012-9-25

@author: huangchong
'''
import telnetlib
def control_bandwidth(host,port,user,password):
    tn = telnet_login(host,port,user,password)
    do_something(tn, 'en')
    if user:
        tn.read_until("username:")
        tn.write(user + "\n")
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    do_something(tn, 'system-view')
    do_something(tn, 'vlan 74')
    do_something(tn,'undo traffic-policy inbound')
    do_something(tn,'traffic-policy 2M  inbound')
    do_something(tn,'undo traffic-policy outbound')
    do_something(tn,'traffic-policy 2M outbound ')
    print 'end'
    end_telnet(tn)
    print tn.read_all()  

def telnet_login(host,port,user,password):
    tn = telnetlib.Telnet(host)
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    return tn

def do_something(tn,comm):
    tn.write(comm+'\n')

def end_telnet(tn):
    tn.write("quit\n")

if __name__ == '__main__':
    control_bandwidth('124.74.8.110','','peifeng_qian','S93hap&com=)^We*','')
   
        
        