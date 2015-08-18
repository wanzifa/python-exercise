# -*- coding: utf-8 -*-
# 习题2-15

print ('please input 3 numbers:')


a = input('number1:')
b = input('number2:')
c = input('number3:')
sort = [a,b,c]

def sortabc(x):
    list.sort(x)
    return x


print 'from smallest to biggest:', sortabc(sort)[0], sortabc(sort)[1], sortabc(sort)[2]
print 'from smallest to biggest:', sortabc(sort)[2], sortabc(sort)[1], sortabc(sort)[0]
