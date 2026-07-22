"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {} # original node -> deep copied clone

        def dfs(orig):
            if not orig:
                return None # empty graph
            if orig in mapping:
                return mapping[orig] # previously cloned

            clone = Node(orig.val) # else create clone
            mapping[orig] = clone # add the connection

            for nei in orig.neighbors:
                clone.neighbors.append(dfs(nei)) # and clone the neighbors
            
            return clone # return deep copied clone

        return dfs(node) # call with first node, return deep cloned clone


