

def toNum(s):
    ord('A')-64
    s = s[::-1]
    num = 0
    for i in range(len(s)):
        num += (ord(s[i])-64)*26**i

    return num


s = "A"
s1 = "AB"
s2 = "ZY"
print(toNum(s))
print(toNum(s1))
print(toNum(s2))
