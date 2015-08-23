# -*- coding: utf-8 -*-
#7-14&&7-13
import random

a =[]
b =[]


def change(x):
    for i in range(10):
        plus=random.randrange(0,9)
        x.append(plus)
    X = set(x)
    return X


A = change(a)
B = change(b)


#(去掉#即为第一问)print  A.union(B)
#(去掉#即为第一问)print A.intersection(B)


j=0
while j<3:
    guess1 = input('please enter a guessed set of A|B:')
    guess2 = input('please enter a guessed set of A&B：')
    if guess1 == A.union(B) and guess2 == A.intersection(B):
        print "you are right"
        break
    else:
        j = j+1
        continue

if j == 3:
    print 'A|B is %s ,A&B is %s' % (A.union(B),A.intersection(B))
