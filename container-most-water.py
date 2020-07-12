def maxArea(height):
    from operator import itemgetter
    l = []
    for i, h in enumerate(height):
        l.append([h, i])
    l.sort(key=itemgetter(0), reverse=True)
    print(l)
    highest = 0
    for i in range(len(l)//2):
        for j in range(len(l)//2):
            if i != j:
                h = min(l[i][0], l[j][0]) * \
                    abs(l[i][1] - l[j][1])
                if h > highest:
                    highest = h

    return highest


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
