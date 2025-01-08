class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = []
        count = 0
        for i in range(len(words)):
            supre = words[i]
            for j in range(i + 1, len(words)):
                comp = words[j]
                k = 0
                l = 0
                while k < len(supre) and l < len(comp):
                    if supre[k] == comp[l] and supre[-k] == comp[-l]:
                        k += 1
                        l += 1
                    else:
                        break 

                if k == len(supre):
                    count += 1
                    

        return count
        