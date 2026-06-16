class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> s:
        n = len(strs)-1
        if n+1 ==1:
            return strs[0]
        if n+1 == 0:
            return ""
        strs = sorted(strs)
        c = 0
        for i in range(1, len(strs[0]) + 1):
            if strs[0][0:i] == strs[n][0:i]:
                c = i
            else:
                break

        return (strs[0][0:c])