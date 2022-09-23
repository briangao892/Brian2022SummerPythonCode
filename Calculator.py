do = input("What would you like to do? Input History, or Calculate: ")
do = do.lower()
history = []
if do == "calculate":
    num1 = float(input("Enter first number: "))
    op = (input("Enter operator: "))
    num2 = float(input("Enter second number: "))
elif do == "history":
    print(history)
if do == "calculate":
    if op == "+":
        print(num1 + num2)
        history.append(str(num1)+ "+" +str(num2))
    elif op == "-":
        print(num1 - num2)
        history.append(str(num1) + "-" + str(num2))
    elif op == "*":
        print(num1 * num2)
        history.append(str(num1) + "*" + str(num2))
    elif op == "/":
        print(num1 / num2)
        history.append(str(num1) + "/" + str(num2))
    else:
        print("Invalid Operation")
print(history)