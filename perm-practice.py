def perm(l):
    if len(l) == 0:
        return []

    if len(l) == 1:
        return [l]

    rtn = []
    for i in range(len(l)):
        item = l[i]

        remainingList = l[:i] + l[i+1:]
        for p in perm(remainingList):
            rtn.append([item]+p)
    return rtn


print(perm([1, 2, 3]))
