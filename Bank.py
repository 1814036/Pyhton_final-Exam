from Users import User
import random
class Bank:
    acc_type=["Saving","Current"]
    
    def __init__(self,name) -> None:
        self.name=name
        self.accounts={}
        self.total_loans=0
        self.loan_feature_enabled=True
        self.__bank_balalce= 100000
        
    def create_account(self,name,email,address,account_type):
        account_number=random.randint(100000,500000)
        if account_type.capitalize() in self.acc_type:
            self.accounts[account_number]=User(name,email,address,account_type,account_number)
            print("Account Create Sucessful")
            return account_number
        else:
            print(" Account type doesn't match!")
            
    # Getter Methode
    @property
    def get_bank_balance(self):
        return self.__bank_balalce
    
    # Settere Methode
    @get_bank_balance.setter
    def get_bank_balance(self,amount):
        self.__bank_balance+=amount
        
        
    # Delete Account 
    def delete_account(self,account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Accounted Delete Successfull")
        else:
            print("Account doesn't Exist")
            
    def account_list(self):
        print("Account No\t Name\tEmail\tAccount_type")
        for key,user in self.accounts.items():
            print(f'{key}\t{user.name}\t{user.email}\t{user.account_type}')
            
    def loan_feature_toggle(self):
        self.loan_feature_enabled =not self.loan_feature_enabled
        
        if self.loan_feature_enabled==True:
            print("Loan Feature Enabled")
            
        else:
            print("Loan Feature Disabled")