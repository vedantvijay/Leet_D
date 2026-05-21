class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return ([s.index(char) for char in s] == [t.index(char) for char in t])