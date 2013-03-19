'''
Created on 2012-9-25

@author: huangchong
'''

import struct
import binascii

def data_to_binary(param):
    return binascii.hexlify(param)
    
def binary_to_data(param):
    return binascii.unhexlify(param)
  
    