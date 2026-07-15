import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a = 2
        b = 1
        l = []
        l.append(a)
        m = []
        m.append(b)
        for i in range(n-1):
            a = a+2
            l.append(a)
            b = b+2
            m.append(b)
        
        return(math.gcd(sum(l),sum(m)))
    
        