# link: https://www.pythontutorial.net/python-oop/python-__eq__/

# Introduction to the '__eq__()' method

"""
Suppose that you have the 'Person' class with
three instance attributes: 'first_name', 'last_name', 'age'.

Then you create two instances of the 'Person' class.
the 'john' and 'jane' objects are not the same object.
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


john = Person("John", "Doe", 25)
jane = Person("Jane", "Doe", 25)

# Check if the objects are the same using the 'is' operator.
print(john is jane)
# [Output] False

# Check if the objects are the same using the '==' equality operator.
print(john == jane)
# [Output] False

"""
In this case, since 'john' and 'jane' have the same 'age', you want
them to be equal. In other words. you want the following expression
to return 'True'.

    john == jane

To do it, you can implement the '__eq__()' dunder method
in the 'Person' class.

The following shows how implements the '__eq__()' method
in the 'Person' class that return 'True' if two person obejcts
have the same 'age'.
"""


class AnotherPerson:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, AnotherPerson):
            return self.age == other.age

        return False


another_john = AnotherPerson("John", "Doe", 25)
another_jane = AnotherPerson("Jane", "Doe", 25)
another_older_john = AnotherPerson("Jane", "Doe", 27)

print(another_john == another_jane)
# [Output] True

print(another_john == another_older_john)
# [Output] False

"""
Now if you compare the two instances of the 'AnotherPerson' class
with the same 'age', it returns 'True'.

If two instances of the 'AnotherPerson' class don't have the same 'age'
the '==' operator return 'False'.
"""

# Compares a 'AnotherPerson' object with an integer
print(another_john == 25)
# [Output] AttributeError

"""
To fix the 'AttributeError', you can modify the '__eq__()' method
to check if the object is an instance of the 'AnotherPerson' class
before accessing the 'age' attribute.

If the 'other' object isn't an instance of the 'AnotherPerson' class,
the '__eq__()' method returns 'False'.
"""

print(another_john == 25)
# [Output] False

"""
Learn how to use the '__eq__()' mehtod to compare two objects by
their values.

[Summary]
- Implement the '__eq__()' method to define the equality logic
  for comparing two objects using the '==' the equal operator.
"""
