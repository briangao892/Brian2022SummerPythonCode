numb = [-1, 3, 6, -5, 7, -6, -2, 1]
numb2 = []
for i in numb:
    if i < 0:
        numb2.append(i)
for i in numb:
    if i > 0:
        numb2.append(i)
print(numb2)
numb = [-1, 3, 6, -5, 7, -6, -2, 1]
print(numb, "3")
index = 0
string = ""
for i in range(len(numb)):
    index = i
    if numb[i] > 0:
        numb.append(numb[i])
        numb.remove(numb[index])
        print('----', i, numb)
    else:
        continue

print()
print(numb)
