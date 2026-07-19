class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        seen1 = 0  
        seen2 = 0   

        swaps = 0

        for x in nums:
            if x < a:
                swaps += seen1 + seen2
            elif x <= b:
                swaps += seen2
                seen1 += 1
            else:
                seen2 += 1

        return(swaps)%MOD
