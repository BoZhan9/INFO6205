class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or strs[0] == 0:
            return ""
        res = ""
        for c in range(0, len(strs[0])):
            for i in range(0, len(strs)):
                if c == len(strs[i]) or strs[i][c] != strs[0][c]:
                    return res                
            res += strs[0][c]
        return res