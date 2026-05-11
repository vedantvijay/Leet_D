class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        reversed_nums = nums[::-1]

        return nums + reversed_nums
