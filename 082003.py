## -*- coding: utf-8 -*-
#6-11

import string
ip_primary = raw_input('please enter your ip:')


def change(x) :
    a = x[:3]
    b = x[3:6]
    c = x[6:9]
    d = x[9:12]
    ip2 = [a, b, c, d]
    ip ='.'.join(ip2)
    return ip


print change(ip_primary)


list1 = change(ip_primary).split('.')
ip_contrary_list = list1[::-1]
ip_contrary = '.'.join(ip_contrary_list)


print ip_contrary
