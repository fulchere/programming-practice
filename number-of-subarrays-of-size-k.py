def numOfSubarrays(arr, k, threshold):
    lo = 0
    hi = k-1
    cur_avg = sum(arr[0:hi+1])/k
    cnt = 0

    while hi < len(arr):
        print("cur_avg is:", cur_avg)
        if cur_avg >= threshold:
            cnt += 1

        cur_avg -= arr[lo]/k
        lo += 1
        hi += 1
        if hi >= len(arr):
            break
        cur_avg += arr[hi]/k

    return cnt


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
numOfSubarrays(arr, k, threshold)


arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
numOfSubarrays(arr, k, threshold)
