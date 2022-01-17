def commonPrefix(inputs):
    return_arr = []
    d = dict()
    for inp in inputs:

        cur_sum = len(inp)
        i = 1
        while i < len(inp):
            cur_string = inp[i:]
            j = 0
            sum_to_add = 0
            while j < len(cur_string):
                if cur_string[j] == inp[j]:
                    sum_to_add += 1
                    j += 1
                else:
                    break

            cur_sum += sum_to_add
            i += 1

        return_arr.append(cur_sum)

    return return_arr


print(commonPrefix(["ababaa"]))
