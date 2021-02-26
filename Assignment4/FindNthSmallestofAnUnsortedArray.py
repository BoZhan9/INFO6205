class Solution:
    def NthSmallest(self, n, nums):
        length = len(nums)
        return self.helper(nums, 0, length - 1, n - 1)
    
    def helper(self, nums, start, end, n):
        if start == end or start >= end:
            return nums[start]
        
        left = start
        right = end
        mid = (left + r) // 2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if start <= right and n <= right:
            return self.helper(nums, start, right, n)
        if left <= end and n >= left:
            return self.helper(nums, left, end, n)

        return nums[n]