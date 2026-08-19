# 1.Write 2 unrelated classes (Duck, Robot) both with quack(), called without checking type.

class Duck:

    def quack(self):
        print('Sounds like quack quack')

class Robot:

    def quack(self):
        print('Sounds like Hello')

object_1 = Duck()
object_2 = Robot()

objects = [object_1,object_2]

for x in objects:
    x.quack()



# 2.Write a function calling .read() on any object, working for a File-like and StringBuffer-like class.

class File:

    def read(self):
        print('Give the contents of the file')

class String_Buffer():

    def read(self):
        print('Give the text that had been stored in the string')

def execute(obj):
    obj.read()

obj_1 = File()
obj_2 = String_Buffer()

execute(obj_1)
execute(obj_2)



# 3.Build EmailSender and SMSSender, both with send(), and a function that works with either.

class Email_Sender:

    def send(self):
        print('Sent through Email')

class SMS_Sender:

    def send(self):
        print('Sent through SMS')

def execute(obj):
    obj.send()

obj_1 = Email_Sender()
obj_2 = SMS_Sender()

execute(obj_1)
execute(obj_2)



# 4.Write a function that processes any object with a .to_dict() method, regardless of class.

class Student:

    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location

    def to_dict(self):
        return f"\'Name\': \'{self.name}\'\n\'Age\': \'{self.age}\'\n\'Location\': \'{self.location}\'"

class Employee:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def to_dict(self):
        return {
            'Name': self.name,
            'Age': self.age,
            'Salary': self.salary
        }

def execute(obj):
    return obj.to_dict()

obj_1 = Student('Siddhu',18,'Kakinada')
obj_2 = Employee('Srinu',42,100000)

print(execute(obj_1))
print(execute(obj_2))



# 5.Build JSONExporter and CSVExporter, both with export(), called generically.

class JSON_Exporter:

    def export(self):
        print('Exported through JSON')

class CSV_Exporter:

    def export(self):
        print('Exported through CSV')

def execute(obj):
    obj.export()

file_1 = JSON_Exporter()

execute(file_1)
execute(CSV_Exporter())



# 6.Write a function calling .calculate_total() on any object, working across Cart and Invoice classes.

class Cart:

    def __init__(self,item_1,item_2,item_3):
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3

    def calculate_total(self,):
        return self.item_1+self.item_2+self.item_3

class Invoice:

    def __init__(self,product_1,product_2,product_3):
        self.product_1 = product_1
        self.product_2 = product_2
        self.product_3 = product_3

    def calculate_total(self):
        return self.product_1+self.product_2+self.product_3

def execute(obj):
    return obj.calculate_total()

obj_1 = Cart(10,20,30)
obj_2 = Invoice(50,60,70)

print(execute(obj_1))
print(execute(obj_2))



# 7.Create Printer and Scanner, both with start(), called through one common function.

class Printer:

    def start(self):
        print('Printer')

class Scanner:

    def start(self):
        print('Scanner')

def execute(obj):
    obj.start()

obj_1 = Printer()
obj_2 = Scanner()

execute(obj_1)
execute(obj_2)



# 8.Write a function working with anything having a .validate() method, tested on 2 classes.

class Email:

    def validate(self,email):

        if '@' in email:
            print('Valid')
        else:
            print('Invalid')

class SMS:

    def validate(self,number):

        if len(number)==10:
            print('Valid')
        else:
            print('Invalid')

def execute(obj,value):
    obj.validate(value)

user_1 = Email()
user_2 = SMS()

execute(user_1,'ueeeejs@gmail.com')
execute(user_2,'1234567890')



# 9.Build LocalStorage and CloudStorage, both with save(), used interchangeably.

class LocalStorage:

    def save(self):
        print('Stored in LocalStorage')

class CloudStorage:

    def save(self):
        print('Stored in CloudStorage')

def execute(obj):
    obj.save()

execute(LocalStorage())
execute(CloudStorage())



# 10.Write a function logging any object with a .get_status() method, tested on 2 unrelated classes.

class Reading:

    def get_status(self):
        print('Done')

class Writing:

    def get_status(self):
        print('Pending')

def execute(obj):
    obj.get_status()

execute(Reading())
execute(Writing())