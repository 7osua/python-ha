# link: https://www.pythontutorial.net/python-oop/python-__repr__/

# Introduction to the '__repr__' magic method

"""
The '__repr__()' dunder method defines behavior when you
pass an instance of a class to the 'repr()'.


The '__repr__()' dunder method returns the string representation
of an object. Typically, the '__repr__()' return a string
that can be executed and yield the same values as the object.

In other words, if you pass the returned string of the
'object_name.__repr__()' method to the 'eval()' function,
you'll get the same values as the 'object_name'.
"""


# Define a 'Person' class with three intatance attributes
# 'first_name', 'last_name', and 'age'.
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # def __repr__(self):
    #     return f"Person({self.first_name}, {self.last_name}, {self.age})"

    # def __str__(self):
    #     return f"({self.first_name}, {self.last_name}, {self.age})"


# Create a new instance of the 'Person' class and display
# its string representation.
person = Person("Jane", "Doe", 27)

print(repr(person))
# [Output] <__main__.Person object at 0x000001E0C2E0B7F0>

print(person)
# [Output] <__main__.Person object at 0x000001E0C2E0B7F0>

"""
By default, the output contains the memory address of
the 'person' object. To customize the string representation
of the object, you can implement the '__repr__' method.
"""


class AnotherPerson:
    def __init__(self, first_name, last_name, age):
        self.firt_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'AnotherPerson("{self.firt_name}", "{self.last_name}", {self.age})'


"""
When you pass an instance of the 'AnotherPerson' class to the
'repr()', python will call the '__repr__' method automatically.

If you execute the return string 'AnotherPerson("Rose","Doe",25)',
it'll return the 'yet_another_person' object.
"""


another_person = AnotherPerson("John", "Doe", 25)
print(repr(another_person))
# [Output] AnotherPerson("John", "Doe", 25)

yet_another_person = AnotherPerson("Rose", "Doe", 25)
print(yet_another_person)
# [Output] AnotherPerson("Rose", "Doe", 25)

next_another_person = AnotherPerson("Bill", "Doe", 25)
print(str(next_another_person))
# [Output] AnotherPerson("Bill", "Doe", 25)

"""
When a class doesn't implement the '__str__()' method and
you pass an insatance of the class to the 'str()' function,
python return the result of the '__repr__()' method because
internally the '__str__' method calls the '__repr__' method.

If a class implements the '__str__' method, python will call
the '__str__()' method when you pass an instance of the class
to the 'str()' function.
"""


class NewPerson:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'NewPerson("{self.first_name}", "{self.last_name}", {self.age})'

    def __str__(self):
        return f'("{self.first_name}", "{self.last_name}", {self.age})'


a_new_person = NewPerson("Amber", "Doe", 25)

# Use the '__str__' method
print(a_new_person)
# [Output] ("Amber", "Doe", 25)

# Use the '__repr__' method
print(repr(a_new_person))
# [Output] NewPerson("Amber", "Doe", 25)

"""
The main difference berwwen '__str__' and '__repr__' method is
intended audiences.

The '__str__' method return a string representation of an object
that is human-readable while the '__repr__' method returns a string
representation of an object that is machine-readable.
"""

"""
Learn how to use the '__repr__' dunder method and understanding
the difference between the '__repr__' and '__str__' methods.

[Summary]
- Implement the '__repr__' method to customize the string representation
  of an object when 'repr()' function is called it.
- The '__str__' calss '__repr__' internally by default.
"""
