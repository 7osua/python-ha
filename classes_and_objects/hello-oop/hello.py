# link : https://www.pythontutorial.net/python-oop/python-object-oriented-programming/


# Introduction to object-oriented programming


"""
- Everything in python is an object.
- An object has a state and behaviors.
- To create object, we can define a class first.
- Then, from the class we can create one or more objects.
- The objects we created from the classe is an intance.
"""

# Define a class


class Person:
    pass


person = Person()
print(person)

"""
- To define a class, you use the class keyword followed by the class name.
- To create an object from the class, we can assign
  the class name followed by parantheses, like calling a function.
- In this example, the person is an instance of the Person class.
  Classes are callable.
"""


# Define instance attributes

"""
- Python is dynamic language, it means we can
  add an attribute to an instance of class dynamically at runtime.
- However, if you create another Person object,
  the new object won’t have the name attribute.
"""

# person.name = "John"
# person2 = Person()
# person2.age = 23

# print(person.name)
# print(person2.age)
# print(person2.name)  # AttributeError

"""
To define and initialize an attribute for all instances of a class,
you use the "__init__" method.
The following defines the Person class with two instance attributes name and age:
"""


class PersonWithAttributes:
    def __init__(self, name, age):
        self.name = name
        self.age = age


a_person = PersonWithAttributes("john", 25)
print(a_person.name)
print(a_person.age)

"""
When we create a "personWithAttributes" object, python will automatically cals
the "__init__" method to initialize the instance attributes.
In the "__init__" method, the "self" is the instance of the "PersonWithAttributes" class.
To access an instance attribute, you use the dot notation "a_person.name".
"""

"""
Learn about object-oriented programming in python,
including essential concepts such as
objects, classes, attributes, methods,
inherintences, overriding methods, etc...
"""
