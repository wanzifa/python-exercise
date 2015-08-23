# -*- coding: utf-8 -*-
#7-10

string = raw_input('please input a string:')


def change(x):
    stringlist = list(x)
    for i in range(len(x)) :
        if 65<=ord(stringlist[i])<78 or 97<=ord(stringlist[i])<110:
            stringlist[i] = chr(ord(stringlist[i])+13)
        elif 66<=ord(stringlist[i])<91 or 110<=ord(stringlist[i])<123:
            stringlist[i] = chr(ord(stringlist[i])-13)
    stringchanged = ''.join(stringlist)
    return stringchanged


print 'the result is %s' % change(string)
