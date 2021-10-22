#this program is to demo the use of classes
class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        self.bonus = 0

    def getPay(self):
        return self.pay

    def setPay(self,pay):
        self.pay=pay
        
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def getBonus(self):
        return self.bonus
    
    def setBonus(self, percentage: float):
        self.bonus = round((float(self.pay) * percentage),2)
    
    def getBonus(self):
        return self.bonus

    def __str__(self):
       
       return '\n'+'-'*21+ '\nEmployee name: '+self.fullName()+'\nEmployee pay: ' +str(self.pay)+'\nEmployee bonus: ' +str(self.bonus)

