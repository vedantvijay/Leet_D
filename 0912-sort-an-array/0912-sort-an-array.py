class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = heapify(nums)
        res = []
        while nums:
            res.append(heappop(nums))
        return res