# link: https://www.pythontutorial.net/python-oop/python-property-decorator/


# Introduction to the property decorator

"""
Defines a 'Person' class with two attributes 'name' and 'age'.
Also, the following defines a getter for the 'age' attribure,
with the 'property()' class.
The 'property()' accepts a getter and returns a property object.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age)


"""
The following creates an instance of the 'Person' class and
get value of the 'age' property via the instance.
Also, you can call the 'get_age()' method of the 'Person' object
directly.

So to get the 'age' of the 'Person' object, you can use either
the 'age' property or the 'get_age()' method. This creates an
unnecessary redundancy.
"""

john = Person("John", 25)
print(john.age)
# [Output] 25

print(john.get_age())
# [Output] 25

"""
To avoid thi redundancy, you can rename the 'get_age()' method
to the 'age()' method.
"""


class AnotherPerson:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def age(self):
        return self._age

    age = property(fget=age)  # type: ignore


another_john = AnotherPerson("John", 27)
print(another_john.age)
# [Output] 27


"""
The 'property()' accepts a callable 'age' and return a callable.
Therefore, it is a decorator. Therefore, you can use the '@property' decorator
to decorate the 'age()' method.
So by using the '@property' decorator, you can simplify the property definition
for a class.
"""


class NewPerson:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age


jane = NewPerson("Jane", 26)
print(jane.age)
# [Output] 26


# Setter decorators

"""
To assign the 'set_age()' to the 'fset' of the 'age' property object,
you call the 'setter()' method of the 'age' property object. Like the following.

The 'setter()' method accepts a callable and returns another callable
(a 'property' object). Therefore, you can use the decorator '@age_setter'
for the 'set_age()' method.
"""


class APerson:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")

        self._age = value

    age = age.setter(set_age)


a_john = APerson("John", 20)
print(a_john.age)
# [Output] 20


class BPerson:
    def __init__(self, name, age):
        self.name = (name,)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")

        self._age = value


b_john = BPerson("John", 23)
print(b_john.age)
# [Output] 23

"""
Now, you can change the 'set_age()' method to the
'age()' method and use the 'age' property in
the '__init__()' method.

The following example use the '@property' decorators to
create the 'name' and 'age' properties in the 'Person' class.
"""


class CPerson:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("The age must be positive")
        self._age = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be empty!")
        self._name = value


c_john = CPerson("John", 30)
print(str(c_john.age) + " " + c_john.name)
# [Output] 30 John

"""
To summarize, you can use decorators to create a property
using the following pattern:

    class MyClass:
        def __init__(self, attr):
            self.prop = attr

        @property
        def prop(self):
            return self.__attr

        @prop.setter
        def prop(self, value):
            self.__attr = value

In this pattern, the '__attr' is the private attribute and
the 'prop' is the property name.
"""


"""
Learn about property decorator '@property' and learn how it works.

[Summary]
- Use the '@property' decorator to create a property for a class.
"""
