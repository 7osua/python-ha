# link: https://www.pythontutorial.net/python-oop/python-delete-property/

from pprint import pprint


# Defines the 'Person' class with the 'name' property
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        self._name = value

    @name.deleter
    def name(self):
        del self._name


"""
To create a property of a class, you use the '@property'
decorator. Underhood, the '@property' decorator uses
'property' class that has three methods:
setter, getter, and deleter.

By using the deleter, you can delete a property from
an object. Notice that the 'deleter()' method deletes a property
of an object, not a 'class'.
"""


pprint(Person.__dict__)
# [Output]
# mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
#               '__doc__': None,
#               '__init__': <function Person.__init__ at 0x000001B6276EB100>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'Person' objects>,
#               'name': <property object at 0x000001B62773F100>})

"""
In the 'Person' class, we use the '@name.deleter' decorator. Inside the deleter, we use the 'del' keyword to delete
the '_name' attribute of the 'Person' instance.
"""


person = Person("John")
pprint(person.__dict__)
# [Output] {'_name': 'John'}

"""
The 'person.__dict__' has the '_name- attribute. Then,
we uses the 'del' keyword to delete the 'name' property.
Internally, python will execute the 'deleter' method that
deletes the '_name' attribute from the 'person' object.
then the 'person.__dict__' will be empty.

And if you attempt to access 'name' property again, you'll
get an error.
"""

del person.name
pprint(person.__dict__)
# [Output] {}

print(person.name)
# [Output] AttributeError: 'Person' object has no attribute '_name'.

"""
Learn how to use the 'property()' class to delete the property of an object.

[Summary]
 - Use the deleter decorator to delete a property of an instance of a class.
"""
