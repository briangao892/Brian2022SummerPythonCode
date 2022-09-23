words = ["hi", 'ty', 'ruck', 'abc']
bad = "abc"

new_list = []
new_str = ""
str = ""
for i in range(len(words)):
    new_str = ""
    for x in range(len(str)):
        str = words[i]
        if str[x] in new_str:
            continue
        else:
            new_str = new_str + str[x]
            new_list.append(new_str)
        str = ""
for i in range(len(new_list)):
    if new_list[i] == bad:
        new_list.remove(new_list[i])
print(new_list)
words2 = ["why", "duck", "stupidd", "abbc"]
bad_word = 'abc'
new = ""
#for i in range(len(words2)):
    #new = ""
    #for x in range(len(words2[i])):
        #if not words2[i] in new:
            #new = new + words2[x]
            #print(words2[x])
        #if new == bad_word:
            #words2.remove(words2[i])
            #print("yo")'''
print(words2)
#def filter(str):
    #new_str = ""
    #for x in range(len(str)):
        #if str[x] in new_str:
            #continue
        #else:
            #new_str = new_str + str[x]
    #return new_str

for i in range(len(words2)):
    res = words2[i]
    if bad_word in res:
        words2[i] = "NO"
print(words2)

list = [
    [1,2,3,4],
    [5,6,7,8],
    [9,0,1,2],
    [3,4,5,6]
]
diag = 0
#for i in list:
    #for j in list:
news = [list[i][i] for i in range(len(list))]
all = 0
for i in range(len(list)):
    for j in range(len(list[0])):
        if i == j:
            all = all + list[i][j]
print(all)
all = 0
for u in range(len(list)):
    for i in range(len(list[0])):
        if u + i == len(list[0])- 1:
            all = all + list[u][i]
print(all)
text = 0
all = 0
for _ in range(2):
    text = 0
    for a in range(len(list)):
        text = 0
        for b in range(len(list[0])):
            if a + b == text:
                all = all + list[a][b]
                text = text + 1
                print(list[a][b])
print(all)
all = 0
for i in range(len(list)):
    for j in range(len(list[0])):
        if i == 0:
            all = all + list[i][j]
            print(all)
        elif j == 0:
            all = all + list[i][j]
            print(all)
for i in range(len(list)):
    for j in range(len(list[0])):
        if i == 3:
            all = all + list[i][j]
            print(all)
        elif j == 3:
            all = all + list[i][j]
            print(all)
print(all)