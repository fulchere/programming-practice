def generate(numRows: int):
    triangle = [[] for n in range(numRows)]
    for row in range(numRows):
        if row == 0:
            triangle[row].append(1)
            continue
        if row == 1:
            triangle[row].append(1)
            triangle[row].append(1)
            continue
        for col in range(row-1):
            triangle[row].append(triangle[row-1][col]+triangle[row-1][col+1])
        triangle[row].append(1)
        triangle[row].insert(0, 1)
    return triangle


for i in range(6):
    print(generate(i))
