# -*- coding: utf-8 -*-
'''
Created on 2012-11-12

@author: huangchong
'''
import os.path
import json

# for read file
def read(pre_file_name):
    path,name = os.path.split(pre_file_name)
    if not os.path.exists(path):  
        os.mkdir(path)            
    if not os.path.exists(pre_file_name):  
        mkfile(pre_file_name)               
    with open(pre_file_name) as f:
        return f.readline()
    
# for write file
def write(arg,pre_file_name):
    file_path, file_name = os.path.split(pre_file_name)
    if not os.path.exists(file_path):  
        os.mkdir(file_path)                 
    with open(pre_file_name,"wt") as f:
        f.write(arg)  

def mkfile(filename, body=None):
    with open(filename, 'w' ) as f:
        f.write(body)
    return  

#def walk(dirname):
#    try:
#        for name in os.listdir(dirname):
#            path = os.path.join(dirname, name)
#            if os.path.isfile(path):
#                path,name =  os.path.split(path)
#                realname ,ext = os.path.splitext(name)
#                if ext == '.mkv':
#                    print path,'----',name      
#            else:
#                walk(path)   
#    except:
#        'wrong'   
#walk('d:\TDDOWNLOAD')


'''demo for telnet'''
#if read('e:/aa/huangchong.txt'):
#    b = json.loads(read('e:/aa/huangchong.txt'))
#b['192.168.0.3']=[u'admin7', u'admin8']  
#write(json.dumps(b),'e:/aa/','huangchong.txt')
#a,c = json.loads(read('e:/aa/huangchong.txt'))['192.168.0.5']

#try:
#  if read('e:/aa/','huangchong2.txt'):
#      username,password = json.loads(read('e:/aa/','huangchong.txt'))['192.168.0.5']
#else:  
#        response = "username or password error!!!"    
#   
#print response 
#fileadd ='e:/aa/bbbb.txt'
#b = {}
#if read(fileadd):
#    b = json.loads(read(fileadd))
#b['111'] = ['222', '33333']  
#print json.dumps(b)
#write(json.dumps(b), fileadd)
    
    