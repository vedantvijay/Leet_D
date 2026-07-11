class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        c = 0
        
        for i in range(n):
            if i not in visited:
                q = deque([i])
                visited.add(i)
                vc = 0
                deg = 0
                while q:
                    curr = q.popleft()
                    vc +=1
                    deg += len(graph[curr])
                    for n in graph[curr]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)
                if deg == vc*(vc-1):
                    c +=1
        return c