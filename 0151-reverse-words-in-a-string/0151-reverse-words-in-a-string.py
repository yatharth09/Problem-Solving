class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for char in s:
            if char == " ":
                if word:
                    words.append(word)
                    word = ""
            else:
                word += char
            
        if word:
            words.append(word)

        words = words[::-1]

        ans = ""
        for word in words:
            ans = ans + word + " "
        
        return ans[:-1]

            

        