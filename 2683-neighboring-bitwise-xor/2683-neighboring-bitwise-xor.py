class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived) - 1):
            if derived[i] == 1:
                temp = 0 if original[-1] == 1 else 1
                original.append(temp)
            else:
                original.append(original[-1])
        
        print(original)
        
        if derived[-1] == 0 and original[-1] == original[0]:
            return True
        

        if derived[-1] == 1 and original[-1] != original[0]:
            return True
        
        return False
       

       
                
        