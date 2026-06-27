mem_ship = input("Do you have membership ? (yes/no) : ")
purchase = int (input("What is your total purchase ?:"))
method = input("Enter your payment method (cash, visa, ABA) : ")
if mem_ship == "yes":
    if purchase >= 1000:
        dis = ("20%")
        final_pay = purchase*0.8
        amount = purchase*0.2
        print("=====RECEPIT=====")
        print("Memeber ship : Yes")
        print(f"Payment : {method}")
        print(f"Total payment is {purchase}")
        print(f"Discounts : {dis}")
        print(f"Discount amount : {amount}")
        print(f"Final payment : {final_pay}")
        print("==================")
    elif purchase >=500:
        dis2 = ("15%")
        final_pay2 = purchase*0.85
        amount2 = purchase*0.15
        print("=====RECEPIT=====")
        print("Memeber ship : Yes")
        print(f"Payment : {method}")
        print(f"Total payment is {purchase}")
        print(f"Discounts : {dis2}")
        print(f"Discount amount : {amount2}")
        print(f"Final payment : {final_pay2}")
        print("==================")
    else:
        dis3 = ("10%")
        final_pay3 = purchase*0.9
        amount3 = purchase*0.1
        print("=====RECEPIT=====")
        print("Memeber ship : Yes")
        print(f"Payment : {method}")
        print(f"Total payment is {purchase}")
        print(f"Discounts : {dis3}")
        print(f"Discount amount : {amount3}")
        print(f"Final payment : {final_pay3}")
        print("==================")
else:
    if purchase >= 1000:
         dis4 = ("10%")
         final_pay4 = purchase*0.9
         amount4 = purchase*0.1
         print("=====RECEPIT=====")
         print("Memeber ship : No")
         print(f"Payment : {method}")
         print(f"Total payment is {purchase}")
         print(f"Discounts : {dis4}")
         print(f"Discount amount : {amount4}")
         print(f"Final payment : {final_pay4}")
         print("==================")
    else:
        dis5 = ("5%")
        final_pay5 = purchase*0.95
        amount5 = purchase*0.05
        print("=====RECEPIT=====")
        print("Memeber ship : No")
        print("Memeber ship : No")
        print(f"Total payment is {purchase}")
        print(f"Discounts : {dis5}")
        print(f"Discount amount : {amount5}")
        print(f"Final payment : {final_pay5}")
        print("==================")
