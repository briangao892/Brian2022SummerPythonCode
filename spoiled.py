last_index = 0
a = [
    [1,2],
    [3,4]
]
index = 0
lost = []
b = [1,2]
index = 0
numbers = []
all = 0
last_a = ""
arr = [5, 3, 2, 7, 8, -200,0,  1, -300, -100]
#[-100, -300, 1, 0, -200, 8, 7, 2, 3, 5]

least_index = 0
new_arr = arr.copy()
def swap(a, b):
    temp = a
    a = b
    b = temp
    print(a, b)
def swap_list(list):
    list = 0
    a = b
    b = last_a
    print(a, b)
def find_greatest(list):
    greatest = 0
    greatest = arr[0]
    last_value = 0
    for j in range(len(list)-1):
        if list[j] > greatest:
            last_value = greatest
            greatest = list[j]
            big_index = greatest
    print(last_value)
def find_length(list):
    length = 0
    for k in range(len(list)):
        length = length + 1
    print(length)
def reverse(list):
    b = 0
    #for b in range(len(list)):
        #swap_num(list[b], list[len(list) - 1 - i])
    print(arr)
for k in range(2):
    print("")
    for i in range(2):
        print(b[i], end=" ")
def swap_num(num1, num2):
    temporary = num1
    num1 = num2
    num2 = temporary
    #print(num1, num2)
def swap_num2(i,j):
    tempor = arr[i]
    arr[i] = arr[j]
    arr[j] = tempor
    print(arr[i], arr[j])
var = len(arr) / 2
for f in range(int(var)):
    swap_num2(f, len(arr) - 1 - f)
    #print(f, len(arr) - 1 - f)
    print(arr)
print('---',arr)
swap_num(5, 8)
find_greatest(arr)
find_length(arr)
reverse(arr)
swap_num(arr[0], arr[-1])
print(arr)
reverse(arr)
swap(input("Enter number: "), input("Enter another number: "))

