nums = [8, 4, 6, 7, 9, 5, 0, 6, 1, 10]
realnums = nums.copy
times = []
times_appeared = 0
'''
for i in range(len(nums)):
    times_appeared = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            times_appeared += 1
    times.append(times_appeared)
'''
print(times)
times = [0] * len(nums)
times_appeared = 0
time = 0
thing = 0
coor = [0] * len(nums)
index = {

}
for i in range(len(nums)):
    index.update({nums[i]: nums.index(nums[i])})
nums.sort()
print(nums)


print(index)
prev = 0
next = 0
for i in range(len(nums)):
    times[i] = index.get(nums[i])
    times_appeared = times_appeared + 1
print(times)
#print(times)

nums = [8, 4, 6, 7, 9, 5, 0, 6, 1, 10]
list = []
for i in range(len(nums)):
    if i == 0 and nums[i - 1] > nums[i]:
        list.append(nums[i])
    prev = nums[i - 1]
    try:
        next = nums[i+1]
    except IndexError:
        break
    print(prev, nums[i], next)
    if nums[i] > prev and nums[i] > next:
        list.append(nums[i])

list.append(nums[-1])
print(list)



























































































