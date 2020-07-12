def letterCombinations(digits):
    d = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    r = [""] if digits else []
    for num in digits:
        r = [p+q for p in r for q in d[int(num)]]
    return r


print(letterCombinations("23"))
