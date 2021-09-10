# demo classes

class Employee:

    def __init__(self, firstName: str, lastName: str, pay: int):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = self.firstName + self.lastName + "@company.com"
    
    def getName(self):
        return self.firstName + " " + self.lastName
        
    def getPay(self):
        return self.pay

    def setPay(self, newPay):
        self.pay = newPay


employee = Employee("ehsan", "sumra",150000)
print(employee.getName())
print(employee.getPay())
print(employee.email)