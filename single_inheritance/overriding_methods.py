# link: https://www.pythontutorial.net/python-oop/python-overriding-method/


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
