import sys
a = 'brian'
b = 'gao'
vars2 = ""
taker = ""
def connect(str1, str2):
    for i in range(len(str2)):
        str1 = str1 + str2[i]
    return(str1)
def multiply(str, int):
    vars = ""
    for v in range(int):
        vars = vars + str
    print(vars)
connect(a, b)
multiply("Brian", 3)
vars = ""
for v in range(3):
    vars = vars + "hi"#str
print(vars)
def multiply2(str2, int2):
    vars2 = ''
    for _ in range(int2):
        vars2 = connect(vars2, str2)
    return vars2
print(multiply2("bye", 5))
