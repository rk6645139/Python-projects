class  Account:
    def __init__(self, account_name,  balance=0):
        self.account_name= account_name
        self.balance= balance

    def deposit(self, amount):
        self.balance +=amount

    def withdraw(self, amount):
        if amount>self.balance:
            return False

        self.balance -= amount
        return True
    
class PaymentApp:
    def __init__(self):
        
        self.accounts={}

    def create_account(self):
        print("\n--- Create New Account ---")

        account_name =input("Enter Account NAme:")

        initial_balance=float(input("Enter initial deposit amount"))

        if account_name in self.accounts:
            print(f"Account {account_name}already exists.")
        else:
            new_account= Account(account_name, initial_balance)
            self.accounts[account_name]= new_account
            print(f"Account '{account_name}' created successfully with balance: ${initial_balance:.2f}")

    def make_payment(self):
        print("\n---make payment---")
        from_account=input("Enter sender's account name:")

        to_account =input("enter receiver's account name:")

        amount=float(input("enter payment amount:"))

        if from_account not in self.accounts or to_account not in self.accounts:
            print("one or both accounts do not exist")

            return
        
        if self.accounts[from_account].withdraw(amount):
            self.accounts[to_account].deposit(amount)

            print(f"Payment of ${amount:.2f}made from {from_account} to {to_account}..")

    def check_balance(self):
        print("\n---check account balance:---")
        account_name=input("Enter Account name:")

        if account_name in self.accounts:
        
            balance=self.accounts[account_name].balance
            print(f"The balance for {account_name} is: ${balance:.2f}")

        else:
            print("Account doesn't exist")

    def show_menu(self):
            while True:
                print("\n---Payment App")
                print("1. Create an Account")
                print("2. Make a payment")
                print("3. Check  account balance")
                print("4. Exit")

                choice=input("Enter your choice (1-4)")

                if choice =='1':
                    self.create_account()

                elif choice=='2':
                    self.make_payment()

                elif choice=='3':
                    self.check_balance()
                elif choice =='4':
                    print("Exiting the app. GoodBye!")

                    break

                else:
                    print("invalid avoice. Please enter a valid option.")

if __name__ =="__main__":
    app=PaymentApp()
    app.show_menu()