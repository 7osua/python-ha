# link: https://www.pythontutorial.net/python-oop/python-private-attributes/

# Intorduction to encapsulation

"""
Encapsulation is one of the four fundamental concepts in
object-oriented programming including :

- abstraction
- encapsulation
- inheritance
- polymorphism

Encapsulation is the packing of data and functions that work on that data
within a single object. By doing so, you can hide the internal state of
the object from outside. This is known as Information Hiding.

A class is an example of encapsulation. A class bundles data and methods
into a single unit. A class provides the access to its attributes via methods.

The idea of information hiding is that if you have an attribute that isn't
visible to the outside, you can control the access to its value to make sure
your object is always a valid state.
"""


# Python encapsulation


# Define a 'Counter' class
class Counter:
    """
    The 'Counter' class has one attribute called 'current'
    which default to zero
    current: an interger
    """

    def __init__(self):
        """
        Parameter:
            self: self@counter
        """
        self.current = 0

    def increment(self):
        """
        Increase the value of the 'current' attribute by one
        Parameter:
            current: an integer
        """
        self.current += 1

    def value(self):
        """
        Return the 'current' value of the 'current' attribute
        Returns:
            current: an integer
        """
        return self.current

    def reset(self):
        """
        Sets the value of the 'curent' attribute to zero.
        Parameter:
            current: an integer
        """
        self.current = 0


# Create a new instance of the 'Counter' class.
counter = Counter()

# Showing the 'current' value of the 'counter' object to the screen
print(counter.value())
# [Output] 0

# Calls the 'increment()' method three time
counter.increment()
counter.increment()
counter.increment()

# Showing the 'current' value of the 'counter' object to the screen
print(counter.value())
# [Output] 3

"""
In above example the class works perfectly fine.
But has one issue, from the outside of the 'Counter' class,
you still can access the 'current' class attribute and change it
to whatever you want. For example:
"""

counter.current = -99
counter.increment()

print(counter.value())
# [Output] -98

"""
In this example, after created an instance of the 'Counter' class,
then you set the value of the 'current' attribute to an invalid value -99.
finally you call the 'increment()' method 1 time.

As you can see, we modifying the 'current' class attribute outside the class.
So how do you prevent the 'current' class attribute from modifying outside
of the 'Counter' class?

That's why private attributes come into play.
"""

# Private attributes


class CounterWithPrivateAttr:
    """
    The '_attribute' should not be manipulated and
    may have a breaking change in the future.
    The following redefines the 'Counter' class with the 'current' as
    a private attribute by convention.
    """

    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


"""
- Private attributes can be only accessible from the methods of the class.
  In other words, they cannot be accessible from outside of the class.
- Python doesn't have a concept of private attributes.
  In other words, all attributes are accessible from the outside of a class.
- By convention, you can define a private attribute
  by prefixing a single underscore (_).
"""

new_counter = CounterWithPrivateAttr()

new_counter.increment()
print(new_counter.value())
# [Output] 1

print(new_counter._current)
# [Output] 1

new_counter._current = 4
print(new_counter.value())
# [Output] 4


# Name mangling with double undescores


# The following example redefines the 'Counter' class
# with the '__current' attribute
class CounterWithManglingName:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


another_counter = CounterWithManglingName()

"""
If you prefix an attribute name with double underscores (__) like this.

    __attribute

Python will automatically change the name of the '__attribute' to

    _Class__attribute

This is called the name mangling.
"""

another_counter.increment()
print(another_counter.value())
# [Output] 1

"""
By doing this, you cannot access the '__attribute' directly from
the outside of a class like:

    instance.__attribute

However, you still can access it using the '_Class__attribute' name

    instance._Class__attribute

Now, if you attempt to access '__current' attribute, you'll get an error
"""

# print(another_counter.__current)  # AttributeError

print(another_counter.value())
# [Output] 1

another_counter._CounterWithManglingName__current = 99  #  type: ignore
print(another_counter._CounterWithManglingName__current)  #  type: ignore
# [Output] 99

another_counter.increment()
print(another_counter.value())
# [Output] 100


"""
Learn about encapsulation and how to use private attributes to
accomplish encapsulation in python.

[Summary]

- Encapsulations is the packing of data and methods into a class
  so that you can hide the information and restrict access from outside.
- Prefix an attribute with a single underscore (_) to make it
  private by convention.
- Prefix an attribute with double underscore (__) to use the name mangling.
"""
