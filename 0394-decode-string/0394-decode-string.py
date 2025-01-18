class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multiple = []
        num = []
        for char in s:
            
            if char == ']':
                ele = []
                while True:
                    ele.append(stack[-1])
                    stack.pop(-1)
                    if stack[-1] == "[":
                        ele = ele[::-1]
                        stack.pop(-1)
                        break
                
                multi = int(multiple[-1])
                multiple.pop(-1)
                newstring = multi * ele
                
                stack.append("".join(newstring))
            else:
                if char >= '0' and char <= '9':
                    num.append(char)
                else:
                    if len(num) != 0:
                        multiple.append("".join(num))
                        num = []
                    stack.append(char)
                
                
            

        return "".join(stack)
                    
                
        