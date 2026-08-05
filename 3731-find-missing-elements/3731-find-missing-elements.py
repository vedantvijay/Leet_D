class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        arr = []
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                arr.append(i)
        return arr