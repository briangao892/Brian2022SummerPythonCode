list1 = [5, 7, 6, 2, 9, 8, 1, -1]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]
empty = []
emptyc = []
arr = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
def sort(list):
    for i in range(len(list)):
        smallest = list[0]
        for j in range(len(list)):
            if list[j] <= smallest:
                smallest = list[j]
        empty.append(smallest)
        list.remove(smallest)
    return empty

res1 = sort(list1)
print(res1)
empty = []
res2 = sort(list2)
print(res2)
for i in range(len(res2)):
    emptyc.append(res1[i])
for i in range(len(res1)):
    emptyc.append(res2[i])
empty = []
complete = sort(emptyc)
print(complete)
for i in range(len(arr)):
    