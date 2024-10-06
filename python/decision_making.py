email = input("Enter your email :")
password = input("Enter your password :")

if email =="" or password == "":
    if email == "" and password !="":
        print("Email can't be blank") 
    elif email != "" and password == "":
        print("Password can't be blank") 
    else:
        print("Both can't be blank")
else:
    if email == "abc@gmail.com" and password == "12345":
        print("Login Succesfully")
    else:
        print("Invalid username or password")