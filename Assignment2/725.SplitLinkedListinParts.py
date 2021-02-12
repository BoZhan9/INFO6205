# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count = 0
        temp = root
        while temp:
            count = count + 1
            temp = temp.next
        
        div = count // k
        mod = count % k
        
        ans = []
                     
        for i in range(0, k):
            temp = []
            j = 0
            d = div
            if i < mod:
                d = d + 1
            
            while j < d:
                if j == 0:
                    ans.append(root)
                head = root
                root = root.next
                if j == d - 1:
                    head.next = None
                j = j + 1
            
        if len(ans) < k:
            for i in range(0, k - len(ans)):
                ans.append(None)
            
        return ans