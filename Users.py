# Creat class Users
class User:
    def __init__(self,name,email,address,account_type,account_number) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.account_number=account_number
        self.__balance=0
        self.transaction_history =[]
        self.loans_taken=0
    
    def deposit(self,amount,bank):
        self.__balance+=amount
        bank.get_bank_balance=amount
        self.transaction_history.append(("Deposit",amount))
        print("Deposit Successfull")

    def withdraw(self,bank,amount):
        if self.__balance >= amount:
            if bank.get_bank_balance > amount:
                self.__balance-=amount
                bank.get_bank_balance -= amount
                self.transaction_history.append("Withdraw", amount)
                print(f"Withdraw Successful account balance {self.__balance}")
                
            else:
                print("Bank is Bankrupt.")
                
        else:
            print("Withdraw Amount Excedded")
    def check_available_balace(self):
        print(f'Available Balance:{self.__balance}')
        
        
    def check_transaction_history(self):
        print("Transaction History")
        print("\nActions \t\t Amiunt")
        for key, value in self.transaction_history:
            print(f'{key} \t\t\t {value}')
        
        
    def take_loan_from_bank(self,amount,bank):
        # Most two time
        if not bank.loan_feature_enabled:
            print("***Loan Features Is Currently Disabled***")
        elif self.loan_tekes >=2:
            print("Maximum Loan Limit Is Exceeded")
            
        else:
            self.__balance+=amount
            bank.get_bank_banlance=-amount
            self.loans_takes +=1
            self.transaction_history.append(("Loan",amount))
            print("Loan Sucessful Done")
    def transfer_balance(self,amount,others_account, bank):
        if others_account not in bank.accounts:
            print("Account Does Not Exist")
        elif amount >self.__balance:
            print("Insufficient Balance")
            
        else:
            self.__balance-=amount
            bank.accounts[others_account].__balance += amount
            self.transaction_history.append((f'Transfer({others_account})', amount))
            bank.accounts[others_account].transaction_history.append(((f'Received ({self.account_number}')), amount)
            print("Balance Transfer Sucessful")
    