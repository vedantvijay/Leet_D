class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1 = nums[-1]*nums[-2]
        third1 = nums[-3]
        n2 = nums[0]*nums[1]
        third2 = nums[-1]
        return max(n1*third1,n2*third2)