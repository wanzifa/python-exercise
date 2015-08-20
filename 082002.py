# -*- coding: utf-8 -*-
#6-8

number = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninty',
100: 'one hundred', 200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred',
700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}


enter_number = input('please input a number between 0 and 1000:')


def change(x):
    if len(str(x)) == 1:
        return number[x]
    elif len(str(x)) == 2 :
        a = x // 10 * 10
        b = x % 10
        if b != 0:
            return number[a] + '-' + number[b]
        else :
            return number[x]
    elif len(str(x)) == 3 :
        a = x // 100 *100
        b = (x - a) // 10 * 10
        c = x % 10
        if b != 0 :
            return number[a] + ' and ' + number[b] + '-' + number[c]
        else :
            return number[a] + ' and ' + number[c]


print change(enter_number)
