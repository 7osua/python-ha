# link : https://www.pythontutorial.net/python-oop/python-static-methods/


# Introduction to static methods
"""
Previously, you have learned about instance methods that are
bound to a specific instance. It means that instance methods
can access and modify the state of the bound object.

Also, you learned about 'class methods' that are bound to a
class. The class methods can access and modify the class state.

Unlike instance methods, static methods aren't bound to an
object. In other words, static methods cannot access and modify
an object state.

in addition, Python doesn't implicitly pass the 'cls' parameter
(or the 'self') to static methods.
Therefore, static methods cannot access and modify
the class state.

In practice, you use the static methods to define utility methods
or group functions that have some logical relationships in a class.

to define a statice method, we can use the '@staticmethod' decorator

    class ClassName:

        @staticmethod
        def static_method_name(param_list):
            pass

to call a static method, we use this syntax.

    ClassName.static_method_name()

"""

# Python static methods Vs. class methods
"""
Class Methods
- Python implicitly pass the 'cls' argument to class methods.
- Class methods can access and modify the class state.
- Use '@classmethod' decorators to define class methods.

Static Methods
- Python doesn't implicitly pass the 'cls' argument
  to static methods.
- Static methods cannot access or modify the class state.
- Use '@staticmethod' decorators to define static methods.
"""


# Static method examples


# Define a class that has static methods for
# converting temperatures between
# Celcius, Fahrenheit and Kelvin


class TemperatureConverter:
    KELVIN = "K"
    FAHRENHEIT = "F"
    CELCIUS = "C"

    @staticmethod
    def celcius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celcius(f):
        return 5 * (f - 32) / 9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celcius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5 * (f + 459.67) / 9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9 * k / 5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ""

        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = "°F"
        elif unit == TemperatureConverter.CELCIUS:
            symbol = "°C"
        elif unit == TemperatureConverter.KELVIN:
            symbol = "°K"

        return f"{value} {symbol}"


# call the 'TemperatureConverter' class
f = TemperatureConverter.celcius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))

# [Output] 95.0 °F

"""
Learn about static methods and learn
how to use static methods to create a utility class.

[Summary]
- Use static methods to define utility methods or group
  a logically related functions into a class.
- Use the '@staticmethod' decorator to define a static
  method.
"""
