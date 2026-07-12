class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(set(arr))
        d = {}
        l = []
        for i,j in enumerate(new_arr):
            d[j] = i+1
        for i in arr:
            l.append(d[i])     
        return l   