# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next

        # reverse right half
        pre, cur = None, middle
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # then sever the 2 lists to prevent cycle
        slow.next = None

        # merge the two
        one, two = head, pre
        while two:
            tmp = one.next
            one.next = two
            one = two
            two = tmp



