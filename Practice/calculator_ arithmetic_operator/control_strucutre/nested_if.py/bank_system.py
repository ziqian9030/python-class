u_m = input("\nPlease enter your username : ")
passw = input("\nPlease enter your password : ")
if u_m == "ziqian" and passw == "123456":
    print("\nLogin successful! Welcome to python bank!")
    intial_balance = float(input("\nPlease enter your initial account balance : "))
    print("\n======Banking menu====== :")
    print(" 1. Check balance")
    print(" 2. Deposite money")
    print(" 3. Withdraw money")
    option = int(input("Please enter your option (1,2 or 3) : "))
    if option == 1:
        print(f"Your current balance is {intial_balance} dollars")
    elif option == 2:
        depo =float(input("Please enter how much money you want to put in : ")) 
        if depo == 0:
            print("Error: Invalid deposit amount")
        else:
            current_ba = intial_balance + depo
            print(f"Now, you have {current_ba} dollars in your account!")
    elif option == 3:
        with_draw = float(input("Please enter how much you want to withdraw : "))
        if with_draw > intial_balance:
            print("Error: Insufficent funds")
        else:
            current_ba2 = intial_balance - with_draw
            print(f"Your account has {current_ba2}dollars left")
    else:
        print("Invalid transaction option")
else:
    print("Wrong user information")
