import random
number = ""
stuff = 0
stuff2 = 0
stuff3 = ""
answer =""

def pick_Random(num):
    while num != number:
        print(num)
        if num > number:
            num = num - 1
        if num < number:
            num = num + 1
        if num == number:
            print("The COMPUTER IS CORRECT. IT SOLVED THE PUZZLE FOR YOU. THE ANSWER IS: ")
    return num





tries = 0
while stuff == 0:
    stuff2 = 0
    number = random.randint(1, 20)
    print(number)

    print(pick_Random(int(input("Enter a number: "))))

