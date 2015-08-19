# 5-16

Balance = input('please enter your primary money:')
payment = input('please enter your monthly payment:')
i=0


print '''         Amount Remaining
Pymt# Paid       Banlance
----- -----  ----------'''
print '''%d     $%.2f     $%f'''\
    % (i,payment,Balance)


while Balance > payment :
    i+=1
    Balance -= payment
    print '''%d     $%.2f     $%f'''\
    % (i,payment,Balance)


print '''%d     $%.2f     $0'''\
    % (i+1,Balance+payment)
