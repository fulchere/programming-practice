n = [1, 2, 3, 4]


def perms(n, k=0):
    if k == len(n):
        print(n)
    else:
        for i in range(k, len(n)):
            n[k], n[i] = n[i], n[k]
            perms(n, k+1)
            n[k], n[i] = n[i], n[k]


perms(n)
