class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,distance in roads:
            graph[u].append((v,distance))
            graph[v].append((u,distance))
        q = deque([1])
        visited = set([1])
        mini = float('inf')
        while q:
            curr = q.popleft()
            for neighbor, dist in graph[curr]:
                mini = min(mini, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
            
        return mini 


        


