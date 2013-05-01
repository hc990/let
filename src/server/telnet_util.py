import telnetlib
'''
Created on 2012-9-25
@author: huangchong
'''
class TelnetManage:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.tn = telnet_login(host, username, password)
        print 'telnet username: %s ' % self.username
        
    def login(self, host, username, password):
        pass
              
# interface FastEthernet0/10
# description testport
# srr-queue bandwidth shape 13 13 13 13
# service-policy input 8M
# end
class TelnetManage3560(TelnetManage):
    def __init__(self, host, username, password, values):
        TelnetManage.__init__(self, host, None, password)
#         self.login(self, self.host , self.username, self.password)
        self.values = values;
        print 'TelnetManage3560: ', self.host

    def set_bandwidth(self):
        do_something(self.tn, 'en')
        if self.password:
            self.tn.read_until("Password:")
            self.tn.write(self.password + "\n")   
        for value in self.values:
            bwvalue = 100 / self.bandwidth
            ex_bandwidth = int(value['ex_bandwidth'])
            portname = value['port_name']
            bandwidth = value['bandwidth']
            do_something(self.tn, 'conf t')
            do_something(self.tn, 'interface FastEthernet%s' % portname)
            do_something(self.tn, str('no service-policy input %sM' % ex_bandwidth))
            do_something(self.tn, 'service-policy input %sM ' % bandwidth)
            do_something(self.tn, 'srr-queue bandwidth shape %s %s %s %s' % (bwvalue, bwvalue, bwvalue, bwvalue))
            print 'bandwidth: s% ' % bandwidth
        do_something(self.tn, 'end')
        do_something(self.tn, "exit")
             
             
class TelnetManage3600(TelnetManage):
    def __init__(self, host , username, password, values):
        TelnetManage.__init__(self, host, username, password)
#         self.login(self, self.host , self.username, self.password)
        self.values = values
        print 'TelnetManage3600: ', self.host

    def set_bandwidth(self):
        for value in self.values:
            inbound = value['bandwidth'] * 1024
            outbound = value['bandwidth'] * 1024  
            portname = value['port_name']
            do_something(self.tn, 'system')
            do_something(self.tn, 'interface ', portname)
            do_something(self.tn, 'line-rate inbound ', inbound)
            do_something(self.tn, 'line-rate outbound ', outbound)
            print 'bandwidth: ', inbound  
        do_something(self.tn, "exit")
        
        
class Cisco4991(TelnetManage):
    def __init__(self, host, port_name, username, password, bandwidth,ex_bandwidth):
        TelnetManage.__init__(self, host, port_name, None, password)
        self.bandwidth = bandwidth
        self.ex_bandwidth = ex_bandwidth
        print 'Cisco4991: ', self.host

    def set_bandwidth(self):
        TelnetManage.set_bandwidth(self, self.host , self.username, self.password)
        do_something(self.tn, 'enable')
        if self.password:
            self.tn.read_until("Password:")
            self.tn.write(self.password + "\n")   
        do_something(self.tn, 'configure terminal')  
        do_something(self.tn, 'interface gigabitEthernet %s' % self.port_name)
        do_something(self.tn, 'no service-policy input %sM' % self.ex_bandwidth)
        do_something(self.tn, 'service-policy input %sM ' % self.bandwidth)
        do_something(self.tn, 'no service-policy output %sM' % self.ex_bandwidth)
        do_something(self.tn, 'service-policy output %sM ' % self.bandwidth)
        do_something(self.tn, 'end')      
        do_something(self.tn, 'exit')   
        print 'bandwidth: s% ' % self.bandwidth

class Cisco9306(TelnetManage):
    def __init__(self, host, port_name, username, password, bandwidth):
        TelnetManage.__init__(self, host, port_name, username, password)
        self.bandwidth = bandwidth
        self.host = host
        self.vlan = port_name
        print 'TelnetManage9306: ', self.host

    def set_bandwidth(self):  
        TelnetManage.set_bandwidth(self, self.host , self.username, self.password)
        do_something(self.tn, 'system-view')
        do_something(self.tn, 'vlan %s' % str(self.vlan))
        do_something(self.tn, 'undo traffic-policy inbound')
        do_something(self.tn, 'traffic-policy %sM  inbound' % self.bandwidth)
        do_something(self.tn, 'undo traffic-policy outbound')
        do_something(self.tn, 'traffic-policy %sM outbound ' % self.bandwidth)
        do_something(self.tn, "quit")
        print 'bandwidth: ', self.bandwidth    

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
