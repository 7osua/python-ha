# link : https://www.pythontutorial.net/python-oop/python-static-methods/


# Introduction to static methods


# Static method examples


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


f = TemperatureConverter.celcius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))

"""
Learn about static methods and learn
how to use static methods to create a utility class.
"""
