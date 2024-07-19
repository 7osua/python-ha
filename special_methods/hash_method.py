# link: https://www.pythontutorial.net/python-oop/python-__hash__/

# Introduction to the 'hash()' function.

"""
1. First define a 'Person' class with 'name' and 'age' attributes.
2. Create two instances  of the 'Person' class.
3. Show the hashes of the 'p1' and 'p2' objects.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 25)
p2 = Person("Jane", 22)

print(hash(p1))
# [Output] 151117985940

print(hash(p2))
# [Output] 151117985835

"""
The 'hash()' function accepts an object and returns the hash value
as an integer. When you pass an object to the 'hash()' function, python
will execute the '__hash__()' method of the object.

It means that when you pass the 'p1' object to the 'hash()' function,
python will call the '__hash__()' method of the 'p1' object.
"""


class AnotherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, AnotherPerson) and self.age == other.age


members = {AnotherPerson("John", 22), AnotherPerson("Jane", 25)}  # type: ignore
# [Output] TypeError

"""
By default, the '__hash__()' method uses the objects identity and
the '__eq__()' method returns 'True' if objects are the same.
To override this default behavior, you can implement the '__eq__()'
and the '__hash__()' method.

If a class override the '__eq__()' method, the object of the class
become unhashable. This means that you won't able to use the objects
in a mapping type. For example, you will not able to use them  as keys
in a dictionary or elements in a set.

The above example implements 'AnotherPerson' class with
the '__eq__()' method. If you attempt to use the 'AnotherPerson' object
in a set, you will get an 'TypeError' error.

Also, the 'AnotherPerson' objects loses hashing because if you implement
the '__eq__()', ' the '__hash__()' is set to 'None'.
"""

hash(AnotherPerson("Jane", 23))
# [Output] TypeError

"""
To make the 'AnotherPerson' hashable, you also need to implement
the '__hash__()' method.
"""


class YetAnotherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return isinstance(other, AnotherPerson) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


another_members = {YetAnotherPerson("John", 22), YetAnotherPerson("Jane", 25)}
hash(YetAnotherPerson("John", 22))
# [Output] 22

"""
Now, you have the 'YetAnotherPerson' class that supports equality
based on 'age' and is hashable.

To make the 'YetAnotherPerson' work well in data structures like
dictionaries, the hash of the class should remain immutable.
To do it, you can make the 'age' attribute of
the 'YetAnotherPerson' class a read-only properti.
"""


class NewPerson:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def __eq__(self, other):
        return isinstance(other, NewPerson) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


new_p1 = NewPerson("Rose", 25)
new_p2 = NewPerson("Rubi", 26)

print(hash(new_p1))
# [Output] 25

print(hash(new_p2))
# [Output] 26

"""
Learn about 'has()' function and how to override
the '__hash__()' method in a custom class.

[Summary]
- By default, the '__hash__()' method uses the id of the objects
  and the '__eq__()' uses the 'is' operator for comparisons.
  If yout implement the '__eq__()' method, python sets the '__hash__()' method
  to 'None' unless you implement the '__hash__'.
"""
