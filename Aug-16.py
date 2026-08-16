'''
# 1.Create a Money class and overload + so two Money objects add correctly (handle currency).

class Money:

    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError('Currencies are Different')
        else:
            total = self.amount+other.amount
            return total
    
money_1 = Money(2000,'INR')
money_2 = Money(10000,'INR')

print(money_1+money_2)



# 2.Build a Vector class and overload +, -, and == for 2D vector math.

class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        comp_x = self.x+other.x
        comp_y = self.y+other.y
        return f'comp_x:{comp_x} , comp_y:{comp_y}'

    def __sub__(self, other):
        comp_x = self.x-other.x
        comp_y = self.y-other.y
        return f'comp_x:{comp_x} , comp_y:{comp_y}'

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

vector_1 = Vector(3,4)
vector_2 = Vector(2,3)

print(vector_1+vector_2,vector_1-vector_2,vector_1==vector_2,sep='\n')



# 3.Create a ShoppingCart class and overload + to merge two carts into one.

class ShoppingCart:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __add__(self, other):
        total_items = self.item + ' , ' + other.item
        total_price = self.price + other.price
        return f'Items: {total_items}\nTotal Price: {total_price}'

item_1 = ShoppingCart('Car',200)
item_2 = ShoppingCart('Bike',300)

print(item_1+item_2)



# 4.Model a Time class (hours, minutes) and overload + handling minute overflow correctly.

class Time:

    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        hours = self.hours+other.hours
        minutes = self.minutes+other.minutes
        extra_hours = minutes//60
        extra_minutes = minutes%60
        extra_hours += hours
        return f'{extra_hours}hours,{extra_minutes}minutes'

time_1 = Time(2,60)
time_2 = Time(3,20)

print(time_1+time_2)



# 5.Create a small Matrix class (2x2) and overload + for matrix addition.

class Matrix:

    def __init__(self,a11,a12,a21,a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __add__(self, other):
        a11 = self.a11 + other.a11
        a12 = self.a12 + other.a12
        a21 = self.a21 + other.a21
        a22 = self.a22 + other.a22
        add = Matrix(a11,a12,a21,a22)
        return add

    def __str__(self):
        return f'{self.a11} {self.a12}\n{self.a21} {self.a22}'

matrix_1 = Matrix(2,3,4,5)
matrix_2 = Matrix(3,4,5,6)

add = matrix_1+matrix_2

print(add)



# 6.Build a Fraction class and overload + and == for arithmetic and comparison.

class Fraction:

    def __init__(self,number):
        self.number = number

    def __add__(self, other):
        add = self.number + other.number
        return Fraction(add)

    def __eq__(self, value):
        if self.number == value.number:
            return True
        else:
            return False

    def __str__(self):
        return f'Addition: {self.number}'

number_1 = Fraction(1/4)
number_2 = Fraction(3/4)

addition = number_1+number_2

print(addition)

if number_1==number_2:
    print('Equal')
else:
    print('False')



# 7.Create a Playlist class and overload + to combine two playlists.

class Playlist:

    def __init__(self,songs_type,number):
        self.songs_type = songs_type
        self.number = number

    def __add__(self, other):
        songs_types = self.songs_type + ' , ' + other.songs_type
        numbers = self.number + ' , ' + other.number
        return Playlist(songs_types,numbers)

    def __str__(self):
        return f'Songs_type: {self.songs_type}\nNumber: {self.number}'
    
playlist_1 = Playlist('Telugu','10')
playlist_2 = Playlist('English','29')

print(playlist_1+playlist_2)



# 8.Model a Temperature class and overload > and < to compare two objects.

class Temperature:

    def __init__(self,temp):
        self.temp = temp

    def __gt__(self, other):
        if self.temp>other.temp:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.temp<other.temp:
            return True
        else:
            return False

temp_1 = Temperature(49)
temp_2 = Temperature(33)

if temp_1>temp_2:
    print('temp_1 is higher')
else:
    print('temp_2 is higher')

if temp_1<temp_2:
    print('temp_1 is lower')
else:
    print('temp_2 is lower')



# 9.Create an Inventory class and overload += to add stock directly.

class Inventory:

    def __init__(self,product,number):
        self.product = product
        self.number = number

    def __iadd__(self,value):
        self.number+=value
        return self

    def __str__(self):
        return f'{self.product} , {self.number}'

stock = Inventory('Laptop',10)

stock+=5

print(stock)


'''
# 10.Build a simple Polynomial class (low-degree) and overload + for addition.

class Polynomial:

    def __init__(self,coeff_of_xSquare,coeff_of_x,constant):
        self.first = coeff_of_xSquare
        self.second = coeff_of_x
        self.constant = constant

    def __add__(self, other):
        add_1 = self.first + other.first
        add_2 = self.second+other.second
        add_3 = self.constant+other.constant
        return add_1,add_2,add_3
    

polynomial_1 = Polynomial(1,2,3)
polynomial_2 = Polynomial(2,3,4)

print(polynomial_1+polynomial_2)