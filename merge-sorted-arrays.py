def merge(l1, l2):
    l = []
    while l1 and l2:
        if l1[0] < l2[0]:
            l.append(l1.pop(0))
        else:
            l.append(l2.pop(0))

    if l1 and not l2:
        l += l1
    else:
        l += l2

    return l


def split(l1, l2)
