class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        right = 0
        left = 0
        res = []
        count = 0
        d = defaultdict(int)
        while right<len(s):
            d[s[right]] += 1
            while d['a']>=1 and d['b']>=1 and d['c']>=1:
                
                count += len(s) - right
                d[s[left]] -= 1
                left = left+1
            
            right = right + 1
        
        return count

            
