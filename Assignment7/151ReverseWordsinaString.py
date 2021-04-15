class Solution:
    def reverseWords(self, s: str) -> str:
        strs = []
        temp = []
        for c in s:
            if c == " ":
                if len(temp) == 0:
                    continue
                else:
                    strs.append(temp)
                    temp = [] 
                    continue
            temp.append(c)
        strs.append(temp)
        
        res = ""
        for index in range(len(strs) - 1, -1, -1):
            if len(strs[index]) < 1:
                continue
            for c in range(0, len(strs[index])):
                    res += strs[index][c]
            res += " "

        return res[:-1]