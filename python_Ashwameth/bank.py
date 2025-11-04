class Bank:
    def __init__(self,accNo,name,accType,balance):
        self.accNo = accNo
        self.name= name
        self.accType= accType
        self.balance = balance

    def deposit(self,amount):
      self.balance = int(self.balance) + int(amount)
      print(f"deposited {amount}")
      


    def withdraw(self,amount):
        if(int(amount) < int(self.balance)):
            self.balance = int(self.balance) - int(amount)
            print(f"{amount} withdrawed")

        else:
            print("Sorry Low Balance")

    def display (self):
        print(f"Name:{self.name} \n Balance:{self.balance} \n Accounnt Type: {self.accType} \n AccountNumber:{self.accNo}")


user = Bank(101,"Abinson","savings","60000")
print(user.display())
choice = int(input("Enter 1 for deposit and 2 for withdraw"))

if choice == 1:
    amt = int(input("Enter the amount to deposit"))
    user.deposit(amt)

else:
    amt = int(input("Enter the amount to withdraw"))
    user.withdraw(amt)
print(user.display())
