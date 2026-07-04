# 1.Rewrite your Day 16 add() and multiply() functions to use return instead of print. Store result in a variable
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
print(add(3,4),multiply(3,4))

# 2.Write max_of_three(a, b, c) that RETURNS the largest of 3 numbers (do not use max() built-in)
def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(max_of_three(100,50,40))

# 3.Write calculate_area(length, width) that returns area. Write calculate_perimeter too. Call both.
def area(length,breadth):
    return length*breadth
def perimeter(length,breadth):
    return 2*(length+breadth)
print(area(2,3),perimeter(2,3))

# 4.Write is_prime(n) that returns True if prime, False otherwise. Test with 2, 7, 9, 13, 15.
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(2))

# 5.Write a function that returns TWO values: min and max of a list. Capture both: mn, mx = minmax(nums).
def minmax(x):
    return min(x),max(x)
x = [1,2,3]
print(minmax(x))