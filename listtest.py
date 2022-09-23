

all = 0
points = 0
numbers = [0, 1, 3, 8, 15, 7, 3, 5, 6, 9]
array = [
    [2, 3, 5],
    [8, 9, 10]
]
def sumofarray(array):
    subtotal = 0
    for element in array:
        if type(element) is list:
            subtotal += sumofarray(list)
        else:
            subtotal += element
    return subtotal

for i in range(len(numbers)):
    all = all + numbers[i]
print(all)
print(numbers[2])
print(numbers[-2])
print(numbers[2:-2])
print(numbers[0])
print(numbers[-1])
print(numbers[9])
print(array[0][1])
print(array[1][2])
all = 0

row = len(array)
col = len(array[0])

for i in range(row):
    for j in range(col):
        for k in range()
        all = all + array[i][j]
print(array)
print(points)
print(all)
print(all)

