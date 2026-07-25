class Solution:
    def maxProduct(self, n: int) -> int:
        m = list(map(int,str(n)))
        e1 = max(m)
        m.remove(e1)
        e2 = max(m)
        return e1*e2