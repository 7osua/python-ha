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


class Person_class:
    pass


person = Person_class()
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


# Define static method

"""
A static method is not bound to class or any instances of the
class. In python, we use static methods to group logically
related functions in a class. To define a static method.

To define static method we can use the '@staticmethod' decorator.
"""


class TemperatureConverter:

    @staticmethod
    def celcius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celcius(f):
        return 5 * (f - 32) / 9


f = TemperatureConverter.celcius_to_fahrenheit(30)
print(f"{30} celcius = {f}f")

"""
- For example, we defines a class
  'TemperatureConverter' that has two static methods
  that convert from celsius to Fahrenheit and vice versa.
- To call a static method, we use the
  'ClassName.static_method_name()' syntax.
- Notice that Python does not implicitly pass an instance (self)
  as well as class (cls) as the first argument of a static method.
"""


# Single inheritance


"""
A class can reuse another class by inheriting it.
When a child class inherits from a parent class,
the child class can access the attributes and methods
of the  parent class.
"""


class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, my name is {self.name}.\n"


class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f"I am a {self.job_title}."


an_employee = Employee("John", 25, "Data Engineer")
print(an_employee.greet())
print(an_employee.counter)

another_employee = Employee("Jane", 27, "Data Analyst")
print(another_employee.greet())
print(another_employee.counter)

"""
For example, you can define
an 'Employee' class that inherits from the 'Person' class.
Inside the '__init__' method of the 'Employee' class calls
the '__init__' method of the 'Person' class
to initialize the 'name' and 'age' attributes.
The 'super()' allows a child class to access a method
of the parent class.

The 'Employee' class extends the 'Person' class
by adding one more attribute called 'job_title'.

The 'Person' is the parent class while
the 'Employee' is a child class.
To override the 'greet()' method in the 'Person' class,
we can define the 'greet()' method in the 'Employee' class.

The 'greet()' method in the 'Employee' is also called
the 'greet()' method of the 'Person' class.
In other words, it delegates to a method of the parent class.

The example above creates a new instance of
the 'Employee' class and call the 'greet()' method.
"""


"""
Learn about object-oriented programming in python,
including essential concepts such as
objects, classes, attributes, methods,
inherintences, overriding methods, etc...
"""
