from collections import defaultdict, deque

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= len(self.bit) - 1:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        ans = 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= idx & -idx
        return ans


class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7

        arr0 = []
        arr1 = []
        arr2 = []

        for x in nums:
            if x < a:
                arr0.append(x)
            elif x > b:
                arr2.append(x)
            else:
                arr1.append(x)

        target = arr0 + arr1 + arr2

        # Map each value to all of its positions in the target array
        pos = defaultdict(deque)
        for i, x in enumerate(target):
            pos[x].append(i)

        # Build permutation of target indices
        perm = []
        for x in nums:
            perm.append(pos[x].popleft())

        bit = Fenwick(len(nums))
        swaps = 0

        # Count inversions
        for i in range(len(nums) - 1, -1, -1):
            swaps += bit.query(perm[i] - 1)
            bit.update(perm[i], 1)

        return swaps % MOD