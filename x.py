z = [
    [90,6, 3],
    [5, 8, 2],
    [100, 1000, 10000]
]
print(z)
answer = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(z)):
    for j in range(len(z[0])):
        answer[i][j] = z[i][len(z[i]) - j - 1]

print(answer)