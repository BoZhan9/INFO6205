class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        if not nums or len(nums) < 3:
            return ans
        
        for i in range(len(nums) - 2):
            sum = -nums[i]
            map = {}
            for j in range(i + 1, len(nums)):
                if sum - nums[j] in map:
                    res = [nums[i], nums[j], sum - nums[j]]
                    res.sort()
                    if res not in ans:
                        ans.append(res)
                else:
                    map[nums[j]] = j
        return ans