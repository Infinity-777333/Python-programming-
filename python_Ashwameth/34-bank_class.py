class bank:
    def __init__(self,ac_no,name,ac_type,balance=0):

            self.ac_no=ac_no

            self.name=name

            self.ac_type=ac_type

            self.balance=balance


    def deposit(self,amount):
        self.balance=self.balance+amount
        print(amount," is deposited")
        print("Your current balance after deposit:", self.balance)

    def withdraw(self,amount):
            
            if(self.balance<amount):
                print("\nsorry, insufficient balance!\n")
                print("Your current balance is",self.balance,"\n")
            else:
                self.balance=self.balance-amount
                print(amount," is withdrawed \n Your current balance after withdrawal", self.balance)

    def display(self):
            print("\n\nAccount number:",self.ac_no)
            print("Name of account holder:",self.name)
            print("Account type:",self.ac_type)
            print("Balance:",self.balance)

            
print("***Enter the details of user***\n")
ac_no=int(input("Enter the Account number:"))
name=input("Enter the  name of user:")
ac_type=input("Enter the account type (Savings/Current):")
user=bank(ac_no,name,ac_type)

print("\n***Account deatails***")
user.display()

while True:
    print("\n***Select the operation ***")
    print("1. Deposit\n2. Withdraw\n3. Display\n4. Exit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        amount=int(input("\nEnter the amount to be deposited:"))
        user.deposit(amount)
    elif choice==2:
        amount=int(input("\nEnter the amount to be withdrawn:"))
        user.withdraw(amount)
    elif choice==3:
        user.display()
    elif choice==4:
        print("\nThank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.")
        
