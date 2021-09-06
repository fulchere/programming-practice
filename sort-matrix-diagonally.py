def diagonalSort(mat):
    n_cols = len(mat[0])
    n_rows = len(mat)

    for j in range(n_rows):
        cur = []
        i = 0
        j_e = j
        while i < n_cols and j < n_rows:
            cur.append(mat[j][i])
            i += 1
            j += 1
        cur.sort()

        i = 0
        while i < n_cols and j_e < n_rows:
            mat[j_e][i] = cur[i]
            i += 1
            j_e += 1

    for i in range(1, n_cols):
        cur = []
        j = 0
        i_e = i
        while i < n_cols and j < n_rows:
            cur.append(mat[j][i])
            i += 1
            j += 1
        cur.sort()

        j = 0
        while i_e < n_cols and j < n_rows:
            mat[j][i_e] = cur[j]
            i_e += 1
            j += 1

    return mat


assert(diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]) == [
       [1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]])

assert(diagonalSort([[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52], [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4], [84, 28, 14, 11, 5, 50]]) == [
       [5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]])
