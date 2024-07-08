# link: https://www.pythontutorial.net/python-oop/python-__eq__/

# Introduction to the '__eq__()' method


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)

print(john is jane)
# [Output] False

print(john == jane)
# [Output] False

"""
Learn how to use the '__eq__()' mehtod to compare two objects by
their values.
"""
