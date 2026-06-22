"""
name = input()
age = input()
college = input()
city = input()
print('       *Profile Card*       ')
print(f'Name:{name}')
print(f'Age:{age}')
print(f'College:{college}')
print(f'City:{city}')
"""
"""
str = input()
print(len(str), str[0], str[-1], str[::-1], str.upper())
"""
"""
name = input()
for i in range(len(name)): 
    print(f'Index {i}:{name[i]}')
"""
"""
number_1 = int(input('Enter number_1: '))
number_2 = int(input('Enter number_2: '))
operator = input('Enter your operator: ')
if operator=='+': print(number_1+number_2)
elif operator=='-': print(number_1-number_2)
elif operator=='*' : print(number_1*number_2)
elif operator=='/' : print(number_1/number_2)
"""
"""
temp = float(input('Enter temperatre: '))
unit = input('Is the temperatute is in C / F?').upper()
if unit=='C': 
    F=temp*(9/5)+32 
    print(F)
elif unit=='F': 
    C=(temp-32)*5/9 
    print(C)
"""