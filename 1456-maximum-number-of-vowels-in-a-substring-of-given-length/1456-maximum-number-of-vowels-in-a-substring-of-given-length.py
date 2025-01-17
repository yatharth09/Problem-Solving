class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        low = high = 0
        count = 0
        vowels = list("aeiou")
        
        maxx = 0
        while high < len(s):
            if s[high] in vowels:
                count += 1
            if high - low + 1 == k:
                maxx = max(maxx, count)
                if s[low] in vowels:
                    count -= 1
                low += 1
            
            high += 1
        
        return maxx
        