class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        if n == 0:
            return ans
        
        self.helpler(ans, n, n, "")
        return ans

    def helpler(self, ans, left, right, temp):
        if right < left:
            return 
        
        # base case
        if left == 0 and right == 0:
            ans.append(temp)
            
        # go left and right recursion to find all permutation
        if left > 0:
            self.helpler(ans, left - 1, right, temp + "(")
        if right > 0:
            self.helpler(ans, left, right - 1, temp + ")")