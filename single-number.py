def singleNumber(nums) -> int:
    nums.sort()
    i = 0
    while True:
        if i == len(nums)-1 or nums[i] != nums[i+1]:
            return nums[i]
        i += 2


print(singleNumber([4, 1, 2, 1, 2]))
