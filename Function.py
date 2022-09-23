def calculate(num1, num2):
    if operator == "+":
        print(float(num1) + float(num2))
    elif operator == "-":
        print(float(num1) - float(num2))
    elif operator == "*":
        print(float(num1) * float(num2))
    elif operator == "/":
        try:
            print(float(num1) / float(num2))
        except ZeroDivisionError:
            if num1 >= num2:
                print("Error")
            else:
                print(0)
    elif operator == "%":
        try:
            print(float(num1) % float(num2))
        except ZeroDivisionError:
            print("No remainder")

    else:
        print("Invalid Operator")

number = 0
while number == 0:
    num = input("Enter a number: ")
    operator = input("Enter your operator: ")
    dum = input("Enter another number: ")
    calculate(num, dum)


