# -*- coding: utf-8 -*-
#6-14

from random import choice


yours = raw_input("please enter your choice:")
_choice = {'scissors':'1', 'stone':'2', 'cloth':'3'}
result = {'11':'draw', '22':'draw', '33':'draw', '12':'you win', '13':'you lose', '23':'you win',
'21':'you lose', '31':'you win', '32':'you lose'}

def win_lose(user) :
    computer_choice = choice(['scissors','stone','cloth'])
    print "the computer's choice is %s" %  computer_choice
    user_choice = _choice.pop(user)
    _result = _choice[computer_choice] + user_choice
    return result[_result]


print win_lose(yours)
