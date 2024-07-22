# link: https://www.pythontutorial.net/python-oop/python-properties/

# Introduction to class properties


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 18)
john.age = -1

age = 0
if age <= 0:
    raise ValueError("The age must be positive")
else:
    john.age = age

# [Output] ValueError: The age must be positive


class NotValid:
    def __init__(self, name, age):
        self.name = name
        if age <= 0:
            raise ValueError("The age must be positive")
        else:
            self.age = age


jane = NotValid("Jane", -1)
# [Output] ValueError: The age must be positive


# Introduction to Getter and Setter


class NewPerson:

    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    def get_age(self):
        return self._age


john = NewPerson("John", 18)
john.set_age(-18)
# [Output] ValueError: The age must be positive

"""
Learn about the 'property' class and how to use it to define properties
for class.
"""
