def longestCommonPrefix(strs):
    p = ""
    i = 0
    while True:
        try:
            prefix = "".join([n[i] for n in strs])
            if prefix.count(prefix[0]) == len(prefix):
                p += prefix[0]
            else:
                return p
            i += 1
        except IndexError:
            return p


s = ["flower", "flow", "flight"]
print(longestCommonPrefix(s))
