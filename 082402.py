# -*- coding: utf-8 -*-
#8-9

N = input('please input a number:')
list1 = [1,1]


def find(listn,n):
    for i in range(2,n):
        new = listn[i-1] + listn[i-2]
        listn.append(new)
    return new


print 'the number you want to find is %d' % find(list1,N)
