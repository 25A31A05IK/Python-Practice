# 1.Create an Employee class (name, id, salary); print a formatted payslip for 3 objects

class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary

    def payslip(self):
        print(f'{self.name} ID is {self.id} and Salary is {self.salary}')

person_1 = Employee('Siddhu',24,150000)
person_2 = Employee('Raghu',25,140000)
person_3 = Employee('Srinu',26,130000)

person_1.payslip()
person_2.payslip()
person_3.payslip()



# 2.Create a Student class storing 3 subject marks; add a method to calculate the average.

class Student:
    def __init__(self):
        self.maths = 50
        self.science = 49
        self.english = 50

    def avg_of_marks(self):
        print(f'Average: {(self.maths+self.science+self.english)/3}')

student = Student()

student.avg_of_marks()



# 3.Model a simple ATM class with balance, deposit(), and withdraw() with basic validation.

class ATM:

    def __init__(self,balance,deposited_money,withdraw_money):
        self.balance = balance
        self.deposited_money = deposited_money
        self.withdraw_money = withdraw_money

    def deposit(self):
        print(f'Balance: {self.balance}')
        print(f'Deposited Money: {self.deposited_money}')
        if self.deposited_money>0: 
            self.balance += self.deposited_money   
            print(f'New Balance: {self.balance}')
        else:
            print('Invalid.')

    def withdraw(self):
        print(f'Balance: {self.balance}')
        print(f'Withdraw Money: {self.withdraw_money}')
        if self.balance>0 and self.withdraw_money<=self.balance: 
            self.balance -= self.withdraw_money   
            print(f'New Balance: {self.balance}')
        else:
            print('Invalid.')

person_1 = ATM(10000,2000,5000)
person_2 = ATM(-2000,-1000,250)

person_1.deposit()
person_2.withdraw()
person_1.withdraw()
person_2.deposit()



# 4.Create a Movie class (title, genre, rating); filter a list of Movie objects by genre.

class Movie:

    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def movie(self):
        print(self.title,self.genre,self.rating,sep='\n')

movie_1 = Movie('Spiderman_1','Marvel',4.5)
movie_2 = Movie('Spiderman_3','Marvel',4.3)
movie_3 = Movie('Hit_3','Crime',4.4)
movie_4 = Movie('Kithakithalu','comedy',4.2)
movie_5 = Movie('Spiderman_Brand_New_Day','Marvel',5.0)

movie_1.movie()
movie_2.movie()
movie_3.movie()
movie_4.movie()
movie_5.movie()

movies = [movie_1,movie_2,movie_3,movie_4,movie_5]
for x in movies:
    if x.genre == 'Marvel':
        print(x.title)
    else:
        print('No Movies.')



# 5.Create a Rectangle class with area() and perimeter(); compare two rectangles by area.

class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area_of_rectangle = self.length*self.breadth
        print(f'Area of the rectangle: {area_of_rectangle}')
        return area_of_rectangle

    def perimeter(self):
        print(f'Permeter of the rectangle: {2*(self.length*self.breadth)}')

rectangle_1 = Rectangle(20,10)
rectangle_2 = Rectangle(30,20)

area_1 = rectangle_1.area()
area_2 = rectangle_2.area()

if area_1>area_2:
    print('Reactangle_1 is Big.')
elif area_2>area_1:
    print('Rectangle_2 is big.')
else:
    print('Both are equal.')



# 6.Model a Task class for a to-do app (title, done, priority); print only pending tasks.

class Model_Task:

    def __init__(self,title,pending,priority):
        self.title = title
        self.pending = pending
        self.priority = priority

    def Task(self):
        print(self.title,self.pending,self.priority)

task_1 = Model_Task('writing','Done','first')
task_2 = Model_Task('reading','not_done','last')
task_3 = Model_Task('playing','Done','middle')

task_1.Task()
task_2.Task()
task_3.Task()

tasks = [task_1,task_2,task_3]

for y in tasks:
    if y.pending == 'not_done':
        print(y.title)
    


# 7.Create a WeatherReading class (city, temp, humidity); find the hottest city from a list.

class Weather:
    def __init__(self,city,temp,humidity):
        self.city = city
        self.temp = temp
        self.humidity = humidity

    def check(self):
        print(self.city,self.temp,self.humidity)

city_1 = Weather('Kakinada',45,'high')
city_2 = Weather('Rajamundry',40,'Moderate')
city_3 = Weather('Hyderabad',39,'Low')

city_1.check()
city_2.check()
city_3.check()

cities = [city_1,city_2,city_3]

hottest = cities[0]

for x in cities:
    if x.temp>hottest.temp:
        hottest = x
print(f'{hottest.city} is the Hotttest City')



# 8.Model a Product class for a cart with price and quantity; calculate subtotal.

class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        print(f'{self.name} costs of {self.price*self.quantity}')

product_1 = Product('Car',500,2)
product_2 = Product('Bike',600,1)

product_1.subtotal()
product_2.subtotal()



# 9.Create a Vehicle class; instantiate 3 vehicles and print their details in a loop.

class Vehicle:

    def __init__(self,name,fuel_type):
        self.name = name
        self.fuel_type = fuel_type

    def details(self):
        print(f'Name: {self.name} , Fuel_type: {self.fuel_type}')

vehicle_1 = Vehicle('Bike','Petrol')
vehicle_2 = Vehicle('Car','Electric')
vehicle_3 = Vehicle('Lorry','Diesel')

detail = [vehicle_1,vehicle_2,vehicle_3]

for x in detail:
    x.details()



# 10.Model an Employee attendance system; calculate attendance percentage from present days.

class Employee_Attendence_System:

    total_days = 50

    def __init__(self,present_days):
        self.present_days = present_days

    def percentage(self):
        print(f'Attendance Precentage: {(self.present_days/self.total_days)*100}')

employee_1 = Employee_Attendence_System(45)
employee_2 = Employee_Attendence_System(50)

employee_1.percentage()
employee_2.percentage()