def maxSubArray(nums):
    max_sum = 0

    lo = 0
    hi = 1

    while hi <= len(nums):
        cur_sum = sum(nums[lo:hi])
        if cur_sum > max_sum:
            max_sum = cur_sum
            hi += 1
        else:
            lo += 1

    return max_sum
