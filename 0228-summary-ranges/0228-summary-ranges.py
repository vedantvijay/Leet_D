class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        l = []
        li = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                li.append(nums[i])

            else:
                l.append(li)
                li = [nums[i]]
        l.append(li)
        bkl = []
        for i in l:
            if len(i)==1:
                bkl.append(str(i[0]))
            else:
                bkl.append(str(i[0])+"->"+str(i[-1]))
    

        return bkl


