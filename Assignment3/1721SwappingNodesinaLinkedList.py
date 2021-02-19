# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length = length + 1
        front = head
        back = head
        print(length)

        for _ in range(k - 1):
            if front:
                front = front.next
 
        for _ in range(length - k):
            if back:
                back = back.next        
        
        temp = front.val
        front.val = back.val
        back.val = temp
        
        return head