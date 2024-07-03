# link: https://www.pythontutorial.net/python-oop/python-__repr__/

# Introduction to the '__repr__' magic method


"""
Learn how to use the '__repr__' dunder method and the difference
between the '__repr__' and '__str__' methods.
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"

    def __str__(self):
        return f"({self.first_name}, {self.last_name}, {self.age})"


person = Person("Jane", "Doe", 27)
print(repr(person))
print(person)
