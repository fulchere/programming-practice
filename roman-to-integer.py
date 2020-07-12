def romanToInt(s: str) -> int:
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    romans = dict()
    for i in range(len(symbols)):
        romans[symbols[i]] = values[i]

    i = 0
    total = 0
    while i < len(s):
        if s[i] == 'I' and i+1 < len(s):
            if s[i+1] == 'V':
                total += 4
                i += 2
                continue
            if s[i+1] == 'X':
                total += 9
                i += 2
                continue
        if s[i] == 'X' and i+1 < len(s):
            if s[i+1] == 'L':
                total += 40
                i += 2
                continue
            if s[i+1] == 'C':
                total += 90
                i += 2
                continue
        if s[i] == 'C' and i+1 < len(s):
            if s[i+1] == 'D':
                total += 400
                i += 2
                continue
            if s[i+1] == 'M':
                total += 900
                i += 2
                continue
        total += romans[s[i]]
        i += 1
    return total


print(romanToInt("III"))
