# 1.Create x=10 globally. Create a function that prints x. Call it. Does it print 10?
x = 10
def num():
    print(x)
num()

# 2.Create a function that creates y=5 locally. After calling the function, try to print y outside. What error?
def local():
    y=5
local()
print(y)

# 3.Use the "global" keyword: create count=0 globally. Write increment() that adds 1 each call. Call 5 times.
count = 0
def increment():
    global count
    count+=1
    print(count)
increment()
increment()
increment()
increment()
increment()

# 4.Predict the output: x=5 → def f(): x=10 → f() → print(x). Run it. Why is x still 5?
x = 5
def f():
    x=10
f()
print(x)

# 5.Create a function login_count that tracks how many times users log in using a global variable.
count=0
def login_count():
    global count
    count+=1
    print(f'Number of times logged in: {count}')
login_count()
login_count()
login_count()
login_count()
login_count()