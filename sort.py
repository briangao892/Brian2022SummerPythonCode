list = [1, 3, 4, 5, 6, 7, 9 ,8 , -0.5, -1,2, 1, 4, 5, 6]
empty = []
ans = "anagram"
ans2 = "zana"
relate = ""
for i in range(len(list)):
    smallest = list[0]
    for j in range(len(list)):
        if list[j] <= smallest:
            smallest = list[j]
    empty.append(smallest)
    list.remove(smallest)
print(empty)
print(list)
for i in range(len(ans2)):
    try:
        if ans2[i] == ans[i]:
            relate = relate + ans2[i]
        else:
            continue
    except IndexError:
        print("The string is too long! Find with an equal amount or greater amount of length. SUCKER!")
        exit()
print(relate)
