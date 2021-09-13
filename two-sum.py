def twoSum(nums, target):
    d = dict()

    for i, n in enumerate(nums):
        cur = target-n
        d[cur] = [n, i]

    for i, n in enumerate(nums):
        if n in d and d[n][1] != i:
            k, l = nums.index(n), nums.index(d[n][0])
            return [k, l] if k != l else [k, 1+k+nums[k+1:].index(d[n][0])]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
