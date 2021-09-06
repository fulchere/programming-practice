def isLongPressedName(name, typed) -> bool:
    if name == typed:
        return True

    n = [[name[0], 1]]
    t = [[typed[0], 1]]

    for ch in name[1:]:
        if n[-1][0] == ch:
            n[-1][1] += 1
        else:
            n.append([ch, 1])

    for ch in typed[1:]:
        if t[-1][0] == ch:
            t[-1][1] += 1
        else:
            t.append([ch, 1])
    if len(n) != len(t):
        return False
    for i in range(len(n)):
        if n[i][1] <= t[i][1] and n[i][0] == t[i][0]:
            continue
        else:
            return False
    return True


name = "alex"
typed = "aaleex"
print(isLongPressedName(name, typed))
name = "saeed"
typed = "ssaaedd"
print(isLongPressedName(name, typed))
name = "leelee"
typed = "lleeelee"
print(isLongPressedName(name, typed))
name = "laiden"
typed = "laiden"
print(isLongPressedName(name, typed))
name = "saeed"
typed = "ssaaedd"
print(isLongPressedName(name, typed))
name = "vtkgn"
typed = "vttkgnn"
print(isLongPressedName(name, typed))
name = "a"
typed = "aaaaaaaaaaaaaaaaa"
print(isLongPressedName(name, typed))
name = "xnhtq"
typed = "xhhttqq"
print(isLongPressedName(name, typed))
