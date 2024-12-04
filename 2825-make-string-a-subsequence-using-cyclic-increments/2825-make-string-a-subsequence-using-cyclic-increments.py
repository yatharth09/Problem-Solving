class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        flag = True
        while i < len(str1):
            if j < len(str2) and (str1[i] == str2[j] or ((ord(str1[i]) + 1 == ord(str2[j]) or (str1[i] == 'z' and str2[j] == 'a')) and flag)):
                if ord(str1[i]) + 1 == ord(str2[j]):
                    flag = False
                j += 1
            i += 1
        
        return j == len(str2)
