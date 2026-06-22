"""
age = int(input())
country = input().upper()
marks = int(input())
if age<=18 and country=='INDIA':
    print('Indian Child')
elif 18<age<=60 and country=='INDIAN':
    print('Indian Adult')
elif age>60 and country=='INDIAN':
    print('Indian Senior')

result='Pass' if marks>35 else fail
print('Result:',result)
"""
"""
country = input().upper()
age = int(input())
if country=='INDIA':
    if age<=18:
        print('Indian Minor')
    elif 18<age<=60:
        print('Indian Adult')
    elif age>60:
        print('Indian Senior')
elif country=='FOREIGN':
    if age<=18:
        print('Foreign Minor')
    elif 18<age<=60:
        print('Foreign Adult')
    elif age>60:
        print('Foreign Senior')
"""
"""
number = int(input('Enter a number: '))
if number>0:
    print('Number is Positive')
    if number%2==0:
        print('Number is even')
    elif number%2!=0:
        print('Number is odd')
elif number<0:
    print('Number is Negative')
elif number==0:
    print('Number is Zero')
"""
"""
age = int(input('Enter your age: '))
if age>18:
    print('Ticket price is Rs.200')
elif 12<age<=18:
    print('Ticket price is Rs.150')
elif age<=12:
    print('Ticket price is Rs.100')
"""
"""
marks = int(input('Enter your marks: '))
attendence = int(input('Enter your attendence: '))
if marks>=35 and attendence>=75:
    print('Pass')
else:
    if marks<35:
        print('Failed because of less marks')
    elif marks>35:
        print('Failed beacuse of less attendence')
"""
number = int(input('Enter a number: '))
result='Even' if number%2==0 else 'Odd'
print(result)