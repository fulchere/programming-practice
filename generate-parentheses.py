class Solution:
    ls = []

    def helper(self, l, r, s):
        if l and r and l < r:
            self.helper(l-1, r, s + "(")
            self.helper(l, r-1, s + ")")
        elif l and r:
            self.helper(l-1, r, s + "(")
        elif not l and r:
            self.helper(l, r-1, s+")")
        elif not l and not r:
            self.ls.append(s)
            return

    def generateParenthesis(self, n: int):
        l, r = n, n
        self.helper(l, r, "")
        return self.ls


sl = Solution()
print(sl.generateParenthesis(1))
