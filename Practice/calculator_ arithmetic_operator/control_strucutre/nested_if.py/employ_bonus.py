name = input("What is your name : ")
position = input("Enter your position (manager/stuff) : ")
exp = int(input("Enter your year experience : "))
sal =float(input("Enter your salary : "))
if position == "manager":
    if exp >= 10:
        final_sal = sal*1.3
        bonus = sal*0.3
        print("==========Employee bonus report==========")
        print(f"Employee name : {name}")
        print(f"Employee's position : {position}")
        print(f"Employee's year experience : {exp}")
        print(f"Salary : {sal}")
        print(f"Bonus : {bonus} dollars")
        print(f"Total salary is : {final_sal} dollars")
    else:
        final_sal2 = sal*1.2
        bonus2 = sal*0.2
        print("==========Employee bonus report==========")
        print(f"Employee name : {name}")
        print(f"Employee's position : {position}")
        print(f"Employee's year experience : {exp}")
        print(f"Salary : {sal}")
        print(f"Bonus : {bonus2} dollars")
        print(f"Total salary is : {final_sal2} dollars")
else:
    if exp >= 5:
        final_sal3 = sal*1.15
        bonus3 = sal*0.15
        print("==========Employee bonus report==========")
        print(f"Employee name : {name}")
        print(f"Employee's position : {position}")
        print(f"Employee's year experience : {exp}")
        print(f"Salary : {sal}")
        print(f"Bonus : {bonus3} dollars")
        print(f"Total salary is : {final_sal3} dollars")
    else:
        final_sal4 = sal*1.05
        bonus4 = sal*0.05
        print("==========Employee bonus report==========")
        print(f"Employee name : {name}")
        print(f"Employee's position : {position}")
        print(f"Employee's year experience : {exp}")
        print(f"Salary : {sal}")
        print(f"Bonus : {bonus4} dollars")
        print(f"Total salary is : {final_sal4} dollars")