#Creating a Banking System using OOP

#Parent Class User()

#Holds details about a User

#Has a function to show their details(show_details)

#Child Class Bank()

#Stores Details about the Users Account Balance

#Allows for Deposits, Withdrawal , View_balance

if __name__ == "__main__":
    
    class User():
        def __init__(self,name,passcode):
            self.name = name
            self.passcode = passcode

        def show_details(self):
            print("Personal Details")
            print("")
            print("Name",self.name)
            print("Passcode",self.passcode)

        #Creating a child class
    class Bank(User):
        def __init__(self,name,passcode):
            super().__init__(name,passcode)
            self.balance = 0

        def deposit(self,amount):
            self.amount = amount
            self.balance = self.balance + self.amount
            print("Account balance has been updated : $",self.balance)

        def withdraw(self,amount):
            self.amount = amount
            if self.amount > self.balance:
                print("Insufficient Funds | Balance Available: $", self.balance)
            else:
                self.balance = self.balance - self.amount
                print("Account has been updated: $",self.balance)

        def view_balance(self):
            self.show_details()
            print("Account Balance is : $", self.balance)
    

