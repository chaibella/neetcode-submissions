# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, cur = None, 0

        def dfs(node):
            nonlocal res, cur
            if res:
                return
            if not node:
                return
            dfs(node.left)
            cur += 1
            if cur == k:
                res = node.val
            dfs(node.right)
            

        dfs(root)
        return res
