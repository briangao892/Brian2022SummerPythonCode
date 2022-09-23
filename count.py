list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(len(list))

for i in range(len(list)):
    print()
    for j in range(len(list[0])):
        ans[j] = list[len(list[j]) - j - 1]
print(ans)
print(list)
for i in range(len(list[0])):
    for b in range(len(list)):
        ans[i][b] = list[i][b]
ans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(list[0])):
    for k in range(len(list)):
        list[k] = list[len(list[k]) - k - 1]
    print(list)
print(ans)
single = [[0, 0, 1]]
#for i in range(len(single)):
    #for k in range(len(single[0])):
        #single[i] = single[len(single[i]) - i - 1]
print(single)
simple = [
    [0, 1, 3, 5, 9],
    #[0, 2, 3, 6, 9]
    ]

print(all)
