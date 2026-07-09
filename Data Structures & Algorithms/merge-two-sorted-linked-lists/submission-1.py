# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        cur, one, two = pre, list1, list2

        while one and two:
            if one.val <= two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next
            cur = cur.next
        
        if one:
            cur.next = one
        if two:
            cur.next = two
        return pre.next