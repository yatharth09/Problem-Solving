class Solution:
    def isPrefixOfWord(self, sentence: str, word: str) -> int:
        i = 0
        j = 0
        ind = 1
        while i < len(sentence):


            if sentence[i] == word[j]:
                j += 1
                i += 1
            else:
                while i < len(sentence):
                    if sentence[i] == ' ':
                        ind += 1
                        break
                    i += 1
                i += 1
                j = 0

            if j == len(word):
                return ind

        return -1

            