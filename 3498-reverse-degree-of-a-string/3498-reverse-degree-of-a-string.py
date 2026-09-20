class Solution(object):
    def reverseDegree(self, s):
        m = 0
        for i,j in enumerate(s):
            m += ((ord(j)-123)*-1)*(i+1)
        return m