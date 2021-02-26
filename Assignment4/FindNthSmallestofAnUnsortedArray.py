class Solution:
    def NthSmallest(self, n, nums):
        length = len(nums)
        return self.helper(nums, 0, length - 1, n - 1)
    
    def helper(self, nums, start, end, n):
        if start == end or start >= end:
            return nums[start]
        
        l= start
        r = end
        mid = (l + r) // 2
        pivot = nums[mid]

        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        if start <= right and n <= r:
            return self.helper(nums, start, r, n)
        if left <= end and n >= l:
            return self.helper(nums, l, end, n)
        return nums[n]