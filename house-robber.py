def rob(nums):
    i = 0
    while i < len(nums):
        print("top of loop", i, len(nums))
        if i == 0:
            i += 1
            continue
        if i == 1:
            if nums[i] < nums[i-1]:
                nums[i] = nums[i-1]
        if i > 1:
            if nums[i] + nums[i-2] > nums[i-1]:
                nums[i] = nums[i] + nums[i-2]
            else:
                nums[i] = nums[i-1]
        i += 1
    return max(nums)


print(rob([1, 2, 3, 1]))
for i in range(5):
    print(i)


print(rob([2, 7, 9, 3, 1]))
#assert rob([1, 2, 3, 1]) == 4
#assert rob([2, 7, 9, 3, 1]) == 12
