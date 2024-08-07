# link: https://www.pythontutorial.net/python-oop/python-super/

# Introduction to the 'super()'


class Employee:

    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive


sales_employee = SalesEmployee("John", 5000, 1000, 2000)
print(sales_employee.get_pay())
# [Output] 8000


class AEmployee:

    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class ASalesEmployee(AEmployee):

    def __init__(self, name, base_pay, bonus, sales_incentive):
        super.__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive


a_sales_employee = SalesEmployee("John", 1000, 1000, 2000)
print(a_sales_employee.get_pay())
# [Output] 4000

# Delegating to to other methods in parent class


class BEmployee:

    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class BSalesEmployee(BEmployee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super.__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive


b_sales_employee = SalesEmployee("John", 1000, 1000, 1000)
print(b_sales_employee.get_pay())
# [Output] 3000
