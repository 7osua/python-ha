# link : https://www.pythontutorial.net/python-oop/python-class/

# Define a class


# By convention, we use capitalized names for classes in Python.
# If the class name contains multiple words,
# we use the camelcase format (e.g. "SalesEmployee").
class Person:

    pass


# To create an instance of a class,
# we use the class name with parentheses ().
person = Person()


# Objects
"""
An object is a container that contains data and functionality.
The data represents the object at a particular moment in time.
Therefore, the data of an object is called the state.
We uses attributes to model the state of an object.

The functionality represents the behaviors of an object.
Python uses functions to model the behaviors.
When a function is associated with an object, it becomes
a method of the object.

In other words, an object is a container that contains the state and methods.
"""

print(person)  # [output] : <__main__.Person object at 0x0000024D31856990>
print(id(person))  # [output] : 2530566564240
print(hex(id(person)))  # [output] : 2530566564240
print(isinstance(person, Person))  # [output] : True

"""
1. When we printing out the 'person' object,
   we will see it's name and memory address.
2. We use the 'id(...)' function to get an identity of an object.
   The id of an object is unique, the 'id(...)' function return
   the memory address of an object.
3. Then, the 'hex(...)' function converts the integer returned by
   the 'id(...)' function to a lowercase hexadecimal string prefixed
   with '0x...'.
4. The 'person' object is a instance of the 'Person' class. The 'isinstance(...)'
   function return 'True' if an object is an intance of a class.
"""


# A 'class' is also an object in python

print(Person.__name__)  # [output] : Person

print(type(Person))

"""
When we define the 'Person' class,
python will be creates an object with the name 'Person'.

The 'Person' object has attributes,
example:
we can find its name using the '__name__' attribute.

The 'Person' object ha a type of 'Type'

The 'person' class also has a behaviour.
example.
it can crete new instance
"""

another_person = Person()
print(isinstance(another_person, Person))

"""
Summary :
Learn about the classes and objects, and how to define a class.

- An object is container that countains state and behavior.
- A 'class' is a blue print to creating objects.
- A 'class' is also an object, which instance of the 'type'.
"""
