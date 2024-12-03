class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0

        while(i < len(haystack)):
            while j < len(needle):
                if i < len(haystack) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    j = 0
                    break
            if j == len(needle):
                return abs(j - i)
            i += 1

        return -1