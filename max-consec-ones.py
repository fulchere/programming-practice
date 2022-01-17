def longestOnes(nums, k):
    lo = 0
    hi = 0
    max_ones = -1
    cur = nums[lo:hi+1]
    zs = 0
    while hi < len(nums):
        if zs > k:
            lo += 1
            if cur.pop(0) == 0:
                zs -= 1

        hi += 1
        if hi < len(nums):
            cur.append(nums[hi])
            if cur[-1] == 0:
                zs += 1

        ones = hi - lo

        if ones > max_ones:
            max_ones = ones
    return max_ones


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))

nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(longestOnes(nums, k))


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(longestOnes(nums, k))

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         lo = 0
#         hi = 0
#         max_ones = -1

#         while hi < len(nums):
#             cur = nums[lo:hi+1]
#             if cur.count(0) <= k:
#                 hi += 1
#             else:
#                 lo += 1
#                 hi += 1
#             ones = hi - lo

#             if ones > max_ones:
#                 max_ones = ones
#         return max_ones
