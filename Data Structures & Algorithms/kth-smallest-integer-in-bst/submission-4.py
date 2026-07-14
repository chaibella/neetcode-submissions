# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        while cur or stack: # while there are nodes to process
            while cur: # will exhaust left side first
                stack.append(cur)
                cur = cur.left # at some point this left will be None
            cur = stack.pop() # last node we visited on the way down
            k -= 1 # decrement k
            if k == 0: # if at nth smallest, return value
                return cur.val
            cur = cur.right # then shift to right for in order traversal
                            # right will be added to stack in next while loop
            

