def merge(nums1, m, nums2, n):
    nums1 = nums1[:len(nums1)-n]
    i = 0
    while nums2:
        val = nums2[0]
        # at front
        if i == 0 and val < nums1[0]:
            nums1.insert(0, val)
            print("AAA")
            nums2.pop(0)

        # at end of array
        elif i+1 == len(nums1):
            idx = i if val < nums1[i] else i + 1
            nums1.insert(idx, val)
            print("BBB")
            nums2.pop(0)

        # middle
        elif val >= nums1[i] and val <= nums1[i + 1]:
            nums1.insert(i+1, val)
            print("CCC")
            nums2.pop(0)

        elif val > nums1[i]:
            i += 1
            print("DDD")
    print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
