# link: https://www.pythontutorial.net/python-oop/python-__str__/

# Introduction to the '__str__' method


# Define a class
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


"""
Below is the 'Person' class with three instance attributes
including 'first_name', 'last_name', 'age'.
After that creates a new instance of the 'Person' class,
then display the new instance of the 'Person' class.

When you use the 'print()' function to display the instance
of the 'Person' class, the 'print()' function shows the memory
address of that instance.

Sometimes, it's useful to have a string representation of an
instance of a class. To customize the string representation of
a class instance, the class needs to implement the '__str__'
magic method.
"""


person = Person("John", "Doe", 25)
print(person)
# [Output] <__main__.Person object at 0x00000183031A8520>

"""
Internally, python will call the '__str__' method automatically
when an instance calls the 'str()' method.

[Note]
the 'print()' function converts all non-keyword arguments to strings
by passing them to the 'str()' before displaying the string values.

The following new class illustrates how to implement the '__str__'
method in the 'Person' class.
"""


class PersonWithStrMethod:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"


"""
When you use the print() function to print an instance
of the 'PersonWithStrMethod' class, python calls the '__str__()' method
defined int the 'PersonWithStrMethod' class.
"""
another_person = PersonWithStrMethod("John", "Doee", 37)
print(another_person)
# [Output] Person(John, Doee, 37)

"""
Learn how to use the '__str__' method to make a string
representation of a class.

[Summary]
- Implement the '__str__()' method to customize the string
  representation of an instance of a class.
"""
