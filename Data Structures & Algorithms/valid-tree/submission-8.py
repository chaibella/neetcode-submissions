class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        
        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            parent[root_b] = root_a

        return True