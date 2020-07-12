
def groupAnagrams(strs):
    from operator import itemgetter

    strs_set = [[sorted(list(s)), i] for i, s in enumerate(strs)]
    strs_set.sort(key=itemgetter(0))

    prev = None
    rtn_list = []
    t_ls = []
    for item in strs_set:
        if prev is None:
            prev = item
            t_ls.append(strs[prev[1]])
            continue

        if item[0] == prev[0]:
            t_ls.append(strs[item[1]])
            prev = item
        else:
            prev = item
            rtn_list.append(t_ls)
            t_ls = [strs[prev[1]]]
    rtn_list.append(t_ls)

    return rtn_list


inp = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(inp))


for i in range(-4, 0):
    print(i)
