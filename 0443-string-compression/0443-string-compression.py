class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        count = 0
        prev = chars[0]
        for char in chars:
            
            if prev == char:
                count += 1
            else:
                if count == 1:
                    ans.append([prev, ""])
                else:
                    ans.append([prev, str(count)])
                count = 1
                prev = char

            char = "2"
            
            
        
        if count == 1:
            ans.append([prev, ""])
        else:
            ans.append([prev, str(count)])
        res = ""
        for i in ans:
            res += "".join(i)

        resList = list(res)
        
        chars[:len(resList)] = resList
        return len(resList)



        
                

            

        