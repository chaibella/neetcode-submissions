# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(ref, sub):
            if not ref:
                return False
            if self.sameTree(ref, sub):
                return True
            return dfs(ref.left, sub) or dfs(ref.right, sub)

        return dfs(root, subRoot)

    def sameTree(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val != b.val:
            return False
        return self.sameTree(a.left, b.left) and \
            self.sameTree(a.right, b.right)
