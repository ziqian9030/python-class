email =input("Enter your email : ")
if email == "ziqian@gmail.com":
    username = input("Enter your username : ")
    if username == "ziqian":
        passw = input("Enter your password : ")
        if passw == "jason is dumb":
            print(" Login success !")
        else:
            print("Wrong password")
    else:
        print("Wrong username.")        
else:
    print("Wrong email. ")