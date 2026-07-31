class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)


        for node in range(n):
            if node in visited:
                continue
            dfs(node, -1)
            count += 1
        
        return count