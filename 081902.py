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
    else:
    # 如果只是做题，可以不加这个处理，但在实际项目中要考虑周全
    # 对任何用户输入的情况都要考虑到
    # 而且不要相信任何用户的输入（尤其是在表单中）
        return "请输入正确的操作符！"


x = calculate(a, b, c)
print '%s = %f' % (expression, x)
