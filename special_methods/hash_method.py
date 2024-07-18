# link: https://www.pythontutorial.net/python-oop/python-__hash__/

# Introduction to the 'hash' function.


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person("John", "Doe", 25)
p2 = Person("Jane", "Doe", 22)

print(hash(p1))
print(hash(p2))


"""
Learn about 'has()' function and how to override
the '__hash__()' method in a custom class.
"""
