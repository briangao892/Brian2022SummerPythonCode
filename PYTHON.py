elements = [0,0,0,0,0,0,0,0,0,0]
num = 0
ori_2d = [
    [5, 8, 0],
    [7, 9, 7],
    [8, 9, 10]
]
for i in range(len(elements)):
    elements[i] = i
print(elements)
def reverse(elements):
    two = 2
    result = [0,0,0,0,0,0,0,0,0,0]
    for j in range(int(len(elements))-1):
        result[j] = elements[len(elements) - j - 1]
    return result
ans = reverse(elements)
print(ans)
def reverse_2D(my_ori_2d):
    print("reverse_2d")
    print(len(my_ori_2d))
    n = len(my_ori_2d)
    res = [[0]*n]*n
    print("initialize res 2 d list :", res)
    i = j = 0
    while i < n:
        while j < n:
            num = my_ori_2d[j][i]
            print(num)
            res[i][j] = num
            print("in while ", i, j, res[i][j])
            j = j + 1
            print(res)
        i = i + 1
        j = 0
    print("res is ", res)
    return res
    #for l in range(3):
    #    for k in range(3):
    #        result = home[l][k]
    #        print(result[l][k])
    #return result
if __name__ == "__main__":
    #print(reverse_2D(ori_2d))
    ans2 = reverse_2D(ori_2d)
    print(ans2)
def reverse_2D(list):
    buffer = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    for i in range(3):
        for j in range(3):
            buffer[i][j] = list[j][i]
    return buffer
ans3 = reverse_2D(ori_2d)
print(ans3)