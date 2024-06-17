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

# Define instances methods


"""
The following add an instance method called 'greet()'
to the 'PersonWithInstanceMethods' class.
We can use the dot notation to call the 'greet()' instance
method.
"""


class PersonWithInstanceMethods:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}."


a_new_person = PersonWithInstanceMethods("Jane", 27)
print(a_new_person.greet())


# Define class atrributes


"""
Unlike instance attributes, class attributes are shared
by all instances of the class.
They are helpful if we want to define a class constants or
variables that keep track of the number of instance of a class.
"""


class PersonWithClassAttributes:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        PersonWithClassAttributes.counter += 1

    def greet(self):
        return f"Hi it is {self.name}"


"""
- We can access the 'counter' attribute from
  the 'PersonWithClassAttributes' class.
- We also can access the 'counter' attribute from
  any instances of the 'PersonWithClassAttributes'
  class.
- To make the 'counter' variable more useful,
  we can increase its value by one once an object is created.
  To do it, we increase the 'counter' class attribute in
  the '__init__()' method.
"""
print(PersonWithClassAttributes.counter)  # counter = 0
another_person = PersonWithClassAttributes("Jhonny", 25)  # counter = 1
print(another_person.counter)
yet_another_person = PersonWithClassAttributes("Jhonny", 25)  # counter = 2
print(yet_another_person.counter)


# Define class method

"""
Like a class attributes, a class method is shared by all instances of the class.
The first argument of a class method is the class itself.
By convention, its name 'cls'. Python automatically passes this argument
to the class method.

Also, we use the '@classmethod' decorator to decorate a class method.
"""


class PersonWithClassMethod:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        PersonWithClassMethod.counter += 1

    def greet(self):
        return f"Hi, it is {self.name}."

    @classmethod
    def create_anonymous(cls):
        return PersonWithClassMethod("Anonymous", 22)


"""
The following example defines a class method that returns an
anonymous Person object.
Then shows how to call the create_anonymous() class method
"""

a_person = PersonWithClassMethod("John", 24)
print(a_person.counter)
another_person = PersonWithClassMethod("Jane", 23)
print(another_person.counter)
anonim_person = PersonWithClassMethod.create_anonymous()
print(anonim_person.counter)
print(anonim_person.name)


"""
Learn about object-oriented programming in python,
including essential concepts such as
objects, classes, attributes, methods,
inherintences, overriding methods, etc...
"""
