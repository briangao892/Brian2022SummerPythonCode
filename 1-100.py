number = 0
sum = 0
while number < 100:
    number = number + 1
    if (number % 2) == 0:
        continue
    else:
        sum = sum + number
        print(number)

print("Done with the for loop")

