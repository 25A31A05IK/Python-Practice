# 1.Create an abstract PaymentMethod with abstract pay(), implemented by CreditCard and UPI.

from abc import ABC,abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentMethod):

    def pay(self):
        print('Pay using Credit Crad')

class UPI(PaymentMethod):

    def pay(self):
        print('Pay using UPI')

user_1 = CreditCard()
user_2 = UPI()

user_1.pay()
user_2.pay()



# 2.Build an abstract Shape with abstract area(), implemented by 3 shape subclasses.

from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self,radius):
        return f'Area of Circle: {3.14*radius*radius}'

class Square(Shape):

    def area(self,side):
        return f'Area of Square: {side*side}'

class Rectangle(Shape):

    def area(self,length,breadth):
        return f'Area of Rectangle: {length*breadth}'

shape_1 = Circle()
shape_2 = Square()
shape_3 = Rectangle()

print(shape_1.area(2))
print(shape_2.area(4))
print(shape_3.area(2,3))



# 3.Create an abstract Employee with abstract calculate_salary(), implemented by 2 employee types.

from abc import ABC,abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):

    def calculate_salary(self):
        return f'Salary is: 200000'

class Worker(Employee):

    def calculate_salary(self):
        return f'Salary is: 100000'

employee_1 = Manager()
employee_2 = Worker()

print(employee_1.calculate_salary())
print(employee_2.calculate_salary())



# 4.Model an abstract Notifier with abstract send(), implemented by Email and SMS notifiers.

from abc import ABC,abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Notifier):

    def send(self):
        print('Notification sent by Email')

class SMS(Notifier):

    def send(self):
        print('Notification sent by SMS')

Email().send()
SMS().send()



# 5.Create an abstract DataExporter with abstract export(), implemented by JSON and CSV exporters.

from abc import ABC,abstractmethod

class DataExporter(ABC):

    @abstractmethod
    def export(self):
        pass

class JSON(DataExporter):

    def export(self):
        return {'Name':'Siddhu','Age':18,'Designation':'Student'}

class CSV(DataExporter):

    def export(self):
        return f'Name,Age,Designation\nSiddhu,18,Student'

print(JSON().export())
print(CSV().export())



# 6.Build an abstract Vehicle with abstract fuel_efficiency(), implemented by 2 vehicle types.

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def fuel_efficiency(self):
        pass

class Bike(Vehicle):

    def fuel_efficiency(self):
        return 'Efficiency is less'

class Car(Vehicle):

    def fuel_efficiency(self):
        return 'Efficiency is high'

print(Bike().fuel_efficiency())
print(Car().fuel_efficiency())



# 7.Try instantiating your abstract class directly and explain the resulting TypeError.

from abc import ABC,abstractmethod

class Demo(ABC):

    @abstractmethod
    def classs(self):
        pass

x = Demo()



# 8.Create an abstract Game with abstract play(), implemented by 2 different game types.

from abc import ABC,abstractmethod

class Game(ABC):

    @abstractmethod
    def play(self):
        pass

class CandyCrush(Game):

    def play(self):
        print('Playing Candy Crush')

class Cricket(Game):

    def play(self):
        print('Playing Cricket')

CandyCrush().play()
Cricket().play()



# 9.Model an abstract Report with abstract generate(), implemented by 2 report types.

from abc import ABC,abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

class Medical_Report(Report):

    def generate(self):
        print('Medical Report')

class Event_Report(Report):

    def generate(self):
        print('Event Report')

Medical_Report().generate()
Event_Report().generate()



# 10.Build an abstract Validator with abstract is_valid(), implemented for email and phone validation.

from abc import ABC,abstractmethod

class Validator(ABC):

    @abstractmethod
    def is_valid(self):
        pass

class Email(Validator):

    def is_valid(self,email):
        if '@' in email:
            print('Valid')
        else:
            print('Invalid')

class Phone_Number(Validator):

    def is_valid(self,number):
        if len(number)==10:
            print('Valid')
        else:
            print('Invalid')

Email().is_valid('adnx@gmail.com')
Phone_Number().is_valid('2856956559')