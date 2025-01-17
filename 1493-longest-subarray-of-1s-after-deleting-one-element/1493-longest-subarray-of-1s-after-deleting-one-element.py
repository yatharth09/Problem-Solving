class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        low = high = 0
        summ = 0
        count = 0
        maxSum = 0
        while high < len(nums):
            summ += nums[high]
            maxSum = max(summ, maxSum)
            if nums[high] == 0:
                count += 1
            
            if count == 2:
                while count > 1:
                    if nums[low] == 0:
                        count -= 1
                    summ -= nums[low]
                    low += 1
                
            high += 1
        
        if 0 not in nums:
            return maxSum - 1
        return maxSum