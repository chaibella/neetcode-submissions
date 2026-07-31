class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # check that edges count makes sense (length == n - 1)
        #   less means the tree is disconnected somewhere
        #   more means the tree has a cycle
        if len(edges) != n - 1:
            return False

        visited = set()

        # adj list, both ways
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # the recursion, if in visited there is cycle, skip parent
        def dfs(cur, par):
            if cur in visited:
                return False # cycle
            visited.add(cur)
            for nei in adj[cur]:
                if nei == par: # skip incoming node/parent
                    continue
                if not dfs(nei, cur):
                    return False
            return True

        # recurse into every unvisited node
        for node in range(n):
            if node in visited:
                continue
            if not dfs(node, -1):
                return False
        return True