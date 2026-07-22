"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {} # source -> clone

        def dfs(source):
            if not source:
                return None
            if source in mapping:
                return mapping[source]
            
            clone = Node(source.val)
            mapping[source] = clone
            for neigh in source.neighbors:
                clone.neighbors.append(dfs(neigh))
            return clone

        return dfs(node)