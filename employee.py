"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthlySalary = 0, hourlyContract = 0, hourlyContractRate = 0, commissionContracts = 0, commissionContractRate = 0, bonusCommision = 0):
        self.name = name
        self.monthlySalary = monthlySalary
        self.hourlyContract = hourlyContract
        self.hourlyContractRate = hourlyContractRate
        self.commisionContracts = commissionContracts
        self.commisionContractRate = commissionContractRate
        self.bonucCommission = bonusCommision
        self.pay = self.monthlySalary + self.hourlyContract*self.hourlyContractRate + self.commisionContracts*self.commisionContractRate + self.bonucCommission


    def get_pay(self):
        return self.pay

    def __str__(self):
        self.str1 = "" + self.name + " works on a"
        self.sl = []
        self.str2 = ""
        if(self.monthlySalary):
            self.s1 = " monthly salary of " + str(self.monthlySalary)
            if(self.str2 != ""):
                self.str2 += " and"
            self.str2+= self.s1
        if(self.hourlyContract):
            self.s2 = " contract of " + str(self.hourlyContract) + " hours at " + str(self.hourlyContractRate) + "/hour"
            if(self.str2 != ""):
                self.str2 += " and"
            self.str2+= self.s2
        if(self.commisionContracts):
            self.s3 = " recieves a commission for " + str(self.commisionContracts) + " contract(s) at " + str(self.commisionContractRate) + "/contract"
            if(self.str2 != ""):
                self.str2 += " and"
            self.str2+= self.s3
        if(self.bonucCommission):
            self.s4 = " receives a bonus commission of " + str(self.bonucCommission)
            if(self.str2 != ""):
                self.str2 += " and"
            self.str2+= self.s4
        self.str2+= "."
        self.str1+= self.str2 + " Their total pay is " + str(self.pay)
        return self.str1


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 0, 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 0, 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0,0,0,0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 0, 120, 30, 0,0, 600)
