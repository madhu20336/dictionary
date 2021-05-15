print("signup or login")
checkAccount=input("Do you have an account (YES OR NO?): ")
if checkAccount=="NO" or checkAccount=="no":
    Name=input("enter your first name: ")
    Sername=input("enter your last name: ")
    f=open("login.txt","r")
    m=f.read()
    if Name not in m or Sername not in m:
        password=input("enter your password: ")
        m=open("login.txt","a")
        m.write("\n")
        m.write(Name)
        m.write(Sername)
        m.write("\n")
        m.write(password)
        m.write("\n")
        m.close()
        print("your acount has been created")
        f.close()
    else:
        print("username already exits")
else:
    new_login=input("enter your name: ")
    file=open('login.txt',"r")
    data=file.read()
    if new_login in data:
        new_pass=input("enter the paasword: ")
        if new_pass in data:
            print("login successfull")
            file.close()
        else:
            print("password incorrect")
    else:
        print("username is wrong")


