class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.email=f"{self.first}{self.last}@company.com"
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True

import datetime
my_date = datetime.date(2016,7,3)
print(Employee.is_workday(my_date))


