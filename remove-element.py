def removeElement(nums, val):
    i = 0

    def fn(s):
        return True if s == val else False
    nums.sort(key=fn)
    print(nums)
    return nums.count(val)


nums = [3, 2, 2, 3]
val = 3
print(removeElement(nums, val))

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(nums, val))
