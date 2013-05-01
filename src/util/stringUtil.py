'''
Created on 2012-3-15

@author: zongzong
'''

"""
No.1
"""
from tornado.options import options
import string
print u"\u2020"
notrans = string.maketrans('', '')

"""
"""
def containAny(astr, strset):
    return len(strset) != len(strset.translate(notrans, astr))    
    
def containALl(astr, strset):
    return not strset.translate(notrans, astr)

def translator(frm='', to='', delete='', keep=None):
    if(len(to) == 1):
        to = to * len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allchars = string.maketrans(frm, to)
        delete = allchars.translate(allchars, keep.translate(allchars, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate

if __name__ == "__main__":
    fun = translator('a', 'c', 'd', 'v')
    print fun('aa vbvv  vccccc  dd')
