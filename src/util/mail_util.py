# -*- coding: utf-8 -*-
'''
Created on 2012-11-14

@author: huangchong
'''
import smtplib
import email.utils
from email.mime.text import MIMEText
from email.Header import Header
# Create the message

def sent_mail(title,message,cname,custorm_mail):
    msg = MIMEText(message,'plain','utf-8')
    msg.set_unixfrom('author')
    msg['To'] = email.utils.formataddr(((cname),
    custorm_mail))
    msg['From'] = email.utils.formataddr((title,
    'account@jztec.cn'))
    msg['Subject'] = Header(title,'utf-8')
    server = smtplib.SMTP()
    #server.connect('mail.jztec.cn','25')
    server.connect('192.168.11.77','25')
    try :
        server.ehlo()
        # If we can encrypt this session, do it
        if server.has_extn('STARTTLS'):
            server.starttls()  
            server.ehlo() # reidentify ourselves over TLS connection
        server.login("account", "1q@W#E$R")   
        server.sendmail('account@jztec.cn',  
        custorm_mail,
        msg.as_string())
    finally:
        server.quit()
        
