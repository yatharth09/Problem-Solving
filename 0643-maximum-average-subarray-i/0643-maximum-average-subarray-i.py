class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        low = high = 0
        summ = 0
        maxSumm = float('-inf')
        while high < len(nums):
            summ += nums[high]
            if high - low + 1 == k:
                maxSumm = max(maxSumm, summ)
                summ -= nums[low]
                low += 1
            high += 1
        
        return maxSumm / k


        