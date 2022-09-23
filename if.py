#Boolean Variable:
is_male = False
is_tall = False
#Asking the the variable called"is_male" is true:
if is_male or is_tall:
    print("You are cool")
elif is_male and not(is_tall):
    print("You are good")
elif not(is_male) and is_tall:
    print("You are drool")
else:
    print("You are coo")
