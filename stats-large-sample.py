def sampleStats(count):
    a = count
    i = 0
    for val in count:
        a += [i]*val
        i += 1
    count = a[:]
    count.sort()

    if len(count) % 2 == 0:
        median = (count[len(count)//2-1] + count[len(count)//2])/2
    else:
        median = count[len(count)//2]

    d = dict()
    m = -1
    mv = None
    for v in count:
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
        if d[v] > m:
            mv = v

    return [min(count), max(count), sum(count)/len(count), median, mv]
