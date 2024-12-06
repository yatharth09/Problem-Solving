class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        summ = 0
        for i in range(1, n + 1):
            if i not in banned:
                summ += i
                if summ > maxSum:
                    break
                count += 1
            
        return count
                
            

        