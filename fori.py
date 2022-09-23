array = [0, 1, 3, 3,3, 5, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
no = []
def count(list, target):
    times = 0
    for i in range(len(list)):
        if list[i] == target:
            times += 1
    return times
index = 0
element = 0
for element in array:
    amount = count(array, element)
    if element not in no:
        no.append(element)
    elif element in no:
        array.remove(element)
    if amount >= 2:
        array.remove(element)
    else:
        continue
print(array)
array = [0, 1, 3, 3,3, 5, 6, 6]
temp = 0
for element in array:
    amount = count(array, element)
    if amount > 1:
        temp = element
        index = array.index(temp)
        for el in range(amount):
            array.remove(element)
        array.insert(index, temp)
print(array)
array = [0, 1, 3, 3,3, 5, 6, 6,6, 7, 7, 7, 7, 7, 7]
for element in array:
    if array[array.index(element) + 1] == element:
        tempo = element
        index = array.index(element)
        for el in range(len(array)):
            if element in array:
                array.remove(element)
            else:
                break
        array.insert(index, tempo)
print(array)
