# link: https://www.pythontutorial.net/python-oop/python-__init__/

# Introduction to the __init__() method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PersonImmediately:
    def __init__(self):
        print(f"An instance (or object) of {PersonImmediately.__name__} class.")


"""
When you create a new object of a class,
python automatically call the '__init__()' method
to initialize the object's attributes.

Unlike regular methods, the'__init__()' method has
two underscores (__) on each side.
Therefore, the '__init__()' is often called dunder init.
The name comes abbreviation of the double underscores init.

The double underscores at both sides of the '__init__()' method
indicate that Python will use the method internally.
In other words, you should not explicitly call this method.

Since Python will automatically call the '__init__()' method
immediately after creating a new object, you can use
'the __init__()' method to initialize the object’s attributes.
"""

if __name__ == "__main__":
    person = Person("John", 25)
    f"I am {person.name}. I am {person.age} year old."
    # [Output] 'I am John. I am 25 year old.'
    person_immediately = PersonImmediately()
    # [Output] An instance (or object) of PersonImmediately class.

"""
When we create an instance of the 'Person' class, python
performs two things
- First, create a new instance of the 'person' class
  by setting the object's namespace such as '__dict__'
  attribute to empty '{}'.
- Second, call the '__init__()' method to inittialize
  the attributes of the newly created object.

If the '__init__' has parameters other than the self,
you need to pass the corresponding arguments
when creating a new object like the example above.
Otherwise, you'll get an error.

[Note]
Note that the '__init__' method does not create
the object but only initializes the object's attributes.
Hence, the '__init__()' is not a constructor.
"""

# The '__init__()' method with default paramaters


class AnotherPerson:
    def __init__(self, name, age=22):
        self.name = name
        self.age = age


if __name__ == "__main__":
    another_person = AnotherPerson("Jane")
    print(f"I'am {another_person.name}. I'm {another_person.age} years old.")
    # [Output] I'am Jane. I'm 22 years old.


"""
The '__init__()' method's parameters can have default values.
In this example,
the 'age' parameter has a default value of '22'.
Because we don't pass an argument to the 'AnotherPerson()' class,
the 'age' uses the default value.
"""

"""
Learn how to use the '__init__()' method
to initialize object's attributes.

[Summary]
- Use the '__init__()' method to initialize the object's
  attributes.
- The '__init__()' does not create an object but
  it automatically called after the object is created.
"""
