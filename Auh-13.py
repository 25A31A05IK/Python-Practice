'''
# 1.Create a 3-level chain Person -> Employee -> Manager, each constructor adding attributes via super().

class Person:

    def __init__(self):
        self.name = 'Siddhu'
        print(self.name)

class Employee(Person):

    def __init__(self):
        super().__init__()
        self.name = 'Raghu'
        print(self.name)

class Manager(Employee):

    def __init__(self):
        super().__init__()
        self.name = 'Cherry'
        print(self.name)

manager = Manager()



# 2.Create Vehicle -> Car -> SportsCar and verify attributes from all 3 levels print correctly.

class Vehicle:

    def __init__(self):
        self.name = 'Car'
        print(self.name)

class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.name = 'Audi'
        print(self.name)

class Sports_Car(Car):

    def __init__(self):
        super().__init__()
        self.name = 'X38H'
        print(self.name)

sports_car = Sports_Car()



# 3.Build Account -> SavingsAccount where the child constructor validates a minimum balance.

class Account:

    min_balance = 1000

    def __init__(self,balance):
        self.balance = balance

class Savings_Account(Account):

    def __init__(self):
        super().__init__(2000)
        if self.balance >= Account.min_balance:
            print('Valid.')
        else:
            print('Invalid.')

Savings_account = Savings_Account()



# 4.Create Shape -> Polygon -> Triangle, checking constructor chaining sets all attributes.

class Shape:

    def __init__(self):
        self.colour = 'Red'
        print(self.colour)

class Polygon(Shape):

    def __init__(self):
        super().__init__()
        self.sides = 4
        print(self.sides)

class Triangle(Polygon):

    def __init__(self):
        super().__init__()
        self.base = 10
        print(self.base)

triangle = Triangle()



# 5.Model User -> PremiumUser where PremiumUser's constructor adds subscription details via super().

class User:

    def __init__(self):
        self.app = 'Spotify'
        print(self.app)

class Premium_User(User):

    def __init__(self):
        super().__init__()
        self.amount = 200
        self.discount = '10%'
        self.total_amount = 180
        self.duration = '1Year'
        print(self.amount,self.discount,self.total_amount,self.duration,sep='\n')

user_1 = Premium_User()



# 6.Create Device -> Phone -> SmartPhone and print full combined spec details.

class Device:

    def __init__(self,brand):
        self.brand = brand
        print(self.brand)

class Phone(Device):

    def __init__(self,model):
        super().__init__('IPhone')
        self.model = model
        print(self.model)

class Smart_Phone(Phone):

    def __init__(self,ram,rom,camera):
        super().__init__('17 Pro Max')
        self.ram = ram
        self.rom = rom
        self.camera = camera
        print(self.ram,self.rom,self.camera,sep='\n')

customer = Smart_Phone('8gb','256gb','48mp')



# 7.Build Employee -> Manager where Manager's constructor validates team_size is non-negative.

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(self.name,self.salary,sep='\n')

class Manager(Employee):

    def __init__(self,team_size):
        super().__init__('Siddhu',200000)
        self.team_size = team_size

        if self.team_size>=0:
            print('Valid.')
        else:
            print('Invalid.')

Employee_1 = Manager(6)



# 8.Create Animal -> Bird -> Eagle, each level adding movement-related attributes.

class Animal:

    def __init__(self,movement):
        self.movement = movement
        print(self.movement)

class Bird(Animal):

    def __init__(self,movement_type):
        super().__init__('Walk')
        self.movement_type = movement_type
        print(self.movement_type)

class Eagle(Bird):

    def __init__(self, movement_speed):
        super().__init__('Fly')
        self.movement_speed = movement_speed
        print(movement_speed)

bird_1 = Eagle(30)



# 9.Model Product -> DigitalProduct where the child sets a default file_size if not provided.

class Product:

    def __init__(self,name):
        self.name = name
        print(self.name)

class Digital_Product(Product):

    def __init__(self,file_size='100mb'):
        super().__init__('Photo')
        self.file_size = file_size
        print(self.file_size)

product_1 =Digital_Product()


'''
# 10.Create Person -> Student -> GraduateStudent and verify all attributes are accessible.
class Person:

    def __init__(self,name):
        self.name = name
        print(self.name)

class Student(Person):

    def __init__(self, Roll_number):
        super().__init__('Siddhu')
        self.Roll_number = Roll_number
        print(self.Roll_number)

class Graduate_Student(Student):

    def __init__(self,year):
        super().__init__('25A31A05IK')
        self.year = year
        print(self.year)

person = Graduate_Student(2029)