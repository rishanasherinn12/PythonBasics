class Employee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f"{self.first}{self.last}@company.com"

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

# emp_1 = Employee('corey','schafer',5000)
# emp_2 = Employee('john','doe',6000)

emp_str_1 = 'jane-rose-6900'
emp_str_1 = 'arun-kumar-3000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)