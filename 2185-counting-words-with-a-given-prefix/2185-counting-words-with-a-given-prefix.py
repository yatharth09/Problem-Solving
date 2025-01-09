class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        size = len(pref)
        count = 0
        for word in words:
            if pref == word[:size]:
                count += 1
            
        return count
            

        