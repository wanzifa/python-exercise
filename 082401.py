# -*- coding: cp936 -*-
#8-6

number = input('please input a number:')
list1 = []


def isprime(x):
    i = 0
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
            else:
                continue
    if i == x - 1:
        return True


def getfactors(x):
    for i in range(1,x):
        if x % i == 0:
            list1.append(i)


getfactors(number)


j = 0
while j < len(list1):
    isprime(list1[j])
    if isprime(list1[j]) == False:
        del list1[j]
    else:
        j += 1


sum = 1
for h in list1:
    sum = sum * h
if sum == number:
    pass
else:
    list1.append(number/sum)
    print list1
