nums = [1, 2, 3]
return_list = []


def create_comb(included, undecided):
    if len(undecided) == 0:
        return

    item = undecided.pop(0)
    create_comb(included[:], undecided[:])
    included.append(item)
    create_comb(included[:], undecided[:])
    return_list.append(included)


create_comb([], nums)
print(sorted(return_list))

nums.append(nums.pop(i))
