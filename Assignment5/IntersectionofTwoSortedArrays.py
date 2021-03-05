class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        inter = set() 

        i = 0
        j = 0

        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                inter.add(nums1[i])
                i += 1
                j += 1
        
        ans = []
        for num in inter:
            ans.append(num)
       
        return ans
        
        