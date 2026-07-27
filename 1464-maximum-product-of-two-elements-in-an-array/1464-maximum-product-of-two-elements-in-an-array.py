class Solution(object):
    def maxProduct(self, nums):
        maxi = [-n for n in nums]
        heapq.heapify(maxi)
        return (-heapq.heappop(maxi)-1)*(-heapq.heappop(maxi)-1)