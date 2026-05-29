class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        j=0
        
        for i in nums:
            c = list(str(i))
            for index,char in enumerate(c):
                j+= int(c[index])
            res.append(j)
            j=0
        
        return min(res)