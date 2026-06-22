"""
#FIZZBUZZ
for i in range(1,31):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0:
        print('Buzz')
        continue
    print(i)
"""
"""
str = 'Python'
i=5
while i>=0:
    print(str[i],end='')
    i-=1
"""
"""
i=1
while i<=10:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1
"""
for num in range(2,51):
    prime = True 
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num)