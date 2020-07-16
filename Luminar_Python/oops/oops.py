class Bank:
    #Different type of variables:
    #Instance variable instance means related to object.
    #local variable
    #class or static variables
    #self is used for defining instance varibale.
    bankname="SBI" #decalred as static varibale
    def createAccount(self,acno,name,actype):
        self.acno=acno
        self.name=name
        self.actype=actype
        self.balance=3000
        #self.bankname="SBI"#making this static so every object can access.


    def printValues(self):
        print(self.acno)
        print(self.name)
        print(self.actype)
        print(self.balance)
        print(Bank.bankname)#calling static varibale by class name

ob=Bank()
ob.createAccount(1000765,"Midhun","Savings")
ob.printValues()
