def isValid(s):
    opening = "({["
    closing = ")}]"
    if len(s) == 0:
        return True
    if len(s) % 2 != 0:
        return False
    parenth = []
    for P in s:
        if P in opening:
            parenth.append(P)
            continue
        if P in closing:
            if parenth and opening.index(parenth[-1]) == closing.index(P):
                parenth.pop()
            else:
                return False
    if parenth:
        return False
    return True


ss = ["()", "()[]{}", "(]", "([)]", "{[]}"]
for sss in ss:
    print(isValid(sss))
