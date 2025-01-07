class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        
        fre = [0] * 26
        ans = []
        for i in range(len(words)):
            word1 = words[i]
            print("target Word", word1)
            for j in range(i + 1, len(words)):
                word2 = words[j]
                print("comparing word", word2)
                k = 0
                l = 0
                while(k < len(word1) and l < len(word2)):
                    if word1[k] == word2[l]:
                        k += 1
                        l += 1
                        print("k", k)
                    else:
                        
                        l += 1
                        if(k != 0):
                            k = 0
                            l -= k + 1
                        print("l", l)

                if k == len(word1):
                    print("i triggered")
                    ans.append(word1)
                    break

        return ans
            

            

        