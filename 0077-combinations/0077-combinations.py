class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        listy = []
        new_list = []
        i = 0
        for j in range(1,n+1):
            listy.append(j)
        def dfs(i,new_list):
            if len(new_list) == k:
                res.append(new_list.copy())
                return 
            if i >= n:
                return 
            if len(new_list)<k:
                new_list.append(listy[i])
                dfs(i+1,new_list)
                new_list.pop()
            dfs(i+1,new_list)
        dfs(i,new_list)
        return res
            
