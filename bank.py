bank = [
    [0, 1, 2, 3, 5],
    [7, 9, 2, 1, 10],
    [10, 2, 3, 10, 3]
]
print(len(bank[0]))
total = 0
greatest = 0
for i in range(len(bank)):
    total = 0
    for j in range(len(bank[0])):
        total = total + bank[i][j]
    if total > greatest:
        greatest = total
print(greatest)
greatest = 0
for i in range(len(bank[0])):
    total = 0
    for j in range(len(bank)):
        total = total + bank[j][i]
    if total > greatest:
        greatest = total
print(greatest)