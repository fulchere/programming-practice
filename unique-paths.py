class Solution:
    ct = 0

    def helper(self, dn, rt):
        if dn and rt:
            self.helper(dn-1, rt)
            self.helper(dn, rt-1)
        else:
            self.ct += 1
            return

    def uniquePaths(self, m: int, n: int):
        self.ct = 0
        self.helper(m-1, n-1)
        return self.ct


s = Solution()
print(s.uniquePaths(23, 12))
