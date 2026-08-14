# 1.Create a list of Shape subclasses (Circle, Square, Triangle) and call area() on each in a loop.

class Shape:

    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f'Area of circle: {3.14*(self.radius**2)}')

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        print(f'Area of square: {self.side**2}')

class Triangle(Shape):

    def __init__(self,breadth,height):
        self.breadth = breadth
        self.height = height

    def area(self):
        print(f'Area of triangle: {0.5*self.breadth*self.height}')

shapes = [Circle(2),Square(4),Triangle(2,3)]

for shape in shapes:
    shape.area()



# 2.Model a list of Employee subclasses and call a shared calculate_bonus() method polymorphically.

class Manager:

    def __init__(self,salary,bonus_rate,days_worked,total_days):
        self.salary = salary
        self.bonus_rate = bonus_rate
        self.days_worked = days_worked
        self.total_days = total_days

    def calculate_bonus(self):
        self.bonus = (self.salary*self.bonus_rate)*(self.days_worked/self.total_days)
        print(self.bonus)

class Employee_1(Manager):

    def __init__(self):
        super().__init__(100000,20,45,50)

    def calculate_bonus(self):
        super().calculate_bonus()

class Employee_2(Manager):

    def __init__(self):
        super().__init__(200000,30,49,50)

    def calculate_bonus(self):
        super().calculate_bonus()

class Employee_3(Manager):

    def __init__(self):
        super().__init__(50000,80,50,50)

    def calculate_bonus(self):
        super().calculate_bonus()


Employees = [Employee_1(),Employee_2(),Employee_3()]

for employee in Employees:
    employee.calculate_bonus()



# 3.Create a list of Payment subclasses and process all payments via a common process() method.

class Payment:

    def process(self):
        pass

class UPI(Payment):

    def process(self):
        print('UPI Type Payment')

class Card(Payment):

    def process(self):
        print('Card Type Payment')

class Cash(Payment):

    def process(self):
        print('Cash Type Payment')

payments = [UPI(),Card(),Cash()]

for x in payments:
    x.process()

    

# 4.Build a list of Notification subclasses and send all via one loop calling send().

class Notifications:

    def send(slef):
        pass

class Whatsapp(Notifications):

    def send(self):
        print('It is an Whatsapp notification')

class Instagram(Notifications):

    def send(self):
        print('It is an Instagram notification')

class Snapchat(Notifications):

    def send(self):
        print('It is an Snapchat notification')

Notification = [Whatsapp(),Instagram(),Snapchat()]

for x in Notification:
    x.send()


    
# 5.Create a list of Animal subclasses and call move() on each, printing different styles.

class Animal:

    def move(self):
        pass

class Hen(Animal):

    def move(self):
        print('Small steps')

class Dog(Animal):

    def move(self):
        print('Medium steps')

class Kangaroo(Animal):

    def move(self):
        print('Large steps')

animal_1 = Hen()
animal_2 = Dog()
animal_3 = Kangaroo()

animals = [animal_1,animal_2,animal_3]

for x in animals:
    x.move()



# 6.Model a list of Vehicle subclasses and call fuel_type() polymorphically.

class Vehicle:

    def fuel_type(self):
        pass

class Bike(Vehicle):

    def fuel_type(self):
        print('Pertol')

class Car(Vehicle):

    def fuel_type(self):
        print('Diesel')

vehicles = [Bike(),Car()]

for x in vehicles:
    x.fuel_type()



# 7.Create a list of Report subclasses and generate all reports using generate().

class Report:

    def generate(self):
        pass

class Sales_Report(Report):

    def generate(self):
        print('Sales_Report')

class Student_Report(Report):

    def generate(self):
        print('Student_Report')

class Medical_Report(Report):

    def generate(self):
        print('Medical_Report')

reports = [Sales_Report(),Student_Report(),Medical_Report()]

for x in reports:
    x.generate()



# 8.Build a list of Discount subclasses applying discounts polymorphically.

class Discount:

    def calculate_discount(self):
        pass

class Discount_1(Discount):

    def calculate_discount(self):
        print('10% Discount')

class Discount_2(Discount):

    def calculate_discount(self):
        print('20% Discount')

discounts = [Discount_1(),Discount_2()]

for x in discounts:
    x.calculate_discount()



# 9.Create a list of Employee subclasses and print a summary using a shared describe() method

class Employeee:

    def describe(self):
        pass

class Manager(Employeee):

    def describe(self):
        print('Manager tooks all the tasks and checks whwther employees are doing or not')

class Employee(Employeee):

    def describe(self):
        print('Employee implements the tasksss')

employee = [Manager(),Employee()]

for x in employee:
    x.describe()


    
# 10.Model a list of File subclasses and call a shared get_size() method on each.

class File:

    def get_size(self):
        pass

class File_1(File):

    def get_size(self):
        print('File size is 100mb')

class File_2(File):

    def get_size(self):
        print('File size is 200mb')

files = [File_1(),File_2()]

for x in files:
    x.get_size()