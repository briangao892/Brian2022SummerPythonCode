str = "ailkjfljaeirufjklakljatydmfiqjk"
def filter(str):
    new_str = ""
    for x in range(len(str)):
        if str[x] in new_str:
            continue
        else:
            new_str = new_str + str[x]
    return new_str
amount = filter(str)
print(amount)
