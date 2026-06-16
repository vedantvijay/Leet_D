class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        nums = [(num, idx) for idx, num in enumerate(nums)]
        res = []

        nums = sorted(nums)
        while left<right:
            if nums[left][0] + nums[right][0] == target:
                res.append(nums[left][1])
                res.append(nums[right][1])
                break
            elif nums[left][0] + nums[right][0] < target:
                left +=1
            elif nums[left][0] + nums[right][0] > target:
                right -= 1
        return res
                