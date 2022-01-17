def subarraySumNSQUAREDALG(nums, k):
    total = 0

    for start in range(len(nums)):

        cur_sum = 0
        for movingptr in range(start, len(nums)):
            cur_sum += nums[movingptr]

            if cur_sum == k:
                total += 1

    return total


def subarraySumLINEARTIMEALG(nums, k):
    count = 0
    tot = 0
    vals = {0: 1}

    for val in nums:
        tot += val

        count += vals.get(tot - k, 0)
        vals[tot] = vals.get(tot, 0) + 1

    return count
