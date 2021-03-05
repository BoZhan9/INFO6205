import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        count = Counter(S)
        heap = []
        ans = []
        
        for key, value in count.items():
            heap.append((-value, key)) 
        heapq.heapify(heap)
        
        while(len(heap) > 1):
            
            curr = heapq.heappop(heap)
            next = heapq.heappop(heap)
            
            ans.extend([curr[1], next[1]])
            
            if curr[0]< -1:
                heapq.heappush(heap, (curr[0]+1, curr[1]))
            if next [0]< -1:
                heapq.heappush(heap, (next[0]+1, next[1]))
        if heap:
            if heap[0][0] < -1:
                return ""
            ans.append(heap[0][1])
            
        return "".join(ans)
                    