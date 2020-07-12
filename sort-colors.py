def sortColors(nums):
    i = 0
    len_counter = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.insert(0, nums.pop(i))
        if nums[i] == 2:
            nums.append(nums.pop(i))
            print(nums)
            if len_counter > len(nums):
                break
            len_counter += 1
            continue
        i += 1


n = [1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 2, 2, 2, 0, 1, 2, 1, 0, 2, 1, 0]
sortColors(n)
print(n)

n2 = [2, 0, 2, 1, 1, 0]
sortColors(n2)
print(n2)

n3 = [1, 1, 1, 2, 2, 0, 1]
sortColors(n3)
print(n3)
