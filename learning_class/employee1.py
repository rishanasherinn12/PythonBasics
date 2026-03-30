class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@company.com"

    def fullname(self):
     
        return f"{self.first} {self.last}, email:{self.email}"

obj=Employee("Rish","sherin")
print(obj.fullname())
