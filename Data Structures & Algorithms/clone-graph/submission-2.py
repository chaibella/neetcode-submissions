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
            if source is None:
                return None # dead end
            if source in mapping:
                return mapping[source] # already cloned
            
            clone = Node(source.val) # otherwise create the clone
            mapping[source] = clone # and make the connection

            for nei in source.neighbors: # and clone the neighbors
                clone.neighbors.append(dfs(nei))
            
            return clone # return clone

        return dfs(node) # start call on node, will return cloned copy
