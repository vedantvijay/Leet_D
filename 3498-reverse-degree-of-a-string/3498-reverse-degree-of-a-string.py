class Solution(object):
    def reverseDegree(self, s):
        l = []
        for i,j in enumerate(s):
            l.append(abs(ord(j)-123)*(i+1))
        print(l)
        return sum(l)