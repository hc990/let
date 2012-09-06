'''
Created on 2012-8-30

@author: zongzong
'''

from pysnmp.entity.rfc3413.oneliner import cmdgen, ntforg
from pysnmp.proto.api import v3

sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), \
DisplayString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, \
255))).setMaxAccess("readwrite")
 




