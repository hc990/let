'''
Created on 2012-9-25

@author: huangchong
'''
import telnetlib
def control_bandwidth(host,port,user,port,password,ex_bandwidth,now_bandwidth):
    tn = telnet_login(host,port,user,password)
    do_something(tn, 'en')
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    do_something(tn, 'conf t')
    do_something(tn, 'interface FastEthernet%s' % port)
    do_something(tn, str('no service-policy input %s' % ex_bandwidth))
    do_something(tn, 'service-policy input 5M' % now_bandwidth)
    do_something(tn, 'srr-queue bandwidth shape 20 20 20 20')
    do_something(tn, 'end')
    print 'end'
    end_telnet(tn)
    print tn.read_all()

#def telnet_login(host,port,user,password):
#    tn = telnetlib.Telnet(host)
#    if password:
#        tn.read_until("Password:")
#        tn.write(password + "\n")
#    return tn
#
#def do_something(tn,comm):
#    tn.write(comm+'\n')
#
#def end_telnet(tn):
#    tn.write("exit\n")

#if __name__ == '__main__':
#    control_bandwidth('211.147.81.50','','','cisco','')
   
        
        