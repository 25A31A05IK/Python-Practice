
'''
# Create BankAccount where __init__ takes owner and starting balance; reject a negative starting balance

class Bank_Account:

    def __init__(self,name,starting_balance):
        self.name = name

        if starting_balance>=0:
            self.starting_balance = starting_balance
            print(self.starting_balance)
        else:
            raise ValueError('Starting Baalanace can\'t be negative.')

owner_1 = Bank_Account('Siddhu',1000)
owner_2 = Bank_Account('Raghu',-200)



# Create a User class where __init__ auto-generates a user_id using a class-level counter.

class User:

    counter = 0

    def __init__(self,name):
        self.name = name
        User.counter+=1
        self.user_id = User.counter

    def show(self):
        print(f'Name: {self.name} , User_ID: {self.user_id}')

user_1 = User('Siddhu')
user_2 = User('Raghu')
user_3 = User('Srinu')

user_1.show()
user_2.show()
user_3.show()



# Create a Flight class where __init__ sets flight number, origin, destination; add print_boarding_pass().

class Flight:

    def __init__(self,flight_number,origin,destination):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination

    def print_boarding_pass(self):
        print(f'Flight_Number:{self.flight_number} , Origin:{self.origin} , Destination: {self.destination}')

flight_1 = Flight(2020,'Kakinada','Hyderabad')
flight_2 = Flight(2022,'Rajamundry','Delhi')

flight_1.print_boarding_pass()
flight_2.print_boarding_pass()



# Write a method comparing two Product objects by price.

class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def comparision(self,other):
        if self.price>other.price:
            print('Product_1 is highest.')
        elif self.price==other.price:
            print('Equal.')
        else:
            print('Product_2 is highest')

product_1 = Product('Car',50000)
product_2 = Product('Bike',20000)

product_1.comparision(product_2)



# Create an Order class where __init__ takes a list of items and calculates total cost immediately.

class Order:

    def __init__(self,items):
        self.items = items
        self.total_cost = sum(items)

    def show(self):
        print(self.total_cost)

product_1 = Order([25,60,250])

product_1.show()



# Create an Employee class where __init__ raises ValueError for a negative salary.

class Employee:

    def __init__(self,name,salary):
        self.name = name

        if salary>=0:
            self.salary = salary
            print('Salary is credited')
        else:
            raise ValueError('No negative salary.')

employee_1 = Employee('Ravi',2000)
employee_2 = Employee('Siddhu',-10000)



# Create two Point objects (x, y) and calculate the distance between them.

import math

class Points:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,other):
        print(f'Distance: {math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2))}')

point_1 = Points(2,3)
point_2 = Points(4,5)

point_1.distance(point_2)



# Create a Book class where __init__ sets available=True by default; add borrow()/return_book().

class Book:

    def __init__(self,name):
        self.name = name
        self.available = True

    def borrow(self):
        if self.available==True:
            self.available=False
            print('Book is available to Borrow')
        else:
            print('Book is not available to borrow')

    def return_book(self):
        if self.available==False:
            self.available=True
            print('Book now returned')
        else:
            print('Book already Borrowed')

book_1 =Book('Python')

book_1.borrow()
book_1.return_book()



# Create a Car class where __init__ sets brand, model, year; add a method returning the car's age.

class Car:

    present_year = 2026

    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year

    def age(self):
        print(f'Age of {self.name},{self.model} is {Car.present_year-self.year}')

car_1 = Car('Tata','Safari',1998)
car_2 = Car('Toyota','Fortuner',2009)

car_1.age()
car_2.age()


'''
# Create a Person class and print several instances to observe Python's default object representation.

class Person:
    pass

person_1 = Person()
person_2 = Person()
person_3 = Person()

print(person_1)
print(person_2)
print(person_3)