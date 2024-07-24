# link: https://www.pythontutorial.net/python-oop/python-properties/

# Introduction to class properties

from pprint import pprint


"""
The following defines a 'Person' class that has two attributes
'name' and 'age', and created a new instance of the 'Person' class.

Since 'age' is the instance attribute of the 'Person' class, you can
assign it a new value.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 18)
john.age = -1

"""
The assign above is technically valid. However, the 'age' semantically
incorrect.

To ensure the 'age' is not zero or negative, you use the 'if' statement
to add a check.

    age = 0
"""

age = 0
if age <= 0:
    raise ValueError("The age must be positive")
else:
    john.age = age

# [Output] ValueError: The age must be positive


class NotValid:
    def __init__(self, name, age):
        self.name = name
        if age <= 0:
            raise ValueError("The age must be positive")
        else:
            self.age = age


jane = NotValid("Jane", -1)
# [Output] ValueError: The age must be positive

"""
[Note]
You need to do this every time you want to assign a value to
the 'age' attribute. This is repetitive and difficult to maintain.

To avoid this repetition, you can define a pair of methods called
getter and setter.
"""


# Introduction to Getter and Setter


class NewPerson:

    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    def get_age(self):
        return self._age


"""
The getter and the setter methods provide an interface for
accessing an instance attribute:
    - The getter returns the value of an attribute
    - The setter sets a new value for an attribute

In example above we can make the 'age' attribute 'private' (by convention)
and define a getter and a setter to manipulate the 'age' attribute.

In the 'NewPerson' class, the 'set_age()' is the setter and
the 'get_age()' is the getter. By convention the getter and setter
have the following name:
    - get_<attribute>()
    - set_<attribute>()

In the 'set_age()' method, we raise a 'ValueError' if the 'age'
is less than or equal to zero. Otherwise, we assign the 'age' argument
to the '_age' attribute.

The 'get_age()' method return the value of the '_age' attribute.

In the '__init__()' method, we call the 'set_age()' setter method
to initialize the '_age' attribute.

The following attempts to assign an invalid value to the 'age' attribute.
Then, python issued a 'ValueError' as expected as an invalid value.
"""


john = NewPerson("John", 18)
john.set_age(-18)
# [Output] ValueError: The age must be positive

"""
The code works just fine. But it has a backward compability issue.
Suppose you realesed the 'NewPerson' class for while and other developers
have been already using it. Now you add the getter and setter, all the code
that uses the 'NewPerson' class won't work anymore.

To define a getter and setter method while achieving backward compability,
you can use the 'property()' class.
"""


# The 'property()' class


class NewPersonWithProperty:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError("The age must be positive")
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age, fset=set_age)


"""
The 'property()' class returns a property object. The 'property()' class
has the following syntax.

    property(fget=None, fset=None, fdel=None, doc=None)

The property() has the following parameters:

    - fget is a function to get the value of the attribute, or the getter method.
    - fset is a function to set the value of the attribute, or the setter method.
    - fdel is a function to delete the attribute.
    - doc is a docstring i.e., a comment.

In above example, we define a 'NewPersonWithProperty' class
using the 'property()' function to define the 'age' property for
the 'NewPersonWithProperty' class.

In the 'NewPersonWithProperty' class, we create a new property object
by calling the 'property()' and assign the property object to
the 'age' attribute.

[Note]
The 'age' is a class attribute, not an instance attribute.
The following shows that the 'NewPersonWithProperty.age' is
a 'property' object.
"""

print(NewPersonWithProperty.age)  # type: ignore
# [Output] <property object at 0x000001EF2586FBF0>

"""
The following creates a new instance of the 'NewPersonWithProperty' class
and access the 'age' attributes.

The 'john.__dict__' stores the instance attributes of the 'john' object.
The following shows the contents of the 'john.__dict__'.
"""
john = NewPersonWithProperty("John", 22)
print(john.__dict__)
# [Output] {'name': 'John', '_age': 22}

john.age = -18
# [Output] ValueError: The age must be positive

"""
As you can see clearly from the output, the 'john.__dict__' doesn't have
the 'age' attribute of the 'john' object.

In this case, python lookup th 'age' attribute in the 'john.__dict__' first.
Because pyhton doesn't find the 'age' attribute in the 'john.__dict__', it'll
then find the 'age' attribute in the 'NewPersonWithProperty.__dict__'.

The 'NewPersonWithProperty.__dict__' stores the class attributes of
the 'NewPersonWithProperty' class. The following shows the contents of
the 'NewPersonWithProperty.__dict__'.
"""

pprint(NewPersonWithProperty.__dict__)

# [Output]
# mappingproxy({'__dict__': <attribute '__dict__' of 'NewPersonWithProperty' objects>,
#               '__doc__': None,
#               '__init__': <function NewPersonWithProperty.__init__ at 0x000001EF258A0360>,
#               '__module__': '__main__',
#               '__weakref__': <attribute '__weakref__' of 'NewPersonWithProperty' objects>,
#               'age': <property object at 0x000001EF2586FBF0>,
#               'get_age': <function NewPersonWithProperty.get_age at 0x000001EF258A0540>,
#               'set_age': <function NewPersonWithProperty.set_age at 0x000001EF258A04A0>})

john.age = 19

"""
Because python finds the 'age' attribute in the 'NewPersonWithProperty.__dict__',
it'll call the 'age' property object.

When you assign a value to the 'age' object. Python will call the function assigned
to the 'fset' argument, which is the 'set_age()' method.

similiarly when you read from the 'age' property object, python will execute
the function assigned to the 'fget' argument, which is the 'get_age()' method.

By using the 'property()' class, we can add a property to a class while
maintaining backward compatibility. In practice, you will define the attributes
first. Later, you can add property to the class if needed.
"""


"""
Learn about the 'property' class and how to use it to define properties
for class.

[Summary]
    - Use the 'property() class to define property for a class.
"""
