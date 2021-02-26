class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        length = len(arr)

        while length > 0:
            k = arr.index(length) + 1
            if k == length: 
                length -= 1
                continue
            ans.append(k)
            arr = arr[k-1::-1] + arr[k:]
            ans.append(length)
            arr = arr[length-1::-1] + arr[length:]
            length -= 1
        return ans
        
        