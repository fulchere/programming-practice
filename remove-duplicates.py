def removeDuplicates(nums):
    print(nums)
    nums[:] = list(set(nums))
    print(nums)
    return len(nums)


n = [1, 1, 2]
print(removeDuplicates(n))
print(n)
