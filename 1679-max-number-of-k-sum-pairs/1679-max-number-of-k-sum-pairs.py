class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = len(nums) - 1
        count = 0
        while low < high:
            if nums[low] + nums[high] == k:
                count += 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] > k:
                high -= 1
            else:
                low += 1
            
        
        return count
        