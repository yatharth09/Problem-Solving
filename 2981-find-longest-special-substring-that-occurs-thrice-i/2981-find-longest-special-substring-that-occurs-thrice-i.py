class Solution:
    def maximumLength(self, s: str) -> int:
        mp = {}
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                flag = True
                for k in range(1, len(substr)):
                    if substr[k] != substr[k - 1]:
                        flag = False
                    
                if flag:
                    if substr not in mp:
                        mp[substr] = 1
                    else:
                        mp[substr] += 1

        
        ans = -1
        for key in mp:
            if mp[key] >= 3:
                
                ans = max(ans, len(key))

        return ans


            
            


            
        