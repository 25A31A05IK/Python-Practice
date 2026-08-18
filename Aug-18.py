# 1.Create BankAccount with a private __balance; deposit()/withdraw() are the only ways to change it.

class BankAccount:

    def __init__(self,balance,deposit_money,withdraw_money):
        self.__balance = balance
        self.deposit_money = deposit_money
        self.withdraw_money = withdraw_money

    def get_balance(self):
        return self.__balance

    def deposit(self):
        self.__balance += self.deposit_money
        return self.__balance

    def withdraw(self):
        self.__balance -= self.withdraw_money
        return self.__balance

account = BankAccount(20000,3000,2000)

print(f'Balance Money: {account.get_balance()}')
print(f'Balance after deposited: {account.deposit()}')
print(f'Balance after withdrawn: {account.withdraw()}')



# 2.Build a User class with private __password, exposing only check_password() (never the raw value).

class User:

    def __init__(self,password):
        self.__password = password

    def check_password(self,password):
        return self.__password == password

user = User('7071')

print(f"Password is: {user.check_password('7071')}")



# 3.Create an Employee class with private __salary, exposing get_salary() only for that employee

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.name,self.__salary

employee = Employee('Siddhu',100000)

print(employee.get_salary())



# 4.Model a Car class with private __mileage, increasable only via a drive() method.

class Car:

    def __init__(self,name,mileage):
        self.name = name
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage
    
    def drive(self):
        self.__mileage += 5
        return self.__mileage

car = Car('Audi',6)

print(f'General Mileage: {car.get_mileage()}')
print(f'After Servicing: {car.drive()}')



# 5.Create an Inventory class with private __stock, exposing add_stock()/remove_stock() with validation.

class Inventory:

    def __init__(self,name,stock):
        self.name = name
        self.__stock = stock

    def get_stock(self):
        return f'Stock: {self.name}\nNumber: {self.__stock}'

    def add_stock(self,x):
        if x>0:
            self.__stock += x
            return self.__stock
        else:
            return 'Invalid.'
        
    def remove_stock(self,y):
        if self.__stock>0:
            if y>0 and y<=self.__stock:
                self.__stock -= y
                return self.__stock
            else:
                return'Invalid.'
        else:
            return 'Invalid.'

stock = Inventory('Car_Toys',10)

print(stock.get_stock())
print(stock.add_stock(5))
print(stock.add_stock(-6))
print(stock.remove_stock(5))



# 6.Build a Student class with a private __marks list, exposing add_mark() and calculate_average().

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def add_marks(self,x):
        self.__marks.append(x)
        return self.__marks

    def calculate_average(self):
        average = sum(self.__marks)/len(self.__marks)
        return average

    def get_marks(self):
        return f'Name: {self.name}\n{self.__marks} , {self.calculate_average()}'

student = Student('Siddhu',[99,98,97])

print(student.add_marks(96))
print(student.calculate_average())
print(student.get_marks())



# 7.Create a SecureFile class with private __content, readable only via read(password).

class Secure_File:

    def __init__(self,content,password):
        self.__content = content
        self.password = password

    def read(self,x):
        if self.password == x:
            return self.__content
        else:
            return 'You cannot open.'

file = Secure_File("Dddy\'s Home",'7071')

print(file.read('7071'))
print(file.read('5555'))



# 8.Model a Thermostat class with a private __temperature changeable only within a safe range.

class Thermostat:

    def __init__(self,temperature):
        self.__temperature = temperature

    def change_temperature(self,x):
        if x>=20 and x<=35:
            self.__temperature = x
            return self.__temperature
        else:
            return 'You can\'t change the temperature.'

temperature_1 = Thermostat(25)
temperature_2 = Thermostat(10)

print(temperature_1.change_temperature(30))
print(temperature_2.change_temperature(45))



# 9.Create a Wallet class with a private __balance, ensuring withdraw() never goes negative.

class Wallet:

    def __init__(self,balance,withdraw_money):
        self.__balance = balance
        self.withdraw_money = withdraw_money

    def withdraw(self):
        if self.withdraw_money>0 and self.withdraw_money<=self.__balance:
            self.__balance -= self.withdraw_money
            return self.__balance
        else:
            return 'Can\'n be processed.'

user_1 = Wallet(10000,5000)
user_2 = Wallet(10000,20000)

print(user_1.withdraw())
print(user_2.withdraw())



# 10.Build a UserSession class with a private __token, exposing only validate_token().

class User_Section:

    def __init__(self,token):
        self.__token = token

    def validate_token(self,token):
        if self.__token == token:
            return True
        else:
            return False
        
user_1 = User_Section('7071')
user_2 = User_Section('5555')

print(user_1.validate_token('7071'))
print(user_2.validate_token('2052'))