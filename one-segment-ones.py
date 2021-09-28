class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        tot = 0
        for ch in s.split("0"):
            if len(ch) > 0:
                tot += 1
            if tot > 1:
                return False
        return True if tot == 1 else False
