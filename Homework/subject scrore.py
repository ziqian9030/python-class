name = input("Enter your name : ")
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))
grade = int(input("What is your grade : "))
math = int(input("What is your math grade? : "))
eng = int(input("What is your English grade? : "))
khmer = int(input("What is your Khmer grade? : "))
chinese = int(input("Waht is your Chinese grade? : "))
physics = int(input("What is your physics grade? : "))
total = math + eng + khmer + chinese + physics
avg = total/5

print("-----Result-----")
print(f"Name : {name}")
print(f"Gender : {gender}")
print(f"Grade : {grade}")
print(f"Total score is : {total}")
print(f"Your average score is : {avg}")