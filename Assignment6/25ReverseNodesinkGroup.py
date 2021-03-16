# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        len = 1
        start = head
        # get length
        while start.next is not None:
            start = start.next
            len += 1
        return self.helper(head, k, len)
            
    def helper(self, head, k, len):
        if len < k:
            return head
        
        curr = head
        prev = None
        
        # reverse k
        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = self.helper(curr, k, len - k)
        return prev
        
        