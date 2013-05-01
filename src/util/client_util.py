'''
Created on 2012-9-24

@author: huangchong
'''


# work as an client for henlian.co
# the imformation u should give me 
# 
#
#
#import socket
#import sys
#class Client(): 
#    
#    data = 0
#    
#    @staticmethod
#    def create_client(ip,port):
#        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#        socket_server=(ip,port)
#        sock.connect(socket_server)
#        return sock  
#    
#    @staticmethod
#    def send_message(sock,message):
#        try:
#            sock.sendall(message)
#            # Receive the data in small chunks and retransmit it
#    
#            data = sock.recv(16)
#        finally:
#                # Clean up the connection
#            sock.close()
#
#if __name__ == '__main__':
#        socket = Client.create_client('127.0.0.1',10000)
#        Client.send_message(socket)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print fib(4)



        