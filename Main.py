from Admin import Admin
from Bank import Bank
from Users import User


IBBL = Bank("Islami Bank Limited")
admin= Admin(IBBL)
users= {}

def admin_panel():
    while True:
        print("\n Admin Menu")
        print("1.Create User Account")
        print("2.Delete User Account")
        print("3.View All Account")
        print("4.View Total Bank Balance")
        print("5.View Total Loans Given")
        print("6.Toggle Loan Feature")
        print("7. Exit")
        
        ch = int(input("Enter Choice: "))
        if ch==1:
            name=input("Enter Name: ")
            email=input("Enter Email: ")
            address=input("Enter Address: ")
            account_type=input("Enter Account type(Saving?Current): ")
            admin.create_user_account(name,email,address,account_type)
            
        elif ch==2:
            account_number= int(input("Enter Your Account Number"))
            admin.delete_user_account(account_number)
        
        elif ch==3:
            admin.view_all_accounts()
            
        elif ch ==4:
            admin.view_total_bank_balance()
        
        elif ch==5:
            admin.view_total_loans()
            
        elif ch==6:
            admin.loan_feature()
            
        elif ch==7:
            break
        else:
            print("Invalid Input")
            
    
def User_panel():
    while True:
        print("\nUser Menu")
        print("1. Deposite Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        
        ch = int(input("Enter Choice: "))
        
        if ch==1:
            amount = float(input("Enter amount to deposit"))
            User.depsit(amount,IBBL)
        
        elif ch==2:
            amount = float(input("Enter amount of Withdraw"))
            User.withdraw(amount,IBBL)
        
        elif ch==3:
            User.check_available_balace()
        
        elif ch==4:
            User.check_transaction_history()
            
        elif ch==5:
            amount=float(input("Enter Amount to Loan"))
            User.take_loan_from_bank(amount,IBBL)
            
        elif ch==6:
            amount=float(input("Enter Amount to trnasfer: "))
            other_account=int(input("Enter Recipient Account Number: "))
            User.transfer_balance(amount,other_account,IBBL)
        elif ch==7:
            break
        else:
            print("Invalid Option")
        
    
    
while True:
    print(" Welcome Of Our Banking System")
    print("1.Admin Login")
    print("2.User Login")
    print("3.User Registration")
    print("4.Exit")
    
    ch = int(input("Enter Choice: "))
    if ch==1:
        admin_panel()
        
    elif ch==2:
        account_number= int(input("Enter Your Account Number:"))
        
        if account_number in IBBL.accounts:
            user=IBBL.accounts[account_number]
            User_panel()
            
        else:
            print("Account Number Incorrect")
            
    elif ch==3:
        
        name= input("Enter Name:")
        email=input("Enter Email:")
        address= input("Enter Address: ")
        account_type= input("Enter Account Type (Saving?Current): ")
        account_number=IBBL.create_account(name,email,address,account_type)
        print(f"Your Account Number {account_number}")
    elif ch==4:
        print("Successfuly Logout")
        break
    else:
        print("Invalid Input")
    
     
    
    


