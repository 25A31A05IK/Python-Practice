"""
#Leap year
year = int(input('Enter the year: '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print('Leap year')
else:
    print('Not a leap year')
"""
"""
password = input('Enter the password: ')
if len(password)>8 and any(ch.isdigit() for ch in password):
    print('Valid')
else:
    print('Invalid')
""" 
"""
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1>0 and number_2>0 and number_3>0:
    print('All are positive')
elif number_1>0 or number_2>0 or number_3>0:
    print('Atleast one is positive')
else:
    print('No number is positive')
"""
"""
age = int(input())
citizen = input()
criminal = input()
if age>18 and citizen=='yes' and criminal=='no':
    print('Eligible')
else:
    print('Not Eligible')
"""
