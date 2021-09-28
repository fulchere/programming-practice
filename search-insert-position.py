def searchInsert(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo != hi:
        mid = ((hi-lo)//2)+lo
        print('hi:', hi, 'lo:', lo, 'mid:', mid)
        print('nums:', nums, 'target:', target)
        if target < nums[mid]:
            hi = mid
        if target > nums[mid]:
            lo = mid + 1
        if target == nums[mid]:
            return mid

    return lo+1 if nums[lo] < target else lo


nums = [1, 2, 5, 6]
target = 5
print(searchInsert(nums, target))

nums = [1, 2, 5, 6]
target = 2
print(searchInsert(nums, target))

nums = [1, 2, 5, 6]
target = 7
print(searchInsert(nums, target))

nums = [1, 2, 5, 6]
target = 0
print(searchInsert(nums, target))

nums = [1]
target = 0
print(searchInsert(nums, target))
