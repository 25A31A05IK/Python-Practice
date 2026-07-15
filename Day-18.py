# 1.Write greet(name, message="Hello") — calling greet("Ravi") uses default, greet("Ravi","Hi") overrides
def greet(name,message='Hello'):
    print(f'{message} {name}')
greet('Siddhu')
greet('Siddhu','Hi')

# 2.Write power(base, exp=2) — power(3) should square it (9). power(3,3) should cube it (27)
def power(base,exp=2):
    return base**exp
print(power(2))
print(power(2,3))

# 3.Write total(*numbers) that accepts ANY number of arguments and returns their sum.
def total(*numbers):
    print(sum(numbers))
total(2,3,5,9,4,4)

# 4.Create a function with 3 default parameters. Call it with 0 arguments, 1, 2, and all 3. See each result
def info(name='Unknown',age='0',city='Unknown'):
    print(name)
    print(age)
    print(city)
info()
info('Siddhu')
info('Siddhu','18')
info('Siddhu','18','Kakinada')

# 5.Call a function using keyword arguments: greet(message="Hey", name="Ravi") — order does not matter
def greet(name,message='Hi'):
    print(message,name)
greet(message='Hellow',name='Siddhu')