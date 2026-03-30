class Employee:
    raise_amount =1.4
    num_of_emp = 0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay = pay
        self.email=f"{self.first}.{self.last}@gmail.com"
        Employee.num_of_emp +=1

    def fullname(self):    
        return f"{self.first} {self.last}, email:{self.email}"
    
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

obj=Employee("Rish","sherin",500.9)
obj2=Employee("riy","sherin",6000)
print(obj.fullname())
print(Employee.num_of_emp)
obj.apply_raise()
print(obj.pay)
