arr = [ 1,2,3]
nums = []
integer = 0
'''
for i in range(len(arr)):
    integer = str(integer) + str(arr[i])
integer = integer.replace(integer[0], "")
integer = int(integer)
integer = integer + 1
integer = str(integer)
for i in range(len(integer)):
    nums.append(integer[i])
for i in range(len(nums)):
    nums[i] = int(nums[i])
print(nums)
print(len(arr))
'''
integer = 0
index = 0
print(range(len(arr), 0))
stall = 0
for i in range(len(arr)):
    integer = integer * 10
    integer = integer + arr[i]
    stall = stall + 1
print(integer)
integer += 1
stall += 1
print(integer)
nums = []
for i in range(stall):
    nums.append(int(integer%10))
    integer = integer - integer % 10
    integer = integer / 10
nums.reverse()
if nums[0] == 0:
    print(nums[0])
    nums.remove(nums[0])
print(nums)