class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        ind = 0
        spaces.append(len(s))
        for i in range(len(spaces)):
            
            ans = ans + s[ind: spaces[i]] + " "
            ind = spaces[i]
            if spaces[i] == len(s):
                ans = ans[:-1] 
        return ans
                