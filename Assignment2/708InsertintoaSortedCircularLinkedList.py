"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            head = node
            node.next = node
            return head
        
        temp = head.next
        while not (insertVal > temp.val and insertVal <= temp.next.val) and not (temp.next.val < temp.val and (insertVal <= temp.next.val or insertVal >= temp.val)) and temp != head:
            temp = temp.next
        
        node = Node(insertVal)
        next = temp.next
        temp.next = node
        node.next = next
        
        return temp