# link: https://www.pythontutorial.net/python-oop/python-__bool__/


# Introduction to the '__bool__' mehthod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    person = Person("John", 22)
    print(bool(person))
    # [Output] True

"""
An object of a custom class is associated with a boolesn
value. By default, it evaluates to 'True'.

In above example, we define the 'Person' class, instantiate
an object, and show its boolean value. As expected, the 'person' object
is 'True'.

To override thos default behavior, you implement the '__bool__' special
method. The '__bool__' method must return a boolean value, 'True' or 'False'.

For example, suppose that you want the 'person' object to evaluate
'False' if the 'age' of a person is under 18 or above 65.

Below, in this example, the '__bool__()' method returns 'False' if the 'age'
is less than 18 or greater than 65. Otherwise, it returns 'True'.
The 'AnotherPerson' object has the 'age' value of 16 therefore it returns 'False'
in this case.
"""


class AnotherPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age > 18 or self.age < 65:
            return False

        return True


if __name__ == "__main__":
    another_person = AnotherPerson("Jane", 16)
    print(bool(another_person))
    # [Output] False


# Introduction to the '__len__()' method.

"""
If a custom class doesn't have the '__bool__()' method, python
will look for the '__len__()' method. If the '__len__()' method
is zero, the object is 'False'. Otherwise, it is 'True'.

If a class doesn't implement the '__bool__()' and the '__len__()' method,
the object of the class will evaluate to 'True'.

The following defines a 'Payroll' class that doesn't implement '__bool__()'
but the '__len__()' method.
"""


class Payroll:

    def __init__(self, length):
        self.length = length

    def __len__(self):
        print("len was called ...")
        return self.length


if __name__ == "__main__":
    payroll = Payroll(0)
    print(bool(payroll))
    # [Output] False

    payroll.length = 10
    print(bool(payroll))
    # [Output] True

"""
Since the 'Payroll' class doesn't override the '__bool__()' method,
python looks for the '__len__()' method when evealuating the 'Payroll' objects
to boolean value.
"""

"""
Learn how to implement the '__bool__()' method to return boolean
values for object of a custom class.

[Summary]
1. All object of a custom classes return 'True' by default.
2. Implement the '__bool__()' method to override the default.
   The '__bool__()' method must return either 'True' or 'False'.
   If a class doesn't implement the '__bool__()' method,
   python will use the result of the '__len__()' method. If
   the class doesn't implement both methods, the object will 'True'
   by default.
"""
