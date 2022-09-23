string = "codeleet"
indices = []
new_ind = []
new_string = ""
indices2 = [4, 5, 6, 7, 0, 1, 2, 3]
print(new_string)
#What is wrong with this code?:
'''for i in range(len(string)):
    indices.append(i)
for i in range(len(indices) // 2, len(indices)):
    new_ind.append(indices[i])
for i in range(len(string) // 2):
    new_ind.append(indices[i])
'''
#?????
for i in range(len(string)):
    new_string = new_string + string[indices2[i]]

print(new_ind)
print(new_string)
"Hello"
_myvar = ""
