class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        new_list = []
        i = 0
       
        def check_all(i,target,new_list):
            if target == 0:
                res.append(new_list.copy())
                return 
            if i >= len(candidates):
                return 
            if candidates[i] <= target:
                new_list.append(candidates[i])
                check_all(i, target - candidates[i], new_list)
                new_list.pop()
            check_all(i+1, target, new_list)
            
        check_all(i,target,new_list)
        return res
            
            
