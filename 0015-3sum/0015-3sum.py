class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        result =[]
    
        for k in range(len(nums)-1):
            if k>0 and nums[k]==nums[k-1]:
                continue
            left = k+1
            right = len(nums)-1

            while left<right:
                current_sum = nums[k]+nums[left]+nums[right]
                if current_sum == 0:
                    result.append([nums[k],nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]:
                        left +=1
                    while left<right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1
                elif current_sum <0:
                    left +=1
                else:
                    right -=1

        

        return result