import math
list = [0, 1, 9, 0, 6, 5, 2, 2, 9,9,9,9,9,9,3, 2, 4, 3, 5,0,0,0,0, 6, 7, 8, 9, 10]
arr = [0, 5, 8, 7, 3, 6, 2, 7, 1]
def count(goal, list):
    count = 0
    for i in range(len(list)):
        if list[i] == goal:
            count = count + 1
    return count
def mode(List):
    max = [0, 0]
    for i in List:
        occ = count(i, List)
        if occ > max[0]:
            max = [occ, i]
    return max[1]
'''def hitman(list, target):
    for i in list:
        targ = i
        for j in list:
            for k in list:
                if i + j + k == target:
                    print(k + j + i)

                    break
    return ""
'''
res = mode(list)
print(res)
#result = hitman(arr, 8)
#print(result)

