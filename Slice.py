nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1000,2000,3000,4000]
#Attempt 1:
add1 = 0
add2 = 0
staller = len(nums) / 4
'''for i in range(int(staller)):
    add1 = add1 + nums[i]
def reverse(elements):
    result = [0] * 16
    for j in range(int(len(elements))-1):
        result[j] = elements[len(elements) - j - 1]
    return result
cur = reverse(nums)
print(cur)
print(nums)
for i in range(int(staller)):
    add2 = add2 + cur[i]
res = add1 + add2
print(res)'''

''''''

#Attempt 2:
num1 = 0
num2 = 0
length = len(nums) / 4
length1 = length * 3
print(length1)
print(length)
for i in range(len(nums)):
    if i < length:
        num1 = num1 + nums[i]
        print(i)
    if i >= length1:
        num2 = num2 + nums[i]
        print(i)
result = num1 + num2
print(result)