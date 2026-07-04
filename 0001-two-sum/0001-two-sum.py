class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i,c in enumerate(nums):
            comp = target - c
            if comp in num_map:
                return [num_map[comp],i]
            num_map[c] = i
        return []
        
