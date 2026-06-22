"""
name = "Pasagadugula Balaganesh"
print(name.upper())
print(name.lower())
print(name.strip())
new_name = name.replace('Balaganesh','Siddhu')
print(new_name)
print(name.split())
first , last = name.split()
print(last)
print(name.count('a'))
print(name.title())
nickname = "Siddhu"
age = 18
print('My name is {} and I am {} years old.'.format(nickname,age))
"""
message = " hello, world "
print(message.strip().title())
line = "my name is pasagadugula balaganesh"
print(line.title())
fruit = 'banana'
print(fruit.count("a"))
message = "I love Java Programming."
print(message.replace('Java','Python'))
s = "apple,banana,mango,orange,kiwi"
fruits = s.split(",")
print(fruits)
for fruit in fruits: print(fruit)
name = "Siddhu"
age = 18
CGPA = 9.27
print(f'Name:{name} | Age:{age} | CGPA:{CGPA}')