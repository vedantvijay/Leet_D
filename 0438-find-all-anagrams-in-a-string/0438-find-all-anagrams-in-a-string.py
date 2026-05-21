class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p = sorted(p)
        l = 0

        for r in range(len(p) - 1, len(s)):
            if sorted(s[l:r + 1]) == p:
                res.append(l)
            l += 1
                
        return res