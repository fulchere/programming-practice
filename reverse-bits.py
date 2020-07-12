def reverseBits(n):
    n = str(n).zfill(32)
    print(n)
    return int(str(n)[::-1], 2)


print(reverseBits(int(10100101000001111010011100)))
