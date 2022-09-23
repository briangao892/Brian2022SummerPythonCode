listt = [0, 1, 2, 3, 4, 6]
list = [0, 2, 5, 4, 1, 0]
def find_intersection(list, list2):
    already = []
    for i in range(len(list)):
        amount = list2.count(list[i])
        if list[i] not in already:
            already.append(list[i])
            if amount > 0:
                print(list[i])
find_intersection(list, listt)