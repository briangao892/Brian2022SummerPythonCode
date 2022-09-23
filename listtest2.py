a = [[[1,2,3],
      [4,5,6]],
    [[7,8,9],
     [10,11,12]],
    [[13,14,15],
     [16,17,18]]]
simple_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
medium_list = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
keep_names = []
Parents = []
keep_names.clear()
Kids = []
Yuan = ""
Le = ""
Brian = ""
Chloe = ""
Feona = ""

row = len(a)
col = len(a[0])
all = 0
all2 = len(a[0-2])
print(row)
print(col)
for i in range(3):
    for j in range(2):
        for k in range(3):
            all = all + a[i][j][k]
print(all)
print(simple_list[:8])
simple_list.append(13)
print(simple_list)
print(simple_list + medium_list)
del simple_list[2]
print(simple_list)
names = ["Chloe", "Brian", "Feona", "Yuan", "Le"]
names1, names2, names3, names4, names5 = names
print(names.index("Brian"))
names.sort().reverse()

print(names)
print(names1)
print(names2)
print(names3)
print(names4)
print(names5)
print(Kids)
print(keep_names)
if "Ye" in keep_names:
    print("Ye is in there")
else:
    if ValueError:
        print("ValueError: 'Ye' is not in list")

