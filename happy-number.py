def isHappy(n):
    limit = 999999
    for i in range(limit):
        new_num = sum([int(s)**2 for s in str(n)])
        if n == 1:
            return True
        n = new_num
        if n == 4:
            return False

    return False


for i in range(100):
    print("num is:", i, isHappy(i))

for i in range(-1+)
