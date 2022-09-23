list = [
    [0, 1, 2, 10],
    [3, 4, 5, 9],
    [6, 7, 8, 12]
]
list2 = [
    [0, 1, 2, 10],
    [3, 4, 5, 9],
    [6, 7, 8, 12]
]
var = ""
sliceing = [
    [0, 1, 2, 8, 14],
    [3, 4, 6,11, 15],
    [5, 7, 10,12, 11],
    [13,14,15,16, 9],
    [0, 1, 2, 3, 4, 5]
]
sli = [
    [0, 1],
    [2,3]
]
slice = [
    [0, 2, 4],
    [7, 2, 3],
    [1, 3, 8]
]
no = []


lasti = 0
novar = str(len(list[0]))
for i in range(len(list)):
    print()
    for j in range(len(list[0])):
        if i % 2 == 0:
            print(list[i][len(list[i]) - j - 1], end=" ")
        else:
            print(list[i][j], end=" ")
print(list2)
for i in range(len(sliceing)):
    print()
    for j in range(len(sliceing[0])):
        if not j in no:
            print(sliceing[i][j], end=' ')
        else:
            continue
    no.append(lasti)
    lasti = lasti + 1

lasti = len(sliceing[0]) - 1
no = []
for i in range(len(sliceing)):
    print()
    for j in range(len(sliceing[0])):
        if not j in no:
            print(sliceing[i][j], end=' ')
        else:
            continue
    no.append(lasti)
    lasti = lasti - 1
no = []
lasti = 0
lastj = len(sli[0]) - 1
for i in range(len(sli)):
    print()
    for j in range(len(sli[0])):
        if not j in no:
            print(sli[i][j], end=' ')
        else:
            continue
    no.append(lasti)
    no.append(lastj)
    lasti = lasti + 1
    lastj = lastj - 1
print(no)