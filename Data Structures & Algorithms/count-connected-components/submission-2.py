class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # track groups and visited nodes
        count = 0
        visited = set()

        # adj list to track both ways (undirected)
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # dfs to recurse into all connected nodes
        def dfs(node):
            if node in visited:
                return # already counted toward current group (in cycles)
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            return

        # start dfs on every unvisited/new group
        for node in range(n):
            if node in visited:
                continue # part of another group
            dfs(node)
            count += 1 # add new group

        return count