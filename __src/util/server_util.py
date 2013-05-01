'''
Created on 2012-9-24

@author: huangchong
'''
'''
Created on 2012-9-24

@author: huangchong
'''


# work as an client for henlian.co
# the imformation u should give me 
# 
#
#
import socket
import sys
class Server(): 
    
    @staticmethod
    def create_server(ip,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server=(ip,port)  
        sock.bind(socket_server)
        return sock   
    
    @staticmethod
    def receive_message(sock):
        # Listen for incoming connections
        sock.listen(1)
        while True:          
            connection, client_address = sock.accept()
            try:
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    print data
                    if data:
                        #do something
                        connection.sendall(data)
                    else:
                        break
            finally:
                # Clean up the connection
                connection.close()


if __name__ == '__main__':
        sock = Server.create_server('127.0.0.1',10000)
        Server.receive_message(sock)
    



        