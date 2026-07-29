class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set() # already cofirmed no cycle
        visiting = set() # currently checking
        adj = defaultdict(list)

        for cur, nei in edges: # goes both ways because undirected
            adj[cur].append(nei)
            adj[nei].append(cur)

        def dfs(node, parent): # pass in parent because undirected
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adj[node]:
                if nei == parent: # if nei is parent, its where we came from
                    continue
                if not dfs(nei, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        for node in range(n):
            if node not in visited: # because undirected, only visit if not yet visited
                if not dfs(node, -1):
                    return False
        return True
        