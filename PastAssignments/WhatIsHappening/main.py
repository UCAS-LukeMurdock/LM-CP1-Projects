#Luke Murdock, What is Happening

#__init__ it intializes you account; it turns a inputed balance and account number into your account number and your balance
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

#deposit adds the amount to the balance if the conditions are met.
    def deposit(self, amount):
        #checks if the amount that you are depositing is dipositable and deposits it if that is the case and returns true, if not it returns false
        if amount > 0:
            self.balance += amount
            return True
        return False
    
#withdraw subtracts the amount from the balance 

    def withdraw(self, amount):
        #checks if the amount that you are withdrawing can be withdrawed and then withdraws it if so and also responds true, if not, it returns false
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

#get_balance grabs your balance
    def get_balance(self):
        return self.balance

#This lets the user create their account
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

#This is where the user mainly interacts with the computer to make or affect their bank account
def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        #If the user typed in 1 then the computer would let the user create their account
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        #If the user inputs 2, 3, or 4 then they have to type in their account number
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            #checks if the account number is an actual account
            if account_number in accounts:
                account = accounts[account_number]
                #Checks if user typed 2 and if so lets them say the amount they want deposited
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    #Ckecks if the amount was deposited and then tells the user if thats the case
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    #If the amount is invalid, the computer tells the user
                    else:
                        print("Invalid deposit amount.")
                        #if the user inputs 3 then the are able to withdrawl an amount
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    #If the amount is withdrawable then the computer will withdraw it and tell the user it did
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    #If the amount is not withdrawn then it will tell the user that
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                #If the user inputted 4 then the computer will tell the user their balance
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            #Tells the user that the computer can't find their account with the account number the ygave it
            else:
                print("Account not found.")
        #If the user inputted 5 then the computer says bye and ends the program
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        #If the user didn't type 1, 2 ,3 ,4 or 5 then the comupter will say to try again
        else:
            print("Invalid choice. Please try again.")
#If the name of the file is main then the computer will run the main function
if __name__ == "__main__":
    main()