class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        ind = []
        for i in range(len(s)):
            if s[i] in vowels:
                ind.append([s[i], i])
            
        
        for i in range(int(len(ind)/2)):
            ind[i][0], ind[-(i + 1)][0] = ind[-(i + 1)][0], ind[i][0]
        
        

        slist = list(s)

        for i in ind:
            slist[i[1]] = i[0]

        s = "".join(slist)

        return s


        

        

        
        