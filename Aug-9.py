# Create a Temperature class with a @staticmethod converting Celsius to Fahrenheit.
class Temperature:
    
    @staticmethod
    def Fahrenheit(f):
        return (f-32)*5/9

fahrenheit = 32
celsius = Temperature.Fahrenheit(fahrenheit)

print('Fahrenheit:',fahrenheit)
print('Celcius:',celsius)

