# -*- coding: utf-8 -*-
# 8-12

begining = input('please enter the begining number:')
end = input('please enter the end number:')


if end < 33:
    print '''DEC    BIN    OCT    HEX
------------------------'''
    for i in range(begining, end+1):
        print '%d     %d     %o     %x' % (i, eval(bin(i)), eval(oct(i)), eval(hex(i)))

else:
    print '''DEC    BIN    OCT    HEX    ASCII
---------------------------------'''
    for i in range(begining, 33):
        print '%d     %o     %d     %d' % (i, eval(bin(i)), eval(oct(i)), eval(hex(i)))
    for i in range(33, end):
        print '%d     %d     %d     %d     %c' % (i, eval(bin(i)), eval(oct(i)), eval(hex(i)), i)
