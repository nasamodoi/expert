class Bank_account:
    def __init__(self,name,acc,no,balance):
        self.name = name
        self.acc = acc
        self.balance = balance
    def deposit(self,amount):
        if amount < 5000:
            print("deposit not successfull please add amount")
        else:
            print ("deposit successfull")
            self.balance +=amount
            print("new balance", self.balance)
    def withdraw(selt,amount):
        if amount > self.balance:
             print("salio lako halitoshi")
        else:
            self.balance -= amount
            print(f"hongera umefanikiwa kutoa kiasi. ", "salio lako jipya ni:  ", {self.balance})
Bank_account1 = Bank_account("Nassor",001,10000000)
Bank_account2 = Bank_account("Sale",002,20000000)
print(amount.name)
