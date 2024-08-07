# link: https://www.pythontutorial.net/python-oop/python-overriding-method/

import re

# Introduction to overriding method


class Employee:

    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive


john = SalesEmployee("John", 5000, 1500)
print(john.get_pay())
# [Output] 5000

"""
The overriding method allows a child class to provide a specific
implementation of a method that is already provided by one
of the parent classes.

In the example above, we define a 'Employee' class.
The 'Employee' class has two instance variables 'name' and 'base_pay'.
It also has the 'get_pay()' method that returns the 'base_pay'.

Then, we define a 'SalesEmployee' class which inherits from the 'Employee' class.
The 'SaleEmployee' class has three instance attributes:
'name', 'base_pay', 'sales_incentive'.

Then, you create a new instance of the 'SalesEmployee' class and display
the 'pay' value. The 'get_pay()' method returns only the 'base_apy',
not the sum of the 'base_pay' and 'sales_incentive'.

When you call the 'get_pay()' method from the instance of the 'SalesEmployee' classs,
python executes the 'get_pay()' method of the 'Employee' class, which returns
the 'base_pay'.

To include the 'sales_incentive' in the pay, you need to redifine the 'get_pay' method
in the 'SalesEmployee' class.
"""


class ASalesEmployee(Employee):

    def __init__(self, name, base_Pay, sales_incentive):
        self.name = name
        self.base_pay = base_Pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive


"""
In this case, we say that the 'get_pay()' method in the 'ASalesEmployee' class override
the 'get_pay()' in the 'Employee' class.

When you call the 'get_pay()' method of the 'ASalesEmployee' class object's. Python will
call the 'get_pay()' method in the 'ASalesEmployee' class.

[Notes]
If you create an instance of the 'Employee' class, python will call the 'the_pay()' method of the 'Employee' class,
not the 'get_pay()' method of the 'ASalesEmployee' class.
"""

a_john = ASalesEmployee("John", 5000, 1500)
print(a_john.get_pay())
# [Output] 6500

a_jane = Employee("Jane", 5000)
print(a_jane.get_pay())
# [Output] 5000

"""
Learn how to use the overriding method to allow a child class
to provide a specific implementation of a method that
is provided by one of its parent classes.
"""


# Put It Together


class AEmploeyee:

    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class BSalesEmployee(Employee):

    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive


if __name__ == "__main__":

    b_john = BSalesEmployee("John", 5000, 1500)
    print(b_john.get_pay())
    # [Output] 6500

    b_jane = AEmploeyee("Jane", 5000)
    print(b_jane.get_pay())
    # [Output] 5000


# Advanced method overriding


# Define a 'Parser' class
class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)

        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(r"\d{3}-\d{3}-\d{4}", self.text)

        if match:
            return match.group(0)
        return None

    def parse(self):
        return {"email": self.email(), "phone": self.phone()}


s = "Contact us via 408-205-5663 or email@test.com"
parser = Parser(s)
print(parser.parse())
# [Output] {'email': 'email@test.com', 'phone': '408-205-5663'}


"""
The 'Parser' class has an attribute 'text' which specifies a piece of text
to be parse. Also, the 'Parser' class has three methods:

    - The 'email()' method parses a text and returns the 'email'.
    - The 'phone()' method parses a text and returns a phone number
      in the format 'nnn-nnn-nnnn' where 'n' is a number from
      0 to 9 e.g. '408-205-5663'.
    - The 'parse()' method returns a dictionary that contains two elements
      the 'email' and the 'phone'. It calls the 'email()' and the 'phone()' method
      to extract the email and the phone from the 'text' attribute.

Then we uses the 'Parser' class to extract email dan phone. But, suppose you need to
extract phone numbers in the format 'n-nnn-nnn-nnnn', which is the UK phone number
format. Also, you want to extract email like the 'Parser' class.

To do it, you can define a new class called 'UKParser' that inherits from
the 'Parser' class. In the 'UKParser' class, you override the 'phone()' method.
Then you use the 'UKParser' class  to extract a phone number (in UK format) and
email from a text.
"""


class UKParser(Parser):

    def phone(self):
        match = re.search(r"(\+\d{1}-\d{3}-\d{3}-\d{4})", self.text)

        if match:
            return match.group(0)
        return None


s2 = "Contact me via +1-650-453-3456 or email@test.co.uk"
parser = UKParser(s2)
print(parser.parse())
# [Output] {'email': 'email@test.co.uk', 'phone': '+1-650-453-3456'}

"""
In this ecample, the 'parse' calls the 'parse()' method from the parent class
which is the 'Parser' class. In turn, the 'parse()' method calls the 'email()' and
'phone()' methods.

However, the 'parser()' doesn't call the 'phone()' method of the 'Parser' class
but the 'phone()' method of the 'UKParser' class.

The reason is that inside the 'parse()' method, the 'self' is the 'parser' which
is an instance of the 'UKParser' class.

Therefore, when you call the 'self.phone()' method inside the 'parse()' method,
python will look for the 'phone()' method that is bound to the instance of
the 'UKParser'.
"""

# The overriding attributes
# single_inheritance\overriding_methods.py

"""
Learn how to use the overriding method to allow a child class to provide
a specific implementation of a method that is provided by one of
its parent classes.

[Summary]
- Method overriding allows a child class tot provide a specific implementation
  of a method that is already provided by one of its parent class.
"""
