class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = defaultdict(list)
        trusti = set()
        for u, v in trust:
            graph[v].append(u)
            trusti.add(u)
        for i,j in graph.items():
            if len(j) == n-1 and i not in trusti:
                return i

        print(graph)
        return -1