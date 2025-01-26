class Atm:

    #constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""
                           Hell0, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")
    
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("pin set successfully")
    
    def deposite(self):
        temp = input("enter your pin")
        if(temp == self.pin):
            amount = int(input("enter amount"))
            self.balance += amount
        else:
            print("invalid pin")
    
    def withdraw(self):
        temp = input("enter your pin")
        if(temp == self.pin):
            amount = int(input("enter amount to withdraw"))
            if(amount <= self.balance):
                self.balance -= amount
                print("withdraw successfuly")
            else:
                print("not possible")
        else:
            print("invalid pin")
    
    def check_balance(self):
        temp = input("enter pin")
        if(temp == self.pin):
            print(self.balance)
        else:
            print("invalid pin")

def main():
    sbi = Atm()
    print("byeye")