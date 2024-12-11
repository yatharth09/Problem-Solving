class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            y = nums[i] + 2*k
            greatest = 0
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = int(low + (high - low)/2)
                if nums[mid] <= y:
                    greatest = max(mid - i + 1, greatest)
                    low = mid + 1
                else:
                    high = mid - 1

            ans.append(greatest) 

        return max(ans)
            
        
        