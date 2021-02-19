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
        if self.head is None:
            node.prev = None
            self.head = node
            return
        while tail.next is not None:
            tail = tail.next
        
        tail.next = node
        node.prev = tail
        self.size += 1
    
    def addToHead(self, x):
        node = ListNode(x)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.size += 1

    def printSize(self):
        print("Size: " + str(self.size))

    def printList(self):
        curr = self.head
        res = "List: "
        while curr is not None:
            res = res + str(curr.val) + " "
            curr = curr.next
        print(res)
            
d = DoublyLinkedList()
d.addToTail(3)
d.addToHead(4)
d.addToTail(5)
d.printList()
d.printSize()