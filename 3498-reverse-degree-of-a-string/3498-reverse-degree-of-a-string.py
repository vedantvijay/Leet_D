class Solution(object):
    def reverseDegree(self, s):
        m = 0
        for i,j in enumerate(s):
            m += ((123-ord(j)))*(i+1)
        return m