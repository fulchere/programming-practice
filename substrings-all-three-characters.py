def numberOfSubstrings(s):
    startWindow = 0
    count = 0
    letters = {'a': 0, 'b': 0, 'c': 0}

    for endWindow in range(len(s)):
        letters[s[endWindow]] += 1

        while all(letters.values()):
            count += len(s)-endWindow

            letters[s[startWindow]] -= 1
            startWindow += 1

    return count
