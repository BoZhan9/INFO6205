# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return        
        
        odd = head
        even = head.next
        temp = head.next
        
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        
        odd.next = temp
        return head