#Importing Python Math Module:
from math import *

#Storing numbers into variables
num = 8
my_num = -8
#Printing out a simple integer, or number:
print(5)
#Printing out a decimal:
print(5.038)
#Printing out a negative number:
print(-1.85)
#Printing with math:
print(8 + 2.4)
print(8 * 2.4)
print(8 - 2.4)
print(8 / 2.4)
#More complex order of operations
print(8 / 2 + 5)
#Or change the order:
print(8 / (2 + 5))
#Using the modulus operator, which will divide the first number by the second number, and say the remainder
print(8 % 5)
#Printing the variable called "num"
print(num)
#Converting a number into a string
print(str(num))
#With becoming a string, it can also be put into ordinary strings! Like this:
print(str(num) + " is my favorite number") #If you want to add it into normal strings, you have to add the str(variable) function.

#Functions
#Abs, or absolute value
print(abs(my_num))
#Take a number to a power, or exponent
print(pow(num, 5))
#Tell which number is greater, or larger
print(max(num, 5))
#Tell which number is least, or smaller
print(min(num, 5))
#Rounding
print(round(8.6))

#Functions imported from the math module
#Rounds down to the nearest integer
print(floor(8.4))
#Rounds up to the nearest integer
print(ceil(8.4))
#Returns the square root, or the opposite of the powers.
print(sqrt(144))
