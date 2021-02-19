# Implement a doubly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def addToTail(self, x):
        node = ListNode(x)
        tail = self.head
        node.next = None
        if head is None:
            head.prev = None
            self.head = node
            return
        while tail.next is not None:
            tail = tail.next
        
        last.next = node
        node.prev = last
        self.size += 1
    
    def addToHead(self, x):
        node = ListNode(x)
        node.next = head
        node.prev = None
        if head is not None:
            self.head.prev = node
        self.head = node
        self.size += 1

    def printSize(self):
        return self.size

    def printList(self):
        curr = head
        while curr.next is not None:
            print(curr.val + "")