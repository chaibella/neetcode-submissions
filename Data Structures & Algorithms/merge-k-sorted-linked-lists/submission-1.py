# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged.append(self.merge2Lists(list1, list2))
            lists = merged
        return lists[0]

    def merge2Lists(self, list1, list2):
        pre = ListNode()
        one, two, cur = list1, list2, pre

        while one and two:
            if one.val <= two.val:
                cur.next = one
                one = one.next
            else:
                cur.next = two
                two = two.next
            cur = cur.next
        
        cur.next = (one or two)

        return pre.next
    