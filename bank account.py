account={}

def check_account():
    
    while True:
        try:
            return int(input("Enter account no : "))
        except ValueError:
            print("Numbers only.\n")

def create():
    acc_no=check_account()
    if acc_no in account:
        print("Account already exists.")
        return
    name=input("Enter account holder name : ")
    amount=input("Enter initial deposit : ")
    if not amount.isdigit():
        print("Invalid amount.\n")
        return
    amount=float(amount)
    account[acc_no]={"name":name, "balance":amount}
    print("\nAccount created successfully.\n")

def deposit():
    acc_no=check_account()
    if acc_no not in account:
        print("\nAccount not found!\n")
        return
    amount=input("Enter deposit amount : ")
    if not amount.isdigit():
        print("Invalid amount.\n")
        return
    amount=float(amount)
    account[acc_no]["balance"]+=amount
    print("\nDeposit successful!\n")

def withdraw():
    acc_no=check_account()
    if acc_no not in account:
        print("\nAccount not found!\n")
        return
    amount=input("Enter withdrawal amount : ")
    if not amount.isdigit():
        print("Invalid amount\n.")
        return
    amount=float(amount)
    if amount<=account[acc_no]["balance"]:
        account[acc_no]["balance"]-=amount
        print("\nWithdrawal successful!\n")
    else:
        print("\nInsufficiant balance!\n")  

def check_balance():
    acc_no=check_account()
    if acc_no not in account:
        print("\nAccount not found!\n")
        return
    print(f"Account holder : {account[acc_no]['name']}")
    print(f"Balance : {account[acc_no]['balance']}\n")

def action():
    print("""------ Banking System ------
1. Crete account
2. Deposite 
3. Withdraw 
4. Check balance 
5. Exit
""")


def main():
    
    call={
        "1":create,
        "2":deposit,
        "3":withdraw,
        "4":check_balance
    }
    while True:
        action()
        choice=input("Enter choice : ")
        if choice=="5":
            print("Thanks for being with us.")
            break

        if choice in call:
            call[choice]()
        else:
            print("\nInvalid choice.\n")

main()
        



    
    