class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        visiting = set()
        adj = defaultdict(list) # node -> [nei]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(cur, par):
            if cur in visiting:
                return False

            visiting.add(cur)
            
            for nei in adj[cur]:
                if nei == par:
                    continue
                if not dfs(nei, cur):
                    return False
            
            visiting.remove(cur)
            visited.add(cur)
            return True


        for node in range(n):
            if node in visited:
                continue
            if not dfs(node, -1):
                return False
        return True
        