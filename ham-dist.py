def totalHammingDistance(nums):
    total = 0
    while nums:
        cur = nums[0]
        nums.pop(0)
        for n in nums:
            total += bin(cur ^ n).count('1')

    return total


n = [4, 14, 2]
print(totalHammingDistance(n))
