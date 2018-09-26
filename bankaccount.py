class BankAccount:
    def __init__(self,first_name,last_name,middle_name,account_type,account_balance,account_status):
        self.firstname = first_name
        self.lastname = last_name
        self.middlename = middle_name
        self.accounttype = account_type
        self.balance = 100
        self.status = "Opened"

    def deposit_withdraw(self):
        add_subtract = input("Would you like to make a deposit or withdrawal: ")
        if add_subtract == "deposit":
            funds = int(input("How much would you like to deposit: "))
            new_balance = self.balance + funds
            return new_balance

        if add_subtract == "withdrawal":
            funds = int(input("How much would you like to withdraw: "))
            new_balance = self.balance - funds
            if new_balance < 0:
                final = new_balance - 35
                return final

person1 = BankAccount("John","Doe","D","Checking Account","15,000","Open")

print("Your new balance is: ",person1.deposit_withdraw())
