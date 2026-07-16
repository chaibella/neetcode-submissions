# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val)) # preorder, root first then children, pre-stringify
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return ','.join(vals) # don't forget to return as joined string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs():
            nonlocal i
            if vals[i] == '#':
                i += 1 # still need to move past current nth val
                return None
            root = TreeNode(vals[i])
            i += 1 # also dont forget to move past non-null node
            root.left = dfs() # i increments inside
            root.right = dfs() # same, i handled inside
            return root

        vals = data.split(',')
        i = 0 # track which val in vals
        return dfs()



