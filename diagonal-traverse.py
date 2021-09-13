def findDiagonalOrder(mat):
    row = 0
    col = 0
    ans = []

    up = True
    while row < len(mat) and col < len(mat[0]):
        ans.append(mat[row][col])
        # MOVING UP
        if up:
            # AT RIGHT SIDE
            if col == len(mat[0]) - 1:
                row += 1
                up = False
            # AT TOP
            elif row == 0:
                col += 1
                up = False

            else:
                row -= 1
                col += 1

        # MOVING DOWN
        else:
            # AT BOTTOM
            if row == len(mat) - 1:
                col += 1
                up = True
            # AT LEFT SIDE
            elif col == 0:
                row += 1
                up = True
            else:
                row += 1
                col -= 1
    return ans


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findDiagonalOrder(mat))
