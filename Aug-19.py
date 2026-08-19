# 1.Build a Shape system: abstract Shape base, Circle/Square/Triangle subclasses, each with area() and __str__.

import math 
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

    def __str__(self):
        return f'Area of Circle: {math.pi*self.radius*self.radius}'

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

    def __str__(self):
        return f'Area of Square: {self.side*self.side}'

class Triangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

    def __str__(self):
        return f'Area of Triangle: {0.5*self.base*self.height}'

shape_1 = Circle(2)
shape_2 = Square(4)
shape_3 = Triangle(2,5)

shapes = [shape_1,shape_2,shape_3]

for x in shapes:
    print(x.area())
    print(x)



# 2.Overload + on Shape subclasses so two shapes report combined area.

import math 
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __add__(self,other):
        return self.area()+other.area()

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

    def __str__(self):
        return f'Area of Circle: {math.pi*self.radius*self.radius}'

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

    def __str__(self):
        return f'Area of Square: {self.side*self.side}'


shape_1 = Circle(2)
shape_2 = Square(4)

total_area = shape_1 + shape_2

print(total_area)



# 3.Use duck typing: write a function calling .area() on any shape-like object, no type checks.

class Pen:

    def area(self):
        print('Area occupied bu pen is 10sqcm')

def execute(obj):
    obj.area()

execute(Pen())



# 4.Add encapsulation: make dimensions private, exposed only via getter methods.

class Rectangle:

    def __init__(self,length,breadth):
        self.__length = length
        self.__breadth = breadth

    def get_length(self):
        return self.__length

    def get_breadth(self):
        return self.__breadth

    def area(self):
        return f'Area of Rectangle is: {self.__length*self.__breadth}'

    def perimeter(self):
        return f'Perimeter of Rectangle is: {2*(self.__length+self.__breadth)}'

shape = Rectangle(2,4)

print(shape.get_length())
print(shape.get_breadth())
print(shape.area())
print(shape.perimeter())



# 5.Demonstrate polymorphism: loop through mixed shapes calling area() on each.

import math

class Shape:   

    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f'Area of Circle: {math.pi*self.radius*self.radius}'

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return f'Area of Square: {self.side*self.side}'

class Triangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return f'Area of Triangle: {0.5*self.base*self.height}'

shape_1 = Circle(2)
shape_2 = Square(4)
shape_3 = Triangle(2,5)

shapes = [shape_1,shape_2,shape_3]

for x in shapes:
    print(x.area())



# 6.Try instantiating the abstract Shape directly and explain the resulting error.

import math 
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

    def __str__(self):
        return f'Area of Circle: {math.pi*self.radius*self.radius}'

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

    def __str__(self):
        return f'Area of Square: {self.side*self.side}'

shape = Shape()

shape_1 = Circle(2)
shape_2 = Square(4)

print(shape_1.area())
print(shape_2.area())

print(shape_1)
print(shape_2)



# 7.Override __str__ differently in each subclass.

class Vehicle:

    def __str__(self):
        return 'Vehicle is a Bike.'

class Food:

    def __str__(self):
        return 'Food is Biryani.'

class House:

    def __str__(self):
        return 'House is Duplex.'

obj_1 = Vehicle()
obj_2 = Food()
obj_3 = House()

objects = [obj_1,obj_2,obj_3]

for x in objects:
    print(x)



# 8.Write a function sorting a list of shapes by area, largest first.

import math 
from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side*self.side

class Triangle(Shape):

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

shape_1 = Circle(2)
shape_2 = Square(4)
shape_3 = Triangle(2,5)

shapes_area = [shape_1.area(),shape_2.area(),shape_3.area()]

shapes_area.sort()
print(shapes_area)

shapes_area.sort(reverse=True)
print(shapes_area)



# 9.Add a custom exception raised when a shape is created with negative dimensions.

class DimensionValueError(Exception):
    pass

class Cicle:

    def __init__(self,radius):

        if radius>=0:
            self.radius = radius
            print(self.radius)
        else:
            raise DimensionValueError('Dimensions can\'t be negative.')

Cicle(4)
Cicle(-5)



# 10.In 3 lines, explain the difference between overloading and overriding in your own words.

Method Overloading - Using the same method, we can do different operation by taking different number of arguments/different types of arguments
Method Overriding - Own implementation of a method in child class that was already defined in parent class