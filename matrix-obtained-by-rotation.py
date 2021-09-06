def findRotation(mat, target):
    for _ in range(4):
        if mat == target:
            return True
        mat = [list(x) for x in zip(*mat[::-1])]
    return False


print(findRotation(
    [[0, 0, 0], [0, 0, 1], [0, 0, 1]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 1]]))
