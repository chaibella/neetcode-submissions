class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visited = set()
        adj = defaultdict(list) # node -> [nei]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        for node in range(n):
            if node in visited:
                continue
            if not dfs(node, -1):
                return False
        return True