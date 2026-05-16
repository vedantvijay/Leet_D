class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        var = frequency.most_common(k)
        l =[]
        for i in var:
            l.append(i[0])
        return l

        