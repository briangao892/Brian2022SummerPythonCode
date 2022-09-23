D2 = [
    [0, 1, 2, 10, 90],
    [2, 3, 6, 10, 12],
    [0, 3, 1, 6, 12]
]
def count(list, target):
    times = 0
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j] == target:
                times += 1
    return times
def find_duplicate(list):
    times = 0
    ij = []
    for i in range(len(list)):
        for j in range(len(list[0])):
            times = count(list, list[i][j])
            if list[i][j] not in ij:
                ij.append(list[i][j])
                if times > 1:
                    print(list[i][j], end=" ")

find_duplicate(D2)