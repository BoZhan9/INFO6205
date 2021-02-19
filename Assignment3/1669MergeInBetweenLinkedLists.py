# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = list1
        end = list1
        for _ in range(a - 1):
            if start:
                start = start.next
            else:
                return list1
        for _ in range(b + 1):
            if end:
                end = end.next
            else:
                return list1
        start.next = list2
        while list2.next:
            list2 = list2.next
        
        list2.next = end
        return list1