class Solution(object):
    def reverseDegree(self, s):
        m = 0
        for i,j in enumerate(s):
            m = m + abs(ord(j)-123)*(i+1)

        return m