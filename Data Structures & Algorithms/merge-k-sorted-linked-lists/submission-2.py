# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, head in enumerate(lists):
            heapq.heappush(heap, (head.val, i, head))

        pre = ListNode()
        cur = pre

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            cur = cur.next

        return pre.next

