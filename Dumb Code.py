pylist = [100, 3, 6, 9, 3, 5, -6]
name = "Yvel"
string = "ababcddegabcdeg"
def odd_even(nums):
    odd = 0
    even = 0
    for i in range(len(nums)):
        if i % 2 == 1:
            odd = odd + nums[i]
        else:
            even = even + nums[i]
    print(odd, even)
    return odd - even
difference = odd_even(pylist)
print(difference)


def anagram(string):
    Two = 2
    p1 = ''
    p2 = ''
    p1 = name[:len(name) // 2]
    p2 = name[len(name) // 2:]
    if p1 == p2:
        return p1, p2
    else:
        return "not anagram"
def new_anagram(str):
    new_str = ''
    if str == "":
        return "You didn't even write anything!"
    for j in str:
        new_str = j + new_str

    if new_str == str:
        return str+" is an anagram"
    else:
        return str+" is not an anagram"

sym = anagram(name)
sym2 = new_anagram(name)
print(sym2)
def find_amount(str):
    new_str = ""
    for x in range(len(str)):
        if str[x] in new_str:
            continue
        else:
            new_str = new_str + str[x]
    return new_str
amount = find_amount(string)
print(amount)
