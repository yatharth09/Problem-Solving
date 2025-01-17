class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        num1 = num2 = float('inf')
        num3 = 0

        for num in nums:
            num3 = num

            if num3 <= num1:
                num1 = num3
            elif num3 <= num2:
                num2 = num3
            else:
                return True
        
        return False
            
            
            
        