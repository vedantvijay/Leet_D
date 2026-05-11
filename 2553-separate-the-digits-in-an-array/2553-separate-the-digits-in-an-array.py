class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        combo = "".join(str(n) for n in nums)
        ans = [int(i) for i in combo]
        return ans