def topKFrequent(nums, k: int):
    x = k
    from operator import itemgetter
    dc = dict()
    for num in nums:
        if num in dc:
            dc[num] += 1
        else:
            dc[num] = 1

    l = []
    for k, v in dc.items():
        l.append([k, v])
    l.sort(key=itemgetter(1))

    rtn = []
    for i in range(x):
        rtn.append(l.pop()[0])

    return rtn


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
