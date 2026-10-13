class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = sorted(x*x for x in nums)
        odd = 0
        even = 0

        left = 0
        right = len(num) - 1

        for i in range(len(num)):
            if (i+1) % 2 == 0:
                even -= num[left]
                left += 1
            else:
                odd += num[right]
                right -= 1

        return odd + even