arr = [3, 4, 2, 1, 8, 9]
array = [0, 3, 5, 8, 5, 6, 9]
sc_total = 0
total = 0
most = 0
times = 0
info = 0
def find_length(list):
    length = 0
    for k in range(len(list)):
        length = length + 1
    print(length)
    sc_total = length
    return sc_total
def find_mean(array):
    total = 0
    for i in range(len(array)):
        total = total + arr[i]
    sc_total = find_length(arr)
    #print(total/sc_total)
    return total/sc_total
mEAN = find_mean(arr)
print(mEAN)
def find_median(list):
    list.sort()
    print(list)
    index = int(len(list) / 2)
    return list[index]
median = find_median(array)
print(median)