class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([source])
        visited = set()
        visited.add(source)

        while queue:
            node = queue.popleft()
            if destination in visited:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        return False