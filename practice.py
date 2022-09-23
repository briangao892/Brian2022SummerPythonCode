For = [
    [5, 6],
    [7, 8],
    [9, 10],
    [11,12],
    [13,14]
    ]
Fora = [
    [0, 0],
    [0, 0],
    [0, 0]
    ]
For2 = [
    [0,5],
    [6,9],
    [7,4]
]

for i in range(len(For)):
    for j in range(len(For[0])):
        Fora[i][j] = For[len(For) - i - 1][len(For[i]) - j - 1]
total = 0
print(Fora)
for i in range(len(For)):
    for j in range(len(For[0])):
        Fora[i][j] = Fora[i][j] + For2[i][j]
print(Fora)
print(len(For))

Fora = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0,0],
    [0,0]
    ]

for i in range(len(For)):
    for j in range(len(For[0])):
        if i % 2 == 0:
            Fora[i][j] = For[i][len(For[i]) - j - 1]
        else:
            Fora[i][j] = For[i][j]
print(Fora)