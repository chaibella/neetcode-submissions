class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        adj = defaultdict(list) # node -> [neighbors], both ways (undirected)
        visited = set() # already checked, no cycles
        visiting = set() # checking for cycles, exclude parent (undirected)

        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)

        def dfs(node, parent):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue # don't go backwards
                if not dfs(nei, node):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True


        for node in range(n):
            if node in visited:
                continue
            if not dfs(node, -1):
                return False

        return True




