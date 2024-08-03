# link: https://www.pythontutorial.net/python-oop/python-inheritance/


# Introduction to the inheritance


class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"


class Employee:

    def __init__(self, name, job_title):
        self.name = name
        self.jobt_title = job_title

    def greet(self):
        return f"Hi, it's {self.name}"


"""
Inheritance allow a class to re-use the logic of an existing class.
Suppose you have the 'Person' class.
The 'Person' class has the 'name' attribute and the 'greet()' method.
Then, you want to define the 'Employee' that is similiar to
the 'Person' class.

The 'Employee' class has two attributes 'name' and 'job_title'. It also
has the 'greet()' method that is exactly the same as the 'greet()' method
of the 'Person' class.
"""


class AEmployee(Person):

    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title


"""
To reuse the 'greet()' method from the 'Person' class in the 'Employee' class,
you can create a relationship between the 'Person' and 'Employee' classes.
To do it, you use the inheritance so that the 'Employee' class inherits from
the 'Person' class.

Then, we redefines the 'Employee' ('AEmployee') class that inherits from the 'Person' class.

By doing this, the 'Employee' class behaves the same as the 'Person' class
without redefine the 'greet()' method.

This is a single inheritance because the 'Employee' inherits from a single
class('Person'). Note, that python also supports multiple inheritances
where a cllass inherits from multiple classes.
"""

a_employee = AEmployee("John", "Python Developer")
print(a_employee.greet())
# [Output] Hi, it's John

"""
Since the 'Employee' inherits attributes and methods of the 'Person' class,
you can use the instance of the 'Employee' class as if it were an instance of
the 'Person' class.

In the example above, you creates a new instance of the 'Employee' class and
call the 'greet()' method.
"""

# Inheritance terminology

"""
The 'Person' class is the parent class, the base class, or the super class
of the 'Employee' class.
Then, the 'Employee' class is a child class, a derived class, or a subclass
of the 'Person' class.

The 'Employee' class derives from, extends, or subclass the 'Person' class.

The relationship between the 'Employee' class and the 'Person' class is
'IS-A' relationsip. In other words, an empleyee IS-A person.
"""


# 'type' vs. 'isinstance()'


a_person = Person("Jane")
print(type(a_person))
# [Output] <class '__main__.Person'>

a_employee = AEmployee("John", "Python Developer")
print(type(a_employee))
# [Output] <class '__main__.AEmployee'>

"""
The above example shows the type of instances of the 'Person' and
the 'Employee' classes. To check if an object is an instance of a class,
you use the 'isinstance()' method.
"""

print(isinstance(a_person, Person))
# [Output] True

print(isinstance(a_employee, Person))
# [Output] True

print(isinstance(a_employee, AEmployee))
# [Output] True

print(isinstance(a_person, AEmployee))
# [Output] False

"""
As clearly shown in the [Output]

- The 'a_person' is an instance of the 'Person' class.
- The 'a_employee' is an instance of the 'AEmployee' class. It's also
  an instance of the 'Person' class.
- The 'a_person' is not an instance of the 'AEmployee' class.

[Note]
In practice, you'll often use the 'isinsatance()' function to check
wheter an object has certain methods. Then, you'll call the methods
of that object.
"""

# 'issubclass()' function

print(issubclass(AEmployee, Person))
# [Output] True

"""
To check if a class is a subclass of another class, you use
the 'issubclass()' function.
Below examples, defines the 'SalesEmployee' class that inherits from
the 'AEmployee' class.
"""


class SalesEmployee(AEmployee):
    pass


"""
The 'SalesEmployee' is the subclass of the 'AEmployee' class. It's also
a subclass of the 'Person' class as showing in the following.

[Notes]
Note that when you define a class that doesn't inherit from any class,
it'll implicitly inherit from the built-in object class.

For example, the 'Person' class inherits from the 'object' class implicitly.
Therefore, it is a subclass of the 'object' class.

In other words, all classes are subclasses of the 'object' class.
"""

print(issubclass(SalesEmployee, AEmployee))
# [Output] True

print(issubclass(SalesEmployee, Person))
# [Output] True

print(issubclass(Person, object))
# [Output] True


"""
Learn about inheritance and how to use the inheritance to reuse code
from an existing class.

[Summary]
- Inheritance allows a class to reuse existing attributes and methods
  of another class.
- The class that inherits from another class is called a child class,
  a subclass, or a derived class.
- The class from which other classes inherit is call a parent class,
  a superclass, or a base class.
- Use the 'isinstance()' function to check if an object is an instance
  of a class.
- Use the 'issubclass()' function to check if a class is a subclass of
  another class.
"""
