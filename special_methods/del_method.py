# link: https://www.pythontutorial.net/python-oop/python-__del__/

# Introdection to the '__del__()' method.

"""
In python, the garbage collector manages memory automatically.
The garbage collector will destroy the objects that are not referenced.

If an object implements the '__del__' method, python calls the '__del__' method
right begore the garbage collector destroys the object.

However, the garbage collector determines when to destroy the object.
Therefore, it determines when the '__del__' method will be called.

[Note]
The '__del__' method is sometimes reffered to as a clas finalizer.
That '__del__' method is not the destructor because the garbage collector
destroys the object, not the '__del__' method.
"""

# the '__del__' method example


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__ was called")


if __name__ == "__main__":
    person = Person("John Doe", 23)
    person = None
    # [Output] __del__ was called

"""
The example above, defines a 'Person' class with
the special '__del__' method, create a new instance of the 'Person',
and it to 'None'.

When we set the 'person' object to 'None', the garbage collector destroys
it because there is no reference. Therefore, the '__del__' method
was called.

If you use the 'del' keyword to delete the 'person' object,
the '__del__' method is alsi called.

However, the 'del' statement doesn't cause a call to the '__del__' method
if the object has a reference.
"""


class AnotherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("__del__ was called")


if __name__ == "__main__":
    another_person = AnotherPerson("Jane", 25)
    del another_person
    # [Output] __del__ was called


# The '__del__' memthod pitfalls

"""
Python calls the '__del__' method when all object reference are
gone. And you cannot control it in most cases.

Therefore, you should not use the '__del__' method to clean uo
the resources. It's recommended to use the context manager.

If the '__del__' contains references to objects, the garbage collector
will also destroy these objects when the '__del__' is called.

If the '__del__' references the global objects, it may create unexpected
behaviors.

If an exception occurs inside the '__del__' method, python does not raise
the exception but keeeps it silent.

Also python sends the exception message to the 'stderr'. Therfore,
the 'main' program will be able to be awate of the exceptions during
the finalization.

In practice, you'll rarely use the  '__del__' method.
"""

"""
Learn about the '__del__' special method and understand how it works.

[Summary]
- Python calls the '__del__()' method right before the garbage collector
  destroy the object.
- The garbage collector destroys an object when there is no reference to
  the object.
- Exception occurs inside the '__del__' method is not raised but silent.
- Avoid using the '__del__' for clean up resources.
  Use the context manager instead.
"""
