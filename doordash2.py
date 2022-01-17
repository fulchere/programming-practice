import string
from itertools import combinations


def getMlength(st, M):
    return [st[x:y] for x, y in combinations(range(len(st) + 1), r=2) if len(st[x:y]) == M]


def getSpecialSubstring(s, k, charValue):
    special = ""
    normal = ""
    for i in range(26):
        if int(charValue[i]) == 1:
            special += string.ascii_lowercase[i]
        else:
            normal += string.ascii_lowercase[i]

    current_length = len(s)
    while current_length > 0:
        substrings = getMlength(s, current_length)
        for substring in substrings:
            normal_ct = 0
            for ch in substring:
                if ch in normal:
                    normal_ct += 1
            if normal_ct <= k:
                return len(substring)
        current_length -= 1

    return len(s)


s = 'giraffe'
k = 2
charValue = '01111001111111111011111111'
print("func outputs:", getSpecialSubstring(s, k, charValue), "should be: 3")


s = 'special'
k = 1
charValue = '00000000000000000000000000'
print("func outputs:", getSpecialSubstring(s, k, charValue), "should be: 1")
