stu_name = input("Enter your name  : ")
age = int(input("\nWhat is your age : "))
gender = input("\nEnter your gender : ")
level =int(input("\nWhat is your year level : "))
math = int(input("\nEnter your math score : "))
eng = int(input("\nEnter your English score : "))
khm = int(input("\nEnter your Khmer score : "))
chi = int(input("\n Enter your Chiense score : "))

avg = (math+eng+khm+chi)/4

print(f"Your avg score is {avg}")
if avg >= 90:
    print("You got A for your grade!")
elif avg >= 80:
    print("You got B for your grade !")
elif avg >= 70:
    print("You got C for your grade !")
elif avg >=60:
    print("You got D for your grade")
else:
    print("You only got F for your grade")