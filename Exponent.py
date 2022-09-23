print(2**8)
def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result
num1 = input("Enter a number: ")
num2 = input("Enter a power: ")
print(raise_to_power(int(num1), int(num2)))