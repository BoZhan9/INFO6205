# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        start = head
        while start:
            for _ in range(m - 1):
                if start:
                    start = start.next
                else:
                    return head
                
            end = start
            for _ in range(n + 1):
                if end:
                    end = end.next
                else:
                    if start:
                        start.next = end
                    return head
            start.next = end
            start = start.next
        return head