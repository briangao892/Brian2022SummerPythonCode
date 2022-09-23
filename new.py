import random
import sys
for i in range(0, 10):
    number = random.randint(0, 10)
    if number % 2 == 1:
        number = number + 1

    if number % 10 == 0:
        sys.exit()
        print(number)
    else:
        if number % 10 == 0:
            sys.exit()
        print(number)

