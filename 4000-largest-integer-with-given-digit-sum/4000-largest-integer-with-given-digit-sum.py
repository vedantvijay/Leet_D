class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        ans = 0
        if n == 1 and s<10:
            return s
        if s > int(n * 9):
            return -1
        else:
            m = s%9
            print(m)
            k = s//9
            if k == n :
                ans = ("9"*k)
            else:
                ans = ("9"*k) + str(m) + "0" * (n - k - 1)
        return int(ans)
            
            