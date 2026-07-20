class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        
        # Pattern 1: All 0s
        ans = ones
        
        # Pattern 2: All 1s
        ans = min(ans, n - ones)
        
        # Pattern 3: Exactly one 1
        if n >= 1:
            ans = min(ans, ones - 1 if ones > 0 else 1)
            
        # Pattern 4: Exactly two 1s at the very ends (100...001)
        if n >= 2:
            cost_ends = (s[0] == '0') + (s[-1] == '0')
            ones_in_middle = ones - (s[0] == '1') - (s[-1] == '1')
            ans = min(ans, cost_ends + ones_in_middle)
            
        return ans