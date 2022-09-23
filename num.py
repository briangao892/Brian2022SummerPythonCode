dict = {

}
a2 = ""
a = [9, 5, 2, 3, 9, 1, 8, 2, 7, 6, 2, 1, 8]
target = 8
for i in range(len(a)):
    dict.update({i : a[i]})
'''def sum(list, target):
    times=0
    z = 0
    for i in range(len(list)):
        for j in range(len(list)):
            Tw = target - list[i]
            if list[j] * z == Tw:
                z = Tw - a[j]
                if list[i] in list:
                    print("WHY DOES GOOGLE ALWAYS FRAME ME?????????????")
                    times += 1
    return times
res = sum(dict, target)
print(res)'''
def summ(list, target):
    times = 0
    z = 0
    for i in range(len(list)):
        for j in range(len(list)):
            Tw = target / list[i]
            print(list[i], list[j])


            print(list[z])
            if type(list[z]) == float:
                continue
            print(z)
            if list[j] * z == Tw:
                z = Tw / a[j]
                if list[i] in list:
                    times += 1
    return times
result = summ(dict, target)
print(result)