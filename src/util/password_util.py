# -*- coding: utf-8 -*-
#!/usr/bin/python

#charsets={
#"a":"abcdefghijklmnopqrstuvwxyz",\
#"A":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",\
#"0":"0123456789",\
#"$":"^!\"$%&/()=?{[]}+*~#'-_.:,;<>|\\ "\
#}
#
#def GeneratePassword(length=5,charset="aA0"):
#    password="";lc="";charset_string=""
#    for c in charset:
#        if c in charsets.keys():
#            charset_string+=charsets[c]
#    while len(password)<length:  
#        c=urandom(1) 
#        if c in charset_string and c!=lc:
#            password+=c;lc=c
#    return password
  
import string ,random 
pass_gen = lambda length, ascii =  (string.letters) + string.digits + string.punctuation: \
       ("".join([list(set(ascii))[random.randint(0,len(list(set(ascii)))-1)] for i in range(length)]))
       
       
#if __name__=="__main__":
#    print GeneratePassword(15,"aA0")
