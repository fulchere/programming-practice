import string
from itertools import combinations


def getSpecialSubstring(s, k, charValue):
    special = ""
    normal = ""
    for i in range(26):
        if int(charValue[i]) == 1:
            special += string.ascii_lowercase[i]
        else:
            normal += string.ascii_lowercase[i]
    subs = []
    lo = 0
    hi = 1
    while lo < len(s):
        cur = s[lo:hi]
        total_normal = 0
        for ch in cur:
            if ch in normal:
                total_normal += 1
        if total_normal <= k:
            subs.append(cur)
        hi += 1
        if hi > len(s):
            lo += 1
            hi = lo + 1

    return len(max(subs, key=len))


s = 'giraffe'
k = 2
charValue = '01111001111111111011111111'
print("func outputs: ", getSpecialSubstring(s, k, charValue), " should be: 3")
