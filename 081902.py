#5-6

expression = raw_input('please enter your expression:')


list1 = expression.split(' ')
a = float(list1[0])
b = list1[1]
c = float(list1[2])

        
def calculate(a,b,c) :
    if b == '+' :
        return a + c
    elif b == '-' :
        return a - c
    elif b == '*' :
        return a * c
    elif b == '/' :
        return a / c
    elif b == '%'  :
        return a % c
    elif b == '**' :
        return a ** c

x = calculate(a, b, c)
print '%s = %f' % (expression, x)
