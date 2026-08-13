# Create a Car class with an inner Engine class (horsepower, fuel_type); build 2 cars with different engines.
''' 
class Car:

    def __init__(self,brand,model,horsepower,fuel_type):
        self.brand = brand
        self.model = model
        self.Engine = self.Engine(horsepower , fuel_type)

    def show(self):
        print(self.brand , self.model)
        self.Engine.show()

    class Engine:

        def __init__(self,horsepower,fuel_type):
            self.horsepower = horsepower
            self.fuel_type = fuel_type

        def show(self):
            print(self.horsepower , self.fuel_type)

car_1 = Car('Audi',2020,250,'diesel')
car_2 = Car('BMW',2021,300,'petrol')

car_1.show()
car_2.show()



# Create a University class with an inner Department class; list all departments.

class University:

    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.Department = self.Department()

    def show(self):
        print(self.name,self.location)
        self.Department.show()

    class Department:
        def __init__(self):
            self.department_1 = 'CSE'
            self.department_2 = 'Mechanical'
            self.department_3 = 'ECE'

        def show(self):
            print(self.department_1,self.department_2,self.department_3 , sep='\n')

University_1 = University('Pragati','Surampalem')

University_1.show()



# Model a House class with an inner Room class (name, area); calculate total house area.

class House:

    def __init__(self):
        self.Room = self.Room()

    class Room:

        def __init__(self):
            self.room_1 = 'Hall'
            self.room_2 = 'Bedroom'
            self.room_3 = 'Kitchen'
            self.area_1 = 30
            self.area_2 = 24
            self.area_3 = 20

        def total_area(self):
            total_area = self.area_1+self.area_2+self.area_3
            print('Area of each room:')
            print(f'{self.room_1}:{self.area_1}')
            print(f'{self.room_2}:{self.area_2}')
            print(f'{self.room_3}:{self.area_3}')
            print('Total area of the house:',total_area)

house = House()
house.Room.total_area()



# Create an Order class with an inner Address class for shipping details.

class Order:

    def __init__(self , product , district , area , door_no):
        self.product = product
        self.Address = self.Address(district , area , door_no)

    def show(self):
        print(f'Product: {self.product}')
        self.Address.show()

    class Address:

        def __init__(self , district , area , door_no):
            self.district = district
            self.area = area
            self.door_no = door_no

        def show(self):
            print(self.district,self.area,self.door_no,sep='\n')

product_1 = Order('Car','Kakinada','Indrapalem','4-161')
product_2 = Order('Dress','Rajamundry','Gandhinagar','6-134')

product_1.show()
product_2.show()

'''

# Build a Laptop class with an inner Battery class; flag laptops with battery health below 50%.