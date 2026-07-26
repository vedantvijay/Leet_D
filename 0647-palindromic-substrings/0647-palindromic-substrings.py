class Solution(object):
    def countSubstrings(self, s):
        def ispalindrome(k):
            k_rev = k[::-1]
            if k == k_rev:
                return True
            return False
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if ispalindrome(s[i:j+1]):
                    count = count + 1
        return count