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
            nonlocal vals
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return ','.join(vals)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs():
            nonlocal i
            if i == len(vals):
                return None
            if vals[i] == '#':
                i += 1
                return None
            root = TreeNode(int(vals[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root
    
        vals = data.split(',')
        i = 0
        return dfs()




