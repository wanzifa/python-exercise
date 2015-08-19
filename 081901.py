# 5-5

money = input('please input your money：')
a = float(money) * 100


num1 = a // 25
num2 = a % 25 //10
num3 = a % 25 % 10 // 5
num4 = a % 25 % 10 % 5


print '可以换 %d 个25美分，%d个10美分， %d个5美分 ，%d个11美分'\
      % (num1,num2,num3,num4)
    
