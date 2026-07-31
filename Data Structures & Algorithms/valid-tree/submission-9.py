class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check count of edges (less means tree disconnected, more means cycle)
        if len(edges) != n - 1:
            return False

        # track visited nodes
        visited = set()
        # create an adj list, both ways
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # dfs that takes node and parent, dives into node's children/neighbors
        def dfs(node, parent):
            if node in visited:
                return False # cycle
            
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        # process every unvisited node
        for node in range(n):
            if node not in visited:
                if not dfs(node, -1):
                    return False
        return True
