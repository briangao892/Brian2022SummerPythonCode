import pdb
D2 = [
    [5, 9, 5],
    [7, 8, 9],
    [3, 4, 10]
]
D2_Tumbled = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
row = len(D2)
col = len(D2[0])
all = 0
D1 = [0, 3, 5, 7, 0, 9]
D1_Tumbled = [0, 0, 0, 0, 0, 0]


def Tumble(array, Tumbler):
    length = len(array)
    for k in range(3):
        print("")
        for j in range(3):
            Tumbler = array[j][k]
            Tumbler[j] =
    return Tumbler
def TUMBLE(Tumbler):
    n = len(Tumbler)
    res = [ 0 ] * n
    print(n)
    for i in range(n):
        cur = Tumbler[n-i-1] # try to understand this
        #res.append(cur)
        res[i] = cur
    return res
#pdb.set_trace()
Tumble = Tumble(D2, D2_Tumbled)
print(Tumble)
answer = TUMBLE(D1)
print(answer)




