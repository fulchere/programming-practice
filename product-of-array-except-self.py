
def productExceptSelf(nums: int):
    left = [nums[0]]
    right = [nums[-1]]
    for i in range(1, len(nums)-1):
        left.append(left[i-1]*nums[i])
        right.append(right[i-1]*nums[len(nums)-i-1])
    print("left:", left)
    print("right", right)

    right = right[::-1]
    output = [right[0]]

    for i in range(1, len(nums)):
        l = left[i-1] if i else 1
        r = right[i] if i < len(right) else 1
        output.append(l*r)

    return output


print(productExceptSelf([1, 2, 3, 4]))
