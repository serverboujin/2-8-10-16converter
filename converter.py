# -*- coding: utf-8 -*-

import sys

print ('This is a converter')
i = raw_input('Please Enter a number which you would like to convert.>>')
f = raw_input('From?(2/8/10/16)>>')
if f == '2':
    pass
elif f == '8':
    pass
elif f == '10':
    pass
elif f == '16':
    pass
else:
    print ('Quit.')
    sys.exit()      #Interruption due to Invalid number
t = raw_input('To?(2/8/10/16)>>')
if t == '2':
    pass
elif t == '8':
    pass
elif t == '10':
    pass
elif t == '16':
    pass
else:
    print ('Quit.')     #Interruption due to Invalid number
    sys.exit()
if f == '2':
    if t == '2':
        print ('Quit.')     #Interruption due to bad request
        sys.exit()
    elif t == '8':
        print oct(int(i, 2))
    elif t == '10':
        print int(i, 2)
    elif t == '16':
        print hex(int(i, 2))
elif f == '8':
    if t == '2':
        print bin(int(i, 8))
    elif t == '8':
        print ('Quit.')     #Interruption due to bad request
        sys.exit()
    elif t == '10':
        print int(i, 8)
    elif t == '16':
        print hex(int(i, 8))
elif f == '10':
    if t == '2':
        print bin(int(i))
    elif t == '8':
        print oct(int(i))
    elif t == '10':
        print ('Quit.')     #Interruption due to bad request
        sys.exit()
    elif t == '16':
        print hex(int(i))
elif f == '16':
    if t == '2':
        print bin(int(i, 16))
    elif t == '8':
        print oct(int(i, 16))
    elif t == '10':
        print int(i, 16)
    elif t == '16':
        print ('Quit.')     #Interruption due to bad request
        sys.exit()
fin = raw_input()
