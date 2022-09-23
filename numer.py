diction = {}
list = [5, 2,3,4,7, 8, 1, 9, 6]
target = 8
for i in range(len(list)):
    diction.update({i : list[i]})
def sum(list, target):
    z = 0
    time=0
    for i in range(len(list)):
        for j in range(len(list)):
            Tw = target - list[i]
            if list[j] + z == Tw:
                z = Tw - list[j]
                print(list[i], end=" ")
                print(list[j], end=" ")
                print(list[z])
                if list[i] in list.values():
                    time += 1
                    print(list[i], end=" ")
                    print(list[j], end=" ")
                    print(list[z])
    return time
def sum2(list, target):
    time = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if target - list[j] == list[i]:
                print(list[i], list[j])
                #print(list[j])
                time += 1
    return time
def multi(list, target):
    time = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if target / list[j] == list[i]:
                print(list[i], list[j])
                time += 1
    return time
PLEASE = sum(diction, target)
print(PLEASE)
print(diction)
Please = sum2(diction, target)
print(Please)
print("MULTIPLICATION HERE:")
please = multi(diction, target)
print(please)
'''
import turtle
turtle.shape("turtle")
turtle.pensize(100)
while 10>3:
    for i in range(10):
        turtle.forward(10)
    turtle.left(90)
'''
def sumer(list, target):
    time = 0
    for i in range(len(list)):
        for j in range(len(list)):
            Tw = target - list[i]
            z = Tw - list[j]
            if list[j] + z == Tw:
                if list[i] and z in list.values():
                    print(list[i], list[j], z)
                    time = time + 1
    return time
res = sumer(diction, target)
print(res)
print("            s")
def numer(list, target):
    time = 0
    stall = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if not target / list[i] == float:
              Tw = target / list[i]
            elif target / list[i] == float:
                continue
            stall = 1
            z = Tw /  list[j]
            #print(list[i], list[j], int(z))
            if list[j] * z == Tw:
                #print(list[i] * z)
                if list[j] and z in list.values():
                    #print("HEWEŁO")
                    print(list[i], list[j], int(z))
                    time = time + 1
    return time
result = numer(diction, target)
print(result)
print(8/3)