class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        m = 26
        n = 2 
        alpha = [[-1 for _ in range(n)] for _ in range(m)]
        ans = 0
        
        for i in range(26):

            left = -1
            right = -1
            char = chr(ord('a') + i)

            for j in range(len(s)):
                if s[j] == char and left != -1:
                    right = j

                if s[j] == char and left == -1:
                    left = j
                
                
            
            if left == -1 or right == -1:
                break

            mySet = set()
            for k in range(left + 1, right):
                mySet.add(s[k])
            

            ans += len(mySet)

        return ans

                
                


            

        