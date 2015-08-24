

# 这行代码太长，可以用'''str'''
print '''
    please input 5 numbers and choose one of those choices:
        plus(show you the sum of the 5 numbers)
        average(show you the average of the five numbers)
        exit(exit this program)')
'''


a = input ('please input number1:')
b = input ('please input number2:')
c = input ('please input number3:')
d = input ('please input number4:')
e = input ('please input number5:')
userchoice = raw_input('please input your choice:')


if userchoice == 'plus' :
    print 'the sum of the 5 numbers is:', a + b + c + d + e
elif userchoice == 'average' :
    print 'the average of the 5 numbers is:', (a + b + c + d + e) / 5
elif userchoice == 'exit' :
    exit()
