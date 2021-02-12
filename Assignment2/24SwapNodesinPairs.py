# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:    
            temp = curr.next.next
            curr.next.next = temp.next
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next
        return dummy.next