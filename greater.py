default = 10
elements = [15, 10, 9, 6, 19, 18, 17, 5, 8]
for i in range(len(elements)):
    if elements[i] > default:
        elements[i] = 0
words = ["Hello", "Bye", "abccc", "hi", "stupid"]
bad = ["abc", "stupid"]
def filter(str):
    new_str = ""
    for x in range(len(str)):
        if str[x] in new_str:
            continue
        else:
            new_str = new_str + str[x]
    return new_str
new_list = []
for x in range(len(words)):
    if words[x] in new_list:
        continue
    else:
        res = filter(words[x])
        new_list.append(res)
for i in range(len(new_list)-1):
    print(len(new_list))
    res = filter(words[i])
    print(res)
    if new_list[i] in bad:
        new_list.remove(new_list[i])
print(words)