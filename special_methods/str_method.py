# link: https://www.pythontutorial.net/python-oop/python-__str__/

"""
Learn how to use the '__str__' method to make a string
representation of a class.
"""

# Introduction to the '__str__' method


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"


person = Person("John", "Doe", 25)
print(person)
# [Output] <__main__.Person object at 0x00000183031A8520>


# [Output] Person(John, Doe, 25)
