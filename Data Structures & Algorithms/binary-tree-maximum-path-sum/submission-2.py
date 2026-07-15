# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0 # nothing to add

            nonlocal res
            left = max(dfs(node.left), 0) # take left only if it adds to sum
            right = max(dfs(node.right), 0) # same, take only if helpful, not if negative
            res = max(res, node.val + left + right) # overtake res if current bend path larger 
            return node.val + max(left, right) # pass up to parent, max of left or right path


        res = root.val
        dfs(root)
        return res

