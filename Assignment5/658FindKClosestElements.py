class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr is None or len(arr) == 0:
            return arr
        
        ans = []
        index = self.get_index(arr, x)
        left, right = index - 1, index
        for i in range(k):
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right == len(arr):
                ans.append(arr[left])
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
    
        return sorted(ans)
                  
    def get_index(self, arr, x):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid
            elif arr[mid] >= x:
                right = mid
                
        if arr[left] >= x:
            return left
        if arr[right] >= x:
            return right
        
        return len(arr)
