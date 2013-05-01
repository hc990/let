'''
Created on 2012-9-25

@author: huangchong
'''
import util.telnet_util as util

def control_bandwidth(host,port,user,password,id,bandwidth):
    tn = util.telnet_login(host,port,user,password)
    util.do_something(tn, 'enable')
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
        
        
    util.do_something(tn, 'interface GigabitEthernet1/0/9')
    util.do_something(tn, 'srr-queue bandwidth shape 5 5 5 5')
    util.do_something(tn, 'service-policy input 20M')
    util.do_something(tn, 'end')
    
    
    
#    util.do_something(tn, 'sys')
#    comm = 'vlan '+id
#    util.do_something(tn, comm)
#    comm = 'undo traffic-policy inbound'
#    util.do_something(tn, comm)
#    comm = 'traffic-policy '+bandwidth+'M inbound'
#    util.do_something(tn, comm)
#    comm ='undo traffic-policy outbound'
#    util.do_something(tn, comm)
#    comm = 'traffic-policy '+bandwidth+'M outbound'
#    util.do_something(tn, comm)
    util.end_telnet(tn)
    

if __name__ == '__main__':
    control_bandwidth('192.168.11.1',23,'','jztec','','')
        