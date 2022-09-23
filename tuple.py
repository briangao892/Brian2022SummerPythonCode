coordinates = [(3, 4), (3, 5), (3, 6)]
print(coordinates[1])
import copy
import array




names = [1,2,3,4]
tuple(names)
print(tuple(names))
print(type(tuple(names)))
print(list(names))
spam = 42
cheese = spam
print(cheese, spam)
spam = 100
print(cheese, spam)
spam = [0,1,2,3,4,5]
cheese = spam
cheese[1] = 100
D2 = [
    [3, 4, 5],
    [4, 5, 6],
    [7, 8, 9]
]


def eggs(someparameter):
    someparameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)
cheese = spam.copy()
cheese[1] = "hello~"
print(spam)
print(cheese)
stuff = copy.deepcopy(D2)
print(stuff)
stuff1 = D2.copy()
print(stuff1)

spam = ['apples', 'bananas', 'tofu', 'and '+'cats']
print(spam)
check = 0
list = []
nums = []
print("..00.00..")
for i in range(2):
    print(".0000000.")
print("..00000..")
print("...000...")
print("....0....")
n = 10
num = [[0 for _ in range(n)] for _ in range(n)]
'''
num = [
    ["0","0","0"],
    ["0","0","0"],
    [".",".","."]

]
'''
print("my num:", num)

num[0:2] = [".", "0", "0"]

num[3:5] = [".", "0", "0"]

num[6:8] = [".", "0", "0"]
for row in num:
    print(row)

while check == 0:
    answer = input("Enter a random thing: ")
    if answer == "end":
        break
    else:
        list.append(answer)

list.insert(-1, "and")
print(list)
