"""
i=1
while i<11:
    print(i,end=' ')
    i+=1
"""
"""
secret=7
while True:
    guess=int(input('Enter your guess: '))
    if guess>secret:
        print('Too High')
    elif guess<secret:
        print('Too Low')
    else:
        print('Your guess is right!')
        break
"""
"""
count = 0
while True:
    number=int(input('Enter a positive number: '))
    count+=number
    if number<0 or number==0:
        breakex
print(count)
"""
"""
i=10
while i<=10:
    print(f'Countdown: {i}')
    i-=1
    if i==0:
        print('Blast offf!')
        break
"""
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    print()
    i+=1
