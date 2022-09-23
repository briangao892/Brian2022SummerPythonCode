password1 = 123
password2 = 456
pass2 = False
passcode = 0
passcode2 = 0
type = ""
available_names = ["brian", "chloe"]
while pass2 == False:
    type = input("Input Username:")
    type = type.lower()
    if type in available_names:
        if type == "chloe":
            passcode2 = input("Enter Passcode")
            if int(passcode2) == password2:
                print("Hello, Chloe Gao")
                continue
            else:
                print("Invalid Password")
                continue
        if type == "brian":
            passcode = input("Enter Passcode")
            if int(passcode) == password1:
                print("Hello, Brian Gao")
                continue
            else:
                print("Invalid Passcode")
                continue

    else:
        print("Invalid Username")




