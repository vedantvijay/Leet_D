class Solution:
    def isGood(self, nums: List[int]) -> bool:
        frequency_map  = Counter(nums)
        
        if(frequency_map[max(nums)]!=2 ):
            return False
        for i in range(1,max(nums)):  
            if(frequency_map[i]!=1):
                return False


        return len(nums)==(max(nums) + 1)