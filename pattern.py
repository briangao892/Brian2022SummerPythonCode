Array = [
    [1, 2, 3, 0, 20, 41],
    [4, 5, 6, 10, 19, 22],
    [7, 8, 9, 12, 18, 23],
    [11, 13, 15, 14, 17, -5],
    [21, 25, -1, -2, 29, 30],
    [-6, -7, -8, -9, -10, -11]
]
Array2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
no_index = []
vorh = 0
'''
for i in range(len(Array)):
    print()
    for j in range(len(Array[0])):
        if vorh % 2 == 0:
            print(Array[i][j], end=" ")
            no_index.append(Array[i][j])
        elif vorh % 2 == 1:
            if Array[i][j] == Array[i][-1]:
                print(Array[i][j], end=" ")
                no_index.append(Array[i][j])
for i in range(len(Array)):
    for j in range(len(Array[0])):
        print(Array[i][j])
    vorh += 1
print()
for i in range(len(Array)):
    for j in range(len(Array[0])):
        if Array[i][j] not in no_index:
            print(Array[i][j], end=" ")
print()
print(no_index)
'''
no_index = []
def spiral():
    for i in range(len(Array)):
        for j in range(len(Array[0])):
            if i == 0:
                print(Array[i][j], end=" ")
                no_index.append(Array[i][j])
                continue
            if i == len(Array) - 1:
                continue
            if j == len(Array[0]) - 1:
                no_index.append(Array[i][j])
                print("   ",str(Array[i][j]), end=" ")
        print()
    for i in range(len(Array)):
        for j in range(len(Array[0])):
            if i == len(Array) - 1:
                print(Array[i][len(Array[i]) - j - 1], end=" ")
                no_index.append(Array[i][j])
    for i in range(len(Array)):
        for j in range(len(Array[0])):
            if j == 0 and Array[i][j] not in no_index:
                print(str(Array[i][j]), end=" ")
        print()
spiral()
def spiral_as_many_as_you_want(list):
    no_index = []
    for i in range(int(len(list) + 1 / 2)):
        for t in range(len(list[0]) // 2):
            for k in range(len(list)):
                for j in range(len(list[0])):
                    if k == list[i]:
                        print(list[k][j])
                        no_index.append(list[k][j])
                        continue
                    if k == len(list) - 1:
                        continue
                    if j == t - 1:
                        no_index.append(list[k][j])
                        print(Array[k][j], end=" ")
            print()

def spiral2(arr):
    novar = []
    length = len(arr[0]) - 1
    width = 0
    height = len(arr) - 1
    extra = 0
    no = ""
    for i in range(len(arr) + 1 // 2):
        #Top
        for k in range(len(arr)):
            for j in range(len(arr[0])):
                if k == width:
                    if j == len(arr[0]) - 1:
                        break
                    novar.append(arr[k][j])
                    print(arr[k][j], end=" ")
        print()
        #Right
        for k in range(len(arr)):
            for j in range(len(arr[0])):
                if k == len(arr) - 1:
                    break
                if j == length:
                    print(arr[k][j], end=" ")
                    novar.append(arr[k][j])

        print()
        #Bottom
        for k in range(len(arr)):
            for j in range(len(arr[0])):
                if j == len(arr[0]) - 1:
                    break
                args = arr[k][len(arr[k]) - j - 1]
                if k == height:
                    print(args, end=" ")
                    novar.append(args)
        print()
        #Left
        for k in range(len(arr)):
            for j in range(len(arr[0])):
                if k == len(arr) - 1:
                    break
                kws = arr[len(arr) - k - 1][j]
                if j == extra:
                    novar.append(kws)
                    print(kws, end=" ")
        width = width + 1
        length -= 1
        height = height - 1
        extra += 1

import t
spiral2(Array)
spiral_as_many_as_you_want(Array)
